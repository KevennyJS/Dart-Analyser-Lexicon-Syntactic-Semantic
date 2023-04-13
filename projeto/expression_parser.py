import ply.yacc as yacc
from dart_lex import *

precedence = (
    ("right","RECEIVE_VALUE","MULTIPLICATION_EQUAL","DIVIDE_EQUAL","SOMA_EQUAL","SUB_EQUAL"),
    ("left","DOT_DOT"),
    ("right","INTERROGATION","COLON"),
    ("left","OR","AND","IF_NULL"),
    ("nonassoc","EQUAL","EXCLAMATION_EQUAL"),
    ("nonassoc","MORE_EQUAL","MORETHAN","LESS_EQUAL","LESSTHAN","AS","IS","IS_EXCLAMATION"),
    ("left","COMMERCIAL_E"),
    ("left", "MORE","LESS"),
    ("left", "MULTIPLICATION","DIVIDE", "REST"),
    ('nonassoc',"MORE_MORE","LESS_LESS","EXCLAMATION","AWAIT"),
    )

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
                | body ELSE stm
                | body ELSE body

    '''
    pass

def p_stms(p): 
    '''stms : stm  
            | stm  stms
    '''
    pass

def p_stm(p):
    '''stm : exp SEMI_COLON 
        | WHILE LPAREN exp RPAREN body
        | RETURN exp SEMI_COLON 
        | IF LPAREN exp RPAREN bodyorstm
        | FOR LPAREN tiposassign INTERROGATION SEMI_COLON exp INTERROGATION SEMI_COLON exp INTERROGATION  RPAREN body
        | FOR LPAREN tipo ID IN ID RPAREN body
    '''
    pass

# def if1(p):
#     '''if1 : IF'''

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

def p_call(p):
    '''call : ID LPAREN params RPAREN 
            | ID LPAREN RPAREN 
    '''
    pass

#precedence


def p_exp(p):
    '''exp : exp1 MORE exp
           | exp1 LESS exp
           | exp1 MULTIPLICATION exp 
           | exp1 DIVIDE exp 
           | exp1 REST exp
           | exp1 MORE_EQUAL exp
           | exp1 MORETHAN exp 
           | exp1 LESS_EQUAL exp
           | exp1 LESSTHAN exp 
           | exp1 AS exp
           | exp1 IS exp
           | exp1 IS_EXCLAMATION exp
           | exp1 EQUAL exp
           | exp1 EXCLAMATION_EQUAL exp
           | exp1 AND exp
           | exp1 OR exp
           | exp1 IF_NULL exp
           | exp1 INTERROGATION exp COLON exp
           | exp1 MULTIPLICATION_EQUAL exp
           | exp1 RECEIVE_VALUE exp 
           | exp1 DIVIDE_EQUAL exp
           | exp1 SOMA_EQUAL exp
           | exp1 SUB_EQUAL exp
           | exp1 MORE_MORE 
           | exp1 LESS_LESS
           | AWAIT exp
           | DOT_DOT exp 
           | INTERROGATION DOT_DOT exp
           | call  
           | assign  
           | INT
           | DOUBLE
           | ID
    '''
    pass

def p_exp1(p):
    '''exp1 : LPAREN exp RPAREN '''

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
