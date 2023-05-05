import ply.yacc as yacc
from dart_lex import *
from sintaxe_abstrata import *

def p_exp(p):
    '''exp : exp MAIS exp1 
           | exp MENOS exp1 
           | exp1'''
    if(len(p) == 2):
        p[0] = p[1]
    elif(p[2]=='MAIS'):
        p[0] = SomaExp(p[1], p[3])
    else:
        p[0] = SubExp(p[1], p[3])

def p_exp1(p):
    '''exp1 : NUM'''
    p[0] = Num(p[1])


parser = yacc.yacc()
parser.parse(debug=True)