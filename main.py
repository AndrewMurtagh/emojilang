from ply import lex, yacc
import emoji
import sys
import time

# Note: need to define all tokens as functions, not strings
tokens = [
    'COMMENT',

    # assignment
    'ASSIGNMENT',
    'VARIABLE',

    # numerical operators
    'TIMES',
    'PLUS',
    'DIVIDE',
    'MINUS',
    'MODULO',

    # boolean operators
    'EQUALS',
    'NOT_EQUALS',
    'LESS_THAN',
    'LESS_EQUALS_THAN',
    'GREATER_THAN',
    'GREATER_EQUALS_THAN',
    
    # delimiters
    'L_BRACKET',
    'R_BRACKET',
    'L_PAREN',
    'R_PAREN',

    # literals
    'NUMBER',
    'TRUE',
    'FALSE'
]



keywords = {
    'print' : 'PRINT',
    'if': 'IF',
    'while': 'WHILE',
    'sleep': 'SLEEP'
}

tokens = tokens + list(keywords.values())


# numerical operators
def t_TIMES(t):
    r':collision:'
    return t

def t_PLUS(t):
    r':sparkles:'
    return t


def t_DIVIDE(t):
    r':right_anger_bubble:'
    return t


def t_MINUS(t):
    r':dizzy:'
    return t


def t_MODULO(t):
    r':thought_balloon:'
    return t


# boolean operators
def t_EQUALS(t):
    r':full_moon:'
    return t

def t_NOT_EQUALS(t):
    r':new_moon:'
    return t

def t_LESS_THAN(t):
    r':waning_crescent_moon:'
    return t

def t_LESS_EQUALS_THAN(t):
    r':waning_gibbous_moon:'
    return t

def t_GREATER_THAN(t):
    r':waxing_crescent_moon:'
    return t

def t_GREATER_EQUALS_THAN(t):
    r':waxing_gibbous_moon:'
    return t

def t_COMMENT(t):
    r'\:shushing_face:.*'
    pass 


# literals
def t_TRUE(t):
    r':beaming_face_with_smiling_eyes:'
    return t

def t_FALSE(t):
    r':crying_face:'
    return t

def t_NUMBER(t):
    r'(?::keycap_\d:)+'
    numeric_value = t.value
    numeric_value = numeric_value.replace(':','').replace('keycap_', '')
    t.value = int(numeric_value)
    return t


# delimiters
def t_L_BRACKET(t):
    r':airplane_departure:'
    return t

def t_R_BRACKET(t):
    r':airplane_arrival:'
    return t


def t_L_PAREN(t):
    r':last_quarter_moon_face:'
    return t

def t_R_PAREN(t):
    r':first_quarter_moon_face:'
    return t

def t_ASSIGNMENT(t):
    r':pushpin:'
    return t

def t_IF(t):
    r':thinking_face:'
    return t

def t_WHILE(t):
    r':fire:'
    return t

def t_PRINT(t):
    r':loudspeaker:'
    return t

def t_SLEEP(t):
    r':ZZZ:'
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




stack = [True]
variables = {}
precedence = (
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE'),
)

def p_statements(p):
    '''statements : statements statement
        | statement'''
    p[0] = p[1]

def p_statement_print(p):
    '''statement : PRINT L_PAREN expression R_PAREN'''
    if not stack[-1]:
        return
    print('> ', p[3])

def p_statement_sleep(p):
    '''statement : SLEEP L_PAREN NUMBER R_PAREN'''
    if not stack[-1]:
        return
    time.sleep(p[3])

def p_statement_assign(p):
    'statement : VARIABLE ASSIGNMENT expression'
    variables[p[1]] = p[3]

def p_statement_if(p):
    '''statement : IF L_PAREN expression_boolean R_PAREN L_BRACKET if_start statements if_end R_BRACKET'''
    if p[3]:
        p[0] = p[6]
    else:
        p[0] = None

def p_if_start(p):
    '''
    if_start :
    '''
    if not stack[-1]:
        stack.append(False)
    else:
        stack.append(p[-3])
        
def p_if_end(p):
    '''
    if_end :
    '''
    stack.pop()


def p_statement_while(p):
    '''statement : WHILE L_PAREN expression_boolean R_PAREN L_BRACKET while_start statements while_end R_BRACKET'''
    pass


def p_while_start(p):
    """
    while_start :
    """
    if not stack[-1]:
        stack.append(False)
    else:
        stack.append(p[-3])


def p_while_end(p):
    """
    while_end :
    """
    stack.pop()
    if stack[-1] and p[-5]:
        print('HI')
        p.lexer.lexpos = parser.symstack[-7].lexpos


def p_expression_maths(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression MODULO expression'''
    if p[2] == t_PLUS.__doc__: 
        p[0] = p[1] + p[3]

    elif p[2] == t_MINUS.__doc__: 
        p[0] = p[1] - p[3]

    elif p[2] == t_TIMES.__doc__: 
        p[0] = p[1] * p[3]

    elif p[2] == t_DIVIDE.__doc__: 
        p[0] = p[1] / p[3]

    elif p[2] == t_MODULO.__doc__: 
        p[0] = p[1] % p[3]

def p_expression_paren(p):
    'expression : L_PAREN expression R_PAREN'
    p[0] = p[2]

def p_expression_boolean(p):
    '''expression_boolean : expression_boolean_comparison
        | expression_true
        | expression_false'''
    p[0] = p[1]

def p_expression_boolean_comparison(p):
    '''expression_boolean_comparison : expression EQUALS expression
        | expression NOT_EQUALS expression
        | expression LESS_THAN expression
        | expression LESS_EQUALS_THAN expression
        | expression GREATER_THAN expression
        | expression GREATER_EQUALS_THAN expression'''

    if p[2] == t_EQUALS.__doc__:
        p[0] = bool(p[1] == p[3])

    elif p[2] == t_NOT_EQUALS.__doc__:
        p[0] = bool(p[1] != p[3])

    elif p[2] == t_LESS_THAN.__doc__:
        p[0] = bool(p[1] < p[3])

    elif p[2] == t_LESS_EQUALS_THAN.__doc__:
        p[0] = bool(p[1] <= p[3])

    elif p[2] == t_GREATER_THAN.__doc__:
        p[0] = bool(p[1] > p[3])

    elif p[2] == t_GREATER_EQUALS_THAN.__doc__:
        p[0] = bool(p[1] >= p[3])


def p_expression_variable(p):
    'expression : VARIABLE'
    try:
        p[0] = variables[p[1]]
    except LookupError:
        print(f'Error > Undefined variable {p[1]}')
        raise 

def p_expression_true(p):
    'expression_true : TRUE'
    p[0] = True

def p_expression_false(p):
    'expression_false : FALSE'
    p[0] = False

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]


def p_error(p):
    print(f'Error > Syntax error in source code: {str(p)}')


source_code = '''🐸📌4️⃣💥🌜3️⃣✨5️⃣🌛
🤔🌜🐸🌕3️⃣2️⃣🌛 🛫
    🤫 this should be executed
    📢🌜1️⃣🌛
🛬
'''

# print(emoji.demojize(''))
lexer.input(emoji.demojize(source_code))

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)

parser = yacc.yacc(write_tables=False, debug=True)
res = yacc.parse(emoji.demojize(source_code))