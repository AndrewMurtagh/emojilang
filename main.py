from ply import lex, yacc
import emoji

# Note: need to define all tokens as functions, not strings

tokens = [
    'NUMBER',
    'COMMENT',
    'L_PAREN',
    'R_PAREN',
    'ASSIGNMENT',
    'VARIABLE',
    'EQUALITY',
    'L_BRACKET',
    'R_BRACKET',
]

keywords = {
    'print' : 'PRINT',
    'if': 'IF'
}

tokens = tokens + list(keywords.values())


def t_L_BRACKET(t):
    r':airplane_departure:'
    return t

def t_R_BRACKET(t):
    r':airplane_arrival:'
    return t

def t_EQUALITY(t):
    r':sun_behind_small_cloud:'
    return t

def t_COMMENT(t):
    r'\:shushing_face:.*'
    pass 

def t_L_PAREN(t):
    r':last_quarter_moon_face:'
    return t

def t_R_PAREN(t):
    r':first_quarter_moon_face:'
    return t

def t_ASSIGNMENT(t):
    r':pushpin:'
    return t

def t_NUMBER(t):
    r'(?::keycap_\d:)+'
    numeric_value = t.value
    numeric_value = numeric_value.replace(':','').replace('keycap_', '')
    t.value = int(numeric_value)
    return t

def t_IF(t):
    r':thinking_face:'
    return t

def t_PRINT(t):
    r':loudspeaker:'
    return t

def t_VARIABLE(t):
    r':[a-z]+:'
    t.type = keywords.get(t.value, 'VARIABLE')
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore  = ' \t'

def t_error(t):
    print(f'Error > Illegal value in source code: {t.value[0]}')
    t.lexer.skip(1)

lexer = lex.lex()



source_code = '''
🦁📌1️⃣
🤫 this is a comment
📢🌜🦁🌛
📢🌜1️⃣🌛
🤫 this is a comment
'''

source_code = '''
🤔🌜1️⃣🌤️1️⃣🌛 🛫 
    📢🌜2️⃣🌛
    🤔🌜1️⃣🌤️1️⃣🌛 🛫 
        📢🌜3️⃣🌛
    🛬
🛬
'''
source_code = '''
🤔🌜1️⃣🌤️1️⃣🌛 🛫 
    🤫 this should be executed
    📢🌜2️⃣🌛
    🤔🌜1️⃣🌤️9️⃣🌛 🛫 
        🤫 this should not be executed
        📢🌜3️⃣🌛
    🛬
🛬
'''




print(emoji.demojize(source_code))
lexer.input(emoji.demojize(source_code))

print('---LEXING---\n\n')
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)


stack = [True]
variables = {}

def p_statements(p):
    '''statements : statements statement
        | statement'''
    p[0] = p[1]

def p_statement_print(p):
    '''statement : PRINT L_PAREN expression R_PAREN'''
    if not stack[-1]:
        return
    print('> ', p[3])

def p_statement_assign(p):
    'statement : VARIABLE ASSIGNMENT expression'
    variables[p[1]] = p[3]

def p_statement_if(p):
    '''statement : IF L_PAREN comparison R_PAREN L_BRACKET append_stack statements pop_stack R_BRACKET '''
    if p[3]:
        p[0] = p[6]
    else:
        p[0] = None

def p_comparison_binop(p):
    '''comparison : expression EQUALITY expression'''
    if p[2] == ':sun_behind_small_cloud:':
        p[0] = bool(p[1] == p[3])

def p_append_stack(p):
    '''
    append_stack :
    '''
    if not stack[-1]:
        stack.append(False)
    else:
        stack.append(p[-3])
        
def p_pop_stack(p):
    '''
    pop_stack :
    '''
    stack.pop()

def p_expression_variable(p):
    'expression : VARIABLE'
    try:
        p[0] = variables[p[1]]
    except LookupError:
        print(f'Error > Undefined variable {p[1]}')
        raise 

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_error(p):
    print(f'Error > Syntax error in source code: {str(p)}')



yacc.yacc(write_tables=False, debug=True)

print('\n\n---EXECUTING---\n\n')
res = yacc.parse(emoji.demojize(source_code))

# print(variables)