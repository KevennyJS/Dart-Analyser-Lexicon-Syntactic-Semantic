from expression_parser import *

tab = 0

def blank():
    p = ''
    for x in range(tab):
        p = p + ' '
    return 

class Visitor():
    def visitFuncdecl1(self, classe):
        classe.funcdecl.accept(self)

    def visitFuncdecl2(self, classe):
        classe.funcdecl.accept(self)
        classe.program.accept(self)

    def visitDeclvar1(self, classe):
        classe.declvar.accept(self)
    
    def visitDeclvar2(self, classe):
        print("(program)(program)(program)(program)(program)(program)(program)(program)")
        classe.declvar.accept(self)
        print("(program)(program)(program)(program)(program)(program)(program)(program)")
        classe.program.accept(self)

    def visitDeclvarTipoInterrogationIdSemiColon(self, classe):
        classe.tipo.accept(self)
        print(f" {classe.idd} ")

    def visitDeclvarTipoAssignSemicolon(self, classe):
        classe.tipo.accept(self)
        classe.assign.accept(self)

    def visitFuncdeclSignatureBody(self, classe):
        classe.signature.accept(self)
        classe.body.accept(self)

    def visitSignatureTipoIdLparenSigparamsRparen(self, classe):
        classe.tipo.accept(self)
        print(f" {classe.idd} (", end='')
        classe.sigparams.accept(self)
        print(")")

    def visitSignatureTipoIdLparenRparen(self, classe):
        classe.tipo.acceps(self)
        print(f" {classe.idd} ()")
        
    def visitSigParamsTipoId(self, classe):
        classe.tipo.accept(self)
        print(f" {classe.idd}")

    def visitSigParamsTipoIdVirgulaSigparams(self, classe):
        classe.tipo.accept(self)
        print(f" {classe.idd}, ",end = '')
        classe.sigparams.accept(self)

    def visitBodyLchaveStmsRchave(self, classe):
        print("(",end='')
        classe.stms.accept(self)
        print(")",end='')

    def visitBodyLchaveRchave(self, classe):
        print("()")

    def visitBodyOrStmStm(self, classe):
        classe.stm.accept(self)

    def visitBodyOrStmBody(self, classe):
        classe.body.accept(self)

    def visitBodyOrStmBodyElseStm(self, classe):
        classe.body.accept(self)
        print("else")
        classe.stm.accept(self)

    def visitBodyOrStmBodyElseBody(self, classe):
        classe.body.accept(self)
        print("else")
        classe.bodyy.accept(self)

    def visitStmsStm(self, classe):
        classe.stm.accept(self)

    def visitStmsStmStms(self, classe):
        classe.stm.accept(self)
        classe.stms.accept(self)


    def visitStmExpSemicolon(self, classe):
        classe.exp.accept(self)
        print(";")

    def visitStmWhileLparenExpRparenBody(self, classe):
        print("while(",end='')
        classe.exp.accept(self)
        print(")",end='')
        classe.body.accept(self)

    def visitStmIfLparenExpRparenBodyorstm(self, classe):
        classe.stm.accept(self)
        print('if(',end='')
        classe.exp.accept(self)
        print(')',end='')
        classe.bodyorstm.accept(self)

    def visitStmDeclvar(self, classe):
        classe.declvar.accept(self)

    def visitStmForLparenTipoIdInIdRparenBody(self, classe):
        print("for(",end='')
        classe.tipo.accept(self)
        print(f' {classe.idd} in {classe.iddd} ) ',end = '')
        classe.body.accept.accept(self)


    def visitStmForFor(self, classe):
        print('for (',end = '')
        classe.tiposassign.accept(self)
        print(';',end='')
        classe.midfor1.accept(self)
        print(';',end='')
        classe.midfor2.accept(self)
        print(')',end='')
        classe.body.accept(self)
        

    def visitTipoassignsTipoAssign(self, classe):
        classe.tipo.accept(self)
        classe.assign.accept(self)


    def visitTipoassignsTipoAssingVirgula(self, classe):
        classe.tipo.accept(self)
        classe.assign.accept(self)
        print(',',end='')
        classe.tipoAssign.accept(self)

    def visitTipoassignsAssign(self, classe):
        classe.assign.accept(self)

    def visitTipoAssagnsAssagnVirgula(self, classe):
        classe.assign.accept(self)
        print(',',end='')
        classe.tipoAssign.accept(self)

    def visitMidForExp(self, classe):
        classe.exp.accept(self)

    def visitCallParams(self, classe):
        print(f'{classe.idd}(',end='')
        classe.params.accept(self)
        print(')')

    def visitCallNoParams(self, classe):
        print(f'({classe.idd})')

    def visitExpMoreExp(self, classe):
        classe.exp1.accept(self)
        print("+",end='')
        classe.exp2.accept(self)

    def visitExpLessExp(self, classe):
        classe.exp1.accept(self)
        print("-",end='')
        classe.exp2.accept(self)

    def visitExpRestExp(self, classe):
        classe.exp1.accept(self)
        print("%",end='')
        classe.exp2.accept(self)

    def visitExpMultiplicationExp(self, classe):
        classe.exp1.accept(self)
        print("*",end='')
        classe.exp2.accept(self)

    def visitExpDivideExp(self, classe):
        classe.exp1.accept(self)
        print("/",end='')
        classe.exp2.accept(self)

    def visitExpMoreEqualExp(self, classe):
        classe.exp1.accept(self)
        print(">=",end='')
        classe.exp2.accept(self)

    def visitExpMoreThanExp(self, classe):
        classe.exp1.accept(self)
        print(">",end='')
        classe.exp2.accept(self)

    def visitExpLessEqualExp(self, classe):
        classe.exp1.accept(self)
        print("<=",end='')
        classe.exp2.accept(self)

    def visitExpLessThanExp(self, classe):
        classe.exp1.accept(self)
        print("<",end='')
        classe.exp2.accept(self)

    def visitExpAsExp(self, classe):
        classe.exp1.accept(self)
        print("as",end='')
        classe.exp2.accept(self)

    def visitExpIsExp(self, classe):
        classe.exp1.accept(self)
        print("is",end='')
        classe.exp2.accept(self)

    def visitExpIsExclamationExp(self, classe):
        classe.exp1.accept(self)
        print("is!",end='')
        classe.exp2.accept(self)

    def visitExpEqualExp(self, classe):
        classe.exp1.accept(self)
        print("==",end='')
        classe.exp2.accept(self)

    def visitExpExclamationEqualExp(self, classe):
        classe.exp1.accept(self)
        print("!=",end='')
        classe.exp2.accept(self)

    def visitExpAndExp(self, classe):
        classe.exp1.accept(self)
        print("&&",end='')
        classe.exp2.accept(self)

    def visitExpOrExp(self, classe):
        classe.exp1.accept(self)
        print("||",end='')
        classe.exp2.accept(self)

    def visitExpIfNullExp(self, classe):
        classe.exp1.accept(self)
        print("??",end='')
        classe.exp2.accept(self)

    def visitExpInterrogationExpColonExp(self, classe):
        classe.exp1.accept(self)
        print("?",end='')
        classe.exp2.accept(self)
        print(':',end='')
        classe.exp3.accept(self)

    def visitExpMultiplocationEqualExp(self, classe):
        classe.exp1.accept(self)
        print("*=",end='')
        classe.exp2.accept(self)

    def visitExpDivideEqualExp(self, classe):
        classe.exp1.accept(self)
        print("/=",end='')
        classe.exp2.accept(self)

    def visitExpSomaEqualExp(self, classe):
        classe.exp1.accept(self)
        print("+=",end='')
        classe.exp2.accept(self)

    def visitExpSubEqualExp(self, classe):
        classe.exp1.accept(self)
        print("-=",end='')
        classe.exp2.accept(self)

    def visitExpMoreMore(self, classe):
        classe.exp1.accept(self)
        print("++",end='')

    def visitExpLessLess(self, classe):
        classe.exp1.accept(self)
        print("--",end='')

    def visitExpLparenExpRparen(self, classe):
        print("(",end='')
        classe.exp1.accept(self)
        print(")",end='')

    def visitExpAwaitExp(self, classe):
        print("await",end='')
        classe.exp1.accept(self)
        
    def visitExpDotDotExp(self, classe):
        classe.exp1.accept(self)
        print("..")

    def visitExpInterrogationDotDotExp(self, classe):
        print("?..",end='')
        classe.exp1.accept(self)

    def visitExpCall(self,classe):
        classe.call.accept(self)

    def visitExpIdReceiveValueExp(self, classe):
        print(f' {classe.idd} = ',end='')
        classe.exp3.accept(self)
        
    def visitExpId(self, classe):
        print(f"{classe.idd} ", end='')
        
    def visitExpNumInt(self, classe):
        classe.exp1.accept(self)
        
    def visitExpNumDouble(self, classe):
        classe.exp1.accept(self)

    def visitExpStrString(self, classe):
        classe.exp1.accept(self)
        
    def visitExpBoolean(self, classe):
        classe.exp1.accept(self)

    def visitParamsExp(self, classe):
        classe.exp1.accept(self)

    def visitParamsExpVirgulaParams(self, classe):
        classe.exp.accept(self)
        print(" , ")
        classe.params.accept(self)
        
    def visitAssignIdReceiveValueExp(self, classe):
        print(" {idd} = ")
        classe.exp.accept(self)
        
    def visitTipoDouble(self, classe):
        print("double", endl='')

    def visitTipoInt(self, classe):
        print("int", endl='')

    def visitTipoString(self, classe):
        print("String",end='')

    def visitTipoBoolean(self, classe):
        print("bool",end='')

    def visitTipoVoid(self, classe):
        print("void",end='')


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