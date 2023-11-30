from ply import lex, yacc

tokens = [
    'NUMBER',
    'L_PAREN',
    'R_PAREN'
]

keywords = {
    'print' : 'PRINT',
}

tokens = tokens + list(keywords.values())

t_PRINT = r'📢'
t_L_PAREN = r'🌜'
t_R_PAREN = r'🌛'



def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore  = ' \t'

def t_error(t):
    print(f'Error: Illegal value in source code: {t.value[0]}')
    t.lexer.skip(1)

lexer = lex.lex()



source_code = '''📢🌜5🌛
'''


lexer.input(source_code)

print('---LEXING---\n\n')
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)


stack = [True]

def p_statements(p):
    '''statements : statements statement
        | statement'''
    p[0] = p[1]

def p_statement_print(p):
    '''statement : PRINT L_PAREN expression R_PAREN'''
    if not stack[-1]:
        return
    print('print: ', p[3])



def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]



def p_error(p):
    print(f'Error: Syntax error in source code: {str(p)}')



yacc.yacc(write_tables=False, debug=True)

print('\n\n---EXECUTING---\n\n')
res = yacc.parse(source_code)