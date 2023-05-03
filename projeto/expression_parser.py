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
    # if(len(p) == 2):
    #     if(isinstance (p[1],Funcdecl)):
    #         p[0] = Funcdecl(p[1])
    #         #Na hora de criarmos a classe Funcdecl na abstrata podemos passar por 1 parametro ou dois parametro
    #     else
    #         p[0] = Declvar(p[1])
    # else
    #     if(isinstance (p[1],Funcdecl)):
    #         p[0] = Funcdecl(p[1],p[2])
    #         #Na hora de criarmos a classe Funcdecl na abstrata podemos passar por 1 parametro ou dois parametro
    #     else
    #         p[0] = Declvar(p[1],p[2])
        
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
    '''body : LCHAV stms RCHAV 
            | LCHAV RCHAV 
    '''
    pass

#O if esta aqui porque a linguagem Dart nao recomenda if
#  com um comando sem abre chave e fecha chave
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
        | declvar
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

def p_call(p):
    '''call : ID LPAREN params RPAREN 
            | ID LPAREN RPAREN 
    '''
    pass



def p_exp(p):
    '''exp : exp MORE exp
           | exp LESS exp
           | exp MULTIPLICATION exp 
           | exp DIVIDE exp 
           | exp REST exp
           | exp MORE_EQUAL exp
           | exp MORETHAN exp 
           | exp LESS_EQUAL exp
           | exp LESSTHAN exp 
           | exp AS exp
           | exp IS exp
           | exp IS_EXCLAMATION exp
           | exp EQUAL exp
           | exp EXCLAMATION_EQUAL exp
           | exp AND exp
           | exp OR exp
           | exp IF_NULL exp
           | exp INTERROGATION exp COLON exp
           | exp MULTIPLICATION_EQUAL exp
           | exp DIVIDE_EQUAL exp
           | exp SOMA_EQUAL exp
           | exp SUB_EQUAL exp
           | exp MORE_MORE 
           | exp LESS_LESS
           | LPAREN exp RPAREN
           | AWAIT exp
           | DOT_DOT exp 
           | INTERROGATION DOT_DOT exp
           | call  
           | ID RECEIVE_VALUE exp
           | ID
           | NUM_INT
           | NUM_DOUBLE
           | STR_STRING
           | BOO_BOOLEAN
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
    '''tipo : TIPO_DOUBLE 
    | TIPO_INT
    | TIPO_STRING 
    | TIPO_BOOLEAN
    | TIPO_VOID'''
    pass

#def p_arrayTipo(p):
#    '''arrayTipo : List LESSTHAN tipo MORETHAN'''
#    pass

#def p_error(p):
#    p.yacc.skip()
#    pass
parser = yacc.yacc()
parser.parse(debug=False)
