import ply.yacc as yacc
from dart_lex import *

precedence = (("left", "MORE","LESS"),
("left", "LESS"),
("right", "")
)

def p_program(p):
    '''program : funcdecl
                | funcdecl program
                | declvar
                | decvar program
                '''

def p_declvar(p):
    '''declvar : tipo assign SEMI_COLON
               | tipo INTERROGATION ID SEMI_COLON
    '''

def p_funcdecl(p):
    '''funcdec1 : signature body'''

def p_signature(p):
    '''signature: tipo ID LPAREN sigParams RPAREN '''

def p_sigparams(p):
    '''sigparams: tipo ID 
                | tipo ID VIRGULA sigparams'''

def p_body(p):
    '''body: LCHAV stms RCHAV '''

def p_bodyorstm(p):
    '''bodyorstm: stm 
                | body'''

def p_stms(p): 
    '''stms: stm  
            | stm  stms'''

def p_stm(p):
    '''stm: exp SEMI_COLON 
        | WHILE LPAREN exp RPAREN bodyorstm| return exp SEMI_COLON 
        | IF LPAREN exp RPAREN bodyorstm 
        | IF LPAREN exp RPAREN bodyorstm ELSE stm 
        | FOR LPAREN tiposassign INTERROGATION SEMI_COLON exp INTERROGATION SEMI_COLON exp INTERROGATION  RPAREN body
        | FOR LPAREN tipo ID in ID RPAREN body'''

def p_tiposassign(p):
    '''tiposassign: tipo INTERROGATION  assign 
                | tipo tipoassigns'''

def p_tipoassigns(p):
    '''tipoassigns: assign 
                | assign VIRGULA tipoassigns'''
            
def p_elsif(p):
    '''elsif: ELSE IF LPAREN exp RPAREN body 
            | ELSE IF LPAREN exp RPAREN body elsif'''

def p_call(p):
    '''call: ID LPAREN params RPAREN 
            |ID LPAREN RPAREN '''

#precedence

def p_exp(p):
    '''exp: exp MORE exp 
           |exp LESS exp 
           |exp MULTIPLICATION exp 
           |exp DIVIDE exp 
           |exp REST exp 
           |exp MORE_THAN RECEIVE_VALUE exp
           |exp MORETHAN exp 
           |exp LESSTHAN RECEIVE_VALUE exp
           |exp LESSTHAN exp 
           |exp AS exp
           |exp IS exp
           |exp IS EXCLAMATION exp
           |exp EQUAL exp
           |exp EXCLAMATION RECEIVE_VALUE exp
           |exp AND exp
           |exp OR exp
           |exp INTERROGATION  INTERROGATION exp
           |exp expr1 INTERROGATION expr2 : expr3 exp 
           |DOT DOT exp | INTERROGATION DOT DOT exp
           |exp RECEIVE_VALUE exp 
           |exp MULTIPLICATION RECEIVE_VALUE exp
           |exp t_DIVIDE RECEIVE_VALUE exp
           |exp MORE RECEIVE_VALUE exp
           |exp LESS RECEIVE_VALUE exp
           |exp MORE MORE 
           |exp LESS LESS
           |call  
           |assign  
           |NUM  
           |ID'''

def p_params(p):
    '''params: exp VIRGULA params 
            | exp'''

def p_assign(p):
    '''assign: ID RECEIVE_VALUE exp'''

def p_tipo(p):
    '''tipo: DOUBLE | INT| STRING | BOOLEAN | "void"'''

def p_arrayTipo(p):
    '''arrayTipo: List LESSTHAN tipo MORETHAN'''
