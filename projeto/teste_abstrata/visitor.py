from expression_parser import *

tab = 0

def blank():
    p = ''
    for x in range(tab):
        p = p + ' '
    return 

class Visitor():
    def visitSomaExp(self, somaExp):
        somaExp.exp1.accept(self)
        print(' + ', end='')
        somaExp.exp2.accept(self)
    
    def visitSubExp(self, somaExp):
        somaExp.exp1.accept(self)
        print(' - ', end='')
        somaExp.exp2.accept(self)

    def visitNum(self, num):
        print(num.num, end='')

def main():
    f = open("input1.su", "r")
    lexer = lex.lex()
    lexer.input(f.read())
    parser = yacc.yacc()
    result = parser.parse(debug=False)
    print("#imprime o programa que foi passado como entrada")
    visitor = Visitor()
    print(f"RESULT: {result}")
    result.accept(visitor)

if __name__ == "__main__":
    main()