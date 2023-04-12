import ply.yacc as yacc
from dart_lex import *

#precedence = (("left", "MORE","LESS"),
#("left", "LESS"),
#("right", "")
#)

def p_program(p):
    '''program : funcdecl
                | funcdecl program
                | declvar
                | declvar program
    '''
    pass

def p_declvar(p):
    '''declvar : tipo assign SEMI_COLON
               | tipo INTERROGATION ID SEMI_COLON
    '''
    pass

def p_funcdecl(p):
    '''funcdecl : signature body'''
    pass

def p_signature(p):
    '''signature : tipo ID LPAREN sigParams RPAREN 
    | tipo ID LPAREN RPAREN '''
    pass

def p_sigParams(p):
    '''sigParams : tipo ID 
                | tipo ID VIRGULA sigParams
    '''
    pass

def p_body(p):
    '''body : LCHAV stms RCHAV '''
    pass

def p_bodyorstm(p):
    '''bodyorstm : stm 
                | body
    '''
    pass

def p_stms(p): 
    '''stms : stm  
            | stm  stms
    '''
    pass

def p_stm(p):
    '''stm : exp SEMI_COLON 
        | WHILE LPAREN exp RPAREN bodyorstm 
        | RETURN exp SEMI_COLON 
        | IF LPAREN exp RPAREN bodyorstm 
        | IF LPAREN exp RPAREN bodyorstm elsif stm 
        | FOR LPAREN tiposassign INTERROGATION SEMI_COLON exp INTERROGATION SEMI_COLON exp INTERROGATION  RPAREN body
        | FOR LPAREN tipo ID IN ID RPAREN body
    '''
    pass

def p_tiposassign(p):
    '''tiposassign : tipo INTERROGATION  assign 
                | tipo tipoassigns
    '''
    pass

def p_tipoassigns(p):
    '''tipoassigns : assign 
                | assign VIRGULA tipoassigns
    '''
    pass
            
def p_elsif(p):
    '''elsif : ELSE IF LPAREN exp RPAREN body 
            | ELSE IF LPAREN exp RPAREN body elsif
            | ELSE body
    '''
    pass

def p_call(p):
    '''call : ID LPAREN params RPAREN 
            | ID LPAREN RPAREN 
    '''
    pass

#precedence

def p_exp(p):
    '''exp : exp MORE exp 
           | exp LESS exp 
           | exp MULTIPLICATION exp 
           | exp DIVIDE exp 
           | exp REST exp 
           | exp MORE_THAN RECEIVE_VALUE exp
           | exp MORETHAN exp 
           | exp LESSTHAN RECEIVE_VALUE exp
           | exp LESSTHAN exp 
           | exp AS exp
           | exp IS exp
           | exp IS EXCLAMATION exp
           | exp EQUAL exp
           | exp EXCLAMATION RECEIVE_VALUE exp
           | exp AND exp
           | exp OR exp
           | exp INTERROGATION  INTERROGATION exp
           | exp INTERROGATION exp COLON exp
           | DOT DOT exp 
           | INTERROGATION DOT DOT exp
           | exp RECEIVE_VALUE exp 
           | exp MULTIPLICATION RECEIVE_VALUE exp
           | exp DIVIDE RECEIVE_VALUE exp
           | exp MORE RECEIVE_VALUE exp
           | exp LESS RECEIVE_VALUE exp
           | exp MORE MORE 
           | exp LESS LESS
           | call  
           | assign  
           | INT
           | DOUBLE
           | ID
    '''
    pass

def p_params(p):
    '''params : exp VIRGULA params 
            | exp
    '''
    pass

def p_assign(p):
    '''assign : ID RECEIVE_VALUE exp'''
    pass

def p_tipo(p):
    '''tipo : DOUBLE 
    | INT
    | STRING 
    | BOOLEAN 
    | VOID'''
    pass

#def p_arrayTipo(p):
#    '''arrayTipo : List LESSTHAN tipo MORETHAN'''
#    pass

#def p_error(p):
#    p.yacc.skip()
#    pass

parser = yacc.yacc()
parser.parse(debug=True)