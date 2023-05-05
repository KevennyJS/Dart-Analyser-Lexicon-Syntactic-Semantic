import ply.yacc as yacc
from dart_lex import *
from sintaxe_abstrata import *

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
    if(len(p) == 2):
        if(isinstance (p[1],Funcdecl1)):
            p[0] = Funcdecl1(p[1])
        else:
            p[0] = Declvar1(p[1])
    else:
        if(isinstance (p[1],Funcdecl1)):
            p[0] = Funcdecl2(p[1],p[2])
            #Na hora de criarmos a classe Funcdecl na abstrata podemos passar por 1 parametro ou dois parametro
        else:
            p[0] = Declvar2(p[1],p[2])
    pass

def p_declvar(p):
    '''declvar : tipo assign SEMI_COLON
               | tipo INTERROGATION ID SEMI_COLON
    '''
    if(len(p) == 5):
        p[0] = DeclvarTipoInterrogationIdSemiColon(p[1],p[2],p[3],p[4])
    else:
        p[0] = DeclvarTipoAssignSemicolon(p[1],p[2],p[3])
    pass

def p_funcdecl(p):
    '''funcdecl : signature body'''
    p[0] = FuncdeclSignatureBody(p[1],p[2])
    pass

def p_signature(p):
    '''signature : tipo ID LPAREN sigParams RPAREN 
    | tipo ID LPAREN RPAREN '''
    if(len(p) == 6):
        p[0] = SignatureTipoIdLparenSigparamsRparen(p[1],p[2],p[3],p[4],p[5])
    else:
        p[0] = SignatureTipoIdLparenRparen(p[1],p[2],p[3],p[4])
    pass

def p_sigParams(p):
    '''sigParams : tipo ID 
                | tipo ID VIRGULA sigParams
    '''
    if(len(p) == 5):
        p[0] = SigParamsTipoIdVirgulaSigparams(p[1],p[2],p[3],p[4])
    else:
        p[0] = SigParamsTipoId(p[1],p[2])
    pass

def p_body(p):
    '''body : LCHAV stms RCHAV 
            | LCHAV RCHAV 
    '''
    if(len(p) == 4):
        p[0] = BodyLchaveStmsRchave(p[1],p[2],p[3])
    else:
        p[0] = BodyLchaveRchave(p[1],p[2])
    pass

#O if esta aqui porque a linguagem Dart nao recomenda if
#  com um comando sem abre chave e fecha chave
def p_bodyorstm(p):
    '''bodyorstm : stm 
                | body
                | body ELSE stm
                | body ELSE body
    '''
    if(p[1] == 'stm'):
        p[0] = BodyOrStmStm(p[1])
    elif(len(p) == 2):
        p[0] = BodyOrStmBody(p[1])
    elif(p[3] == 'stm'):
        p[0] = BodyOrStmBodyElseStm(p[1],p[2],p[3])
    else:
        #elif(isinstance (p[1],BodyOrStmBodyElseBody)):
        p[0] = BodyOrStmBodyElseBody(p[1],p[2],p[3])
    pass

def p_stms(p): 
    '''stms : stm  
            | stm  stms
    '''
    if(len(p) == 2):
        p[0] = StmsStm(p[1])
    else:
        p[0] = StmsStmStms(p[1],p[2])
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
    if(p[1] == 'exp'):
        p[0] = StmExpSemicolon(p[1],p[2])
    elif(p[1] == 'WHILE'):
        p[0] = StmWhileLparenExpRparenBody(p[1],p[2],p[3],p[4],p[5])
    elif(p[1] == 'RETURN'):
        p[0] = StmReturnExpSemicolon(p[1],p[2],p[3])
    elif(p[1] == 'IF'):
        p[0] = StmIfLparenExpRparenBodyorstm(p[1],p[2],p[3],p[4],p[5])
    elif(p[1] == 'declvar'):
        p[0] = StmDeclvar(p[1])
    elif(len(p) == 13):
        p[0] = StmForFor(p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8],p[9],p[10],p[11],p[12])
    elif(len(p) == 9):
        p[0] = StmForLparenTipoIdInIdRparenBody(p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8])
    #print(len(p))
    # else:
    #     p[0] = StmForLparenTipoIdInIdRparenBody(p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8])
    pass

def p_tiposassign(p):
    '''tiposassign : tipo  assign 
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

# def p_expMoreExp(p):
#     '''exp : exp MORE exp'''
#     p[0] = ExpMoreExp(p[1],p[3])
#     pass

# def p_expLessExp(p):
#     '''exp : exp LESS exp'''
#     p[0] = ExpLessExp(p[1],p[3])
#     pass

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
