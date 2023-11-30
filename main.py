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
]

keywords = {
    'print' : 'PRINT',
}

tokens = tokens + list(keywords.values())


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


# print(emoji.demojize(source_code))
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


def p_expression_variable(p):
    'expression : VARIABLE'
    try:
        p[0] = variables[p[1]]
    except LookupError:
        # print("Undefined name '%s'" % p[1])
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