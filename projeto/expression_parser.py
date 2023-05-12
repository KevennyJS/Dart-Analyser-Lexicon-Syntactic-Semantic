import ply.yacc as yacc
from dart_lex import *
from sintaxe_abstrata import *
from testes import *

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
        else:
            p[0] = Declvar2(p[1],p[2])
    pass

def p_declvar(p):
    '''declvar : tipo assign SEMI_COLON
               | tipo INTERROGATION ID SEMI_COLON
    '''
    if(len(p) == 5):
        p[0] = DeclvarTipoInterrogationIdSemiColon(p[1],p[3])
    else:
        p[0] = DeclvarTipoAssignSemicolon(p[1],p[2])
    pass

def p_funcdecl(p):
    '''funcdecl : signature body'''
    p[0] = FuncdeclSignatureBody(p[1],p[2])
    pass

def p_signature(p):
    '''signature : tipo ID LPAREN sigParams RPAREN 
    | tipo ID LPAREN RPAREN '''
    if(len(p) == 6):
        p[0] = SignatureTipoIdLparenSigparamsRparen(p[1],p[2],p[4])
    else:
        p[0] = SignatureTipoIdLparenRparen(p[1],p[2])
    pass

def p_sigParams(p):
    '''sigParams : tipo ID 
                | tipo ID VIRGULA sigParams
    '''
    if(len(p) == 5):
        p[0] = SigParamsTipoIdVirgulaSigparams(p[1],p[2],p[4])
    else:
        p[0] = SigParamsTipoId(p[1],p[2])
    pass

def p_body(p):
    '''body : LCHAV stms RCHAV 
            | LCHAV RCHAV 
    '''
    if(len(p) == 4):
        p[0] = BodyLchaveStmsRchave(p[2])
    else:
        p[0] = BodyLchaveRchave()
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
        p[0] = BodyOrStmBodyElseStm(p[1],p[3])
    else:
        #elif(isinstance (p[1],BodyOrStmBodyElseBody)):
        p[0] = BodyOrStmBodyElseBody(p[1],p[3])
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
        | FOR LPAREN tiposassign SEMI_COLON midfor  SEMI_COLON midfor  RPAREN body
        | FOR LPAREN tipo ID IN ID RPAREN body
        | declvar
    '''

    if(p[1] == 'exp'):
        p[0] = StmExpSemicolon(p[1])
    elif(p[1] == 'WHILE'):
        p[0] = StmWhileLparenExpRparenBody(p[3],p[5])
    elif(p[1] == 'RETURN'):
        p[0] = StmReturnExpSemicolon(p[2])
    elif(p[1] == 'IF'):
        p[0] = StmIfLparenExpRparenBodyorstm(p[3],p[5])
    elif(p[1] == 'declvar'):
        p[0] = StmDeclvar(p[1])
    elif(len(p) == 10):
        p[0] = StmForFor(p[3],p[5],p[7],p[9])
    elif(len(p) == 9):
        p[0] = StmForLparenTipoIdInIdRparenBody(p[3],p[4],p[6],p[8])
    pass

def p_tiposassign(p):
    '''tiposassign : tipo  assign 
                | tipo assign VIRGULA tipoassigns
                | 
    '''
    
    pass

def p_tipoassigns(p):
    '''tipoassigns : assign
                | assign VIRGULA tipoassigns
    '''
    pass

def p_midFor(p):
    '''midfor : exp
              |
    '''
    pass

def p_call(p):
    '''call : ID LPAREN params RPAREN 
            | ID LPAREN RPAREN 
    '''
    pass

def p_expMoreExp(p):
    '''exp : exp MORE exp'''
    p[0] = ExpMoreExp(p[1],p[3])
    pass

def p_expLessExp(p):
    '''exp : exp LESS exp'''
    p[0] = ExpLessExp(p[1],p[3])
    pass

def p_expRestExp(p):
    '''exp : exp REST exp'''
    p[0] = ExpRestExp(p[1],p[3])
    pass

def p_expMultiplicationExp(p):
    '''exp : exp MULTIPLICATION exp'''
    p[0] = ExpMultiplicationExp(p[1],p[3])
    pass

def p_expDivideExp(p):
    '''exp : exp DIVIDE exp'''
    p[0] = ExpDivideExp(p[1],p[3])
    pass

def p_expMoreEqualExp(p):
    '''exp : exp MORE_EQUAL exp'''
    p[0] = ExpMoreEqualExp(p[1],p[3])
    pass

def p_expMoreThanExp(p):
    '''exp : exp MORETHAN exp'''
    p[0] = ExpMoreThanExp(p[1],p[3])
    pass

def p_expLessEqualExp(p):
    '''exp : exp LESS_EQUAL exp'''
    p[0] = ExpLessEqualExp(p[1],p[3])
    pass

def p_expLessThanExp(p):
    '''exp : exp LESSTHAN exp'''
    p[0] = ExpLessThanExp(p[1],p[3])
    pass

def p_expAsExp(p):
    '''exp : exp AS exp'''
    p[0] = ExpAsExp(p[1],p[3])
    pass

def p_expIsExp(p):
    '''exp : exp IS exp'''
    p[0] = ExpIsExp(p[1],p[3])
    pass

def p_expIsExclamationExp(p):
    '''exp : exp IS_EXCLAMATION exp'''
    p[0] = ExpIsExclamationExp(p[1],p[3])
    pass

def p_expEqualExp(p):
    '''exp : exp EQUAL exp'''
    p[0] = ExpEqualExp(p[1],p[3])
    pass

def p_expExclamationEqualExp(p):
    '''exp : exp EXCLAMATION_EQUAL exp'''
    p[0] = ExpExclamationEqualExp(p[1],p[3])
    pass

def p_expAndExp(p):
    '''exp : exp AND exp'''
    p[0] = ExpAndExp(p[1],p[3])
    pass

def p_expOrExp(p):
    '''exp : exp OR exp'''
    p[0] = ExpOrExp(p[1],p[3])
    pass

def p_expIfNullExp(p):
    '''exp : exp IF_NULL exp'''
    p[0] = ExpIfNullExp(p[1],p[3])
    pass

def p_expInterrogationExpColonExp(p):
    '''exp : exp INTERROGATION exp COLON exp'''
    p[0] = ExpInterrogationExpColonExp(p[1],p[3],p[5])
    pass

def p_expMultiplocationEqualExp(p):
    '''exp : exp MULTIPLICATION_EQUAL exp'''
    p[0] = ExpMultiplocationEqualExp(p[1],p[3])
    pass

def p_expDivideEqualExp(p):
    '''exp : exp DIVIDE_EQUAL exp'''
    p[0] = ExpDivideEqualExp(p[1],p[3])
    pass

def p_expSomaEqualExp(p):
    '''exp : exp SOMA_EQUAL exp'''
    p[0] = ExpSomaEqualExp(p[1],p[3])
    pass

def p_expSubEqualExp(p):
    '''exp : exp SUB_EQUAL exp'''
    p[0] = ExpSubEqualExp(p[1],p[3])
    pass

def p_expSubEqualExp(p):
    '''exp : exp SUB_EQUAL exp'''
    p[0] = ExpSubEqualExp(p[1],p[3])
    pass

def p_expMoreMore(p):
    '''exp : exp MORE_MORE'''
    p[0] = ExpMoreMore(p[1])
    pass

def p_expLessLess(p):
    '''exp : exp LESS_LESS'''
    p[0] = ExpLessLess(p[1])
    pass

def p_expLparenExpRparen(p):
    '''exp : LPAREN exp RPAREN'''
    p[0] = ExpLparenExpRparen(p[2])
    pass

def p_expAwaitExp(p):
    '''exp : AWAIT exp'''
    p[0] = ExpAwaitExp(p[2])
    pass

def p_expDotDotExp(p):
    '''exp : DOT_DOT exp'''
    p[0] = ExpDotDotExp(p[2])
    pass

def p_expInterrogationDotDotExp(p):
    '''exp : INTERROGATION DOT_DOT exp'''
    p[0] = ExpInterrogationDotDotExp(p[3])
    pass

def p_expCall(p):
    '''exp : call'''
    p[0] = ExpCall(p[1])
    pass

def p_expIdReceiveValueExp(p):
    '''exp : ID RECEIVE_VALUE exp'''
    p[0] = ExpIdReceiveValueExp(p[1],p[3])
    pass

def p_expId(p):
    '''exp : ID'''
    p[0] = ExpId(p[1])
    pass

def p_expNumInt(p):
    '''exp : NUM_INT'''
    p[0] = ExpNumInt(p[1])
    pass

def p_expNumDouble(p):
    '''exp : NUM_DOUBLE'''
    p[0] = ExpNumDouble(p[1])
    pass

def p_expStrString(p):
    '''exp : STR_STRING'''
    p[0] = ExpStrString(p[1])
    pass

def p_expBoolean(p):
    '''exp : BOO_BOOLEAN
    '''
    p[0] = ExpBoolean(p[1])
    pass

def p_params(p):
    '''params : exp VIRGULA params 
            | exp
    '''
    if(len(p) == 2):
        p[0] = ParamsExp(p[1])
    else:
        p[0] = ParamsExpVirgulaParams(p[1],p[3])
    pass

def p_assign(p):
    '''assign : ID RECEIVE_VALUE exp'''
    p[0] = AssignIdReceiveValueExp(p[1],p[3])
    pass

def p_tipo(p):
    '''tipo : TIPO_DOUBLE 
    | TIPO_INT
    | TIPO_STRING 
    | TIPO_BOOLEAN
    | TIPO_VOID'''
    if(p[1] == "TIPO_DOUBLE"):
        p[0] = TipoDouble()
    elif(p[1] == "TIPO_INT"):
        p[0] = TipoInt()
    elif(p[1] == "TIPO_STRING"):
        p[0] = TipoString()
    elif(p[1] == "TIPO_BOOLEAN"):
        p[0] = TipoBoolean()
    else:
        p[0] = TipoVoid()
    pass


if __name__ == "__main__":
    lexico = lex.lex()
    lexico.input(vere_codes)

    parser = yacc.yacc()
    parser.parse(debug=False)
