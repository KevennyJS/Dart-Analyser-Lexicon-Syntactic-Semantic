from expression_parser import *
from testes import *

class Visitor:
    def visitFuncdecl1(self, classe):
        classe.funcdecl.accept(self)

    def visitFuncdecl2(self, classe):
        classe.funcdecl.accept(self)
        classe.program.accept(self)

    def visitDeclvar1(self, classe):
        classe.declvar.accept(self)

    def visitDeclvar2(self, classe):
        classe.declvar.accept(self)
        classe.program.accept(self)

    def visitDeclvarTipoInterrogationIdSemiColon(self, classe):
        classe.tipo.accept(self)
        print(f" ? {classe.idd};")

    def visitDeclvarTipoAssignSemicolon(self, classe):
        classe.tipo.accept(self)
        classe.assign.accept(self)

    def visitFuncdeclSignatureBody(self, classe):
        classe.signature.accept(self)
        classe.body.accept(self)

    def visitSignatureTipoIdLparenSigparamsRparen(self, classe):
        classe.tipo.accept(self)
        print(f" {classe.idd} ", end='')
        classe.sigparams.accept(self)

    def 

    def visitTipoVoid(self, classe):
        print("void")

if __name__ == "__main__":
    lexico = lex.lex()
    lexico.input(teste)

    parser = yacc.yacc()
    res = parser.parse()

    res.accept(Visitor())

    