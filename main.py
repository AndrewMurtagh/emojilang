from ply import lex, yacc

tokens = [
    'SMILE'
]

t_SMILE = r'😀'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore  = ' \t'

def t_error(t):
    print(f'Illegal value {t.value[0]}')
    t.lexer.skip(1)

lexer = lex.lex()



source_code = '''😀
'''


lexer.input(source_code)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
