import sys
import emoji
from emojilang import lexer, parser, variables

if __name__ == '__main__':
    if len(sys.argv)==2:
        file = sys.argv[1]
        with open(file) as f:
            source = f.read()
            print(emoji.demojize(source))
            lexer.input(emoji.demojize(source))

            while True:
                tok = lexer.token()
                if not tok:
                    break
                print(tok)

            # parser = yacc.yacc(write_tables=False, debug=True)
            res = parser.parse(emoji.demojize(source))
            print(variables)
    else:
        pass