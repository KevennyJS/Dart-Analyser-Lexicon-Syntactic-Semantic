from abc import abstractmethod
from abc import ABCMeta

class Program(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class Funcdecl1(Program):
    def __init__(self, funcdecl):
        self.funcdecl = funcdecl
    def accept(self, visitor):
        return visitor.visitFuncdecl1(self)

class Funcdecl2(Program):
    def __init__(self, funcdecl, program):
        self.funcdecl = funcdecl
        self.program = program
    def accept(self, visitor):
        return visitor.visitFuncdecl2(self)

class Declvar1(Program):
    def __init__(self, declvar):
        self.declvar = declvar
    def accept(self, visitor):
        return visitor.visitDeclvar1(self)

class Declvar2(Program):
    def __init__(self, declvar, program):
        self.declvar = declvar
        self.program = program
    def accept(self, visitor):
        return visitor.visitDeclvar2(self)

class DeclvarTipoInterrogationIdSemiColon(Program):
    def __init__(self, tipo,interrogation,idd,semicolon):
        self.tipo = tipo
        #self.interrogation = interrogation
        self.id = idd
        #self.semicolon = semicolon
    def accept(self, visitor):
        return visitor.visitDeclvarTipoInterrogationIdSemiColon(self)
        
class DeclvarTipoAssignSemicolon(Program):
    def __init__(self,tipo,assign,semicolon):
        self.tipo = tipo
        self.assign = assign
        self.semicolon = semicolon
    def accept(self, visitor):
        return visitor.visitDeclvarTipoAssignSemicolon(self)

class FuncdeclSignatureBody(Program):
    def __init__(self,signature,body):
        self.signature = signature
        self.body = body
    def accept(self, visitor):
        return visitor.visitFuncdeclSignatureBody(self)

class SignatureTipoIdLparenSigparamsRparen(Program):
    def __init__(self,tipo,idd,lparen,sigparams,rparen):
        self.tipo = tipo
        self.idd = idd
        self.lparen = lparen
        self.sigparams = sigparams
        self.rparen = rparen
    def accept(self, visitor):
        return visitor.visitSignatureTipoIdLparenSigparamsRparen(self)

class SignatureTipoIdLparenRparen(Program):
    def __init__(self,tipo,idd,lparen,rparen):
        self.tipo = tipo
        self.idd = idd
        self.lparen = lparen
        self.rparen = rparen
    def accept(self, visitor):
        return visitor.visitSignatureTipoIdLparenRparen(self)

class SigParamsTipoId(Program):
    def __init__(self,tipo,idd):
        self.tipo = tipo
        self.idd = idd
    def accept(self, visitor):
        return visitor.visitSigParamsTipoId(self)

class SigParamsTipoIdVirgulaSigparams(Program):
    def __init__(self,tipo,idd,virgula,sigparams):
        self.tipo = tipo
        self.idd = idd
        self.virgula = virgula
        self.sigparams = sigparams
    def accept(self, visitor):
        return visitor.visitSigParamsTipoIdVirgulaSigparams(self)

class BodyLchaveStmsRchave(Program):
    def __init__(self,lchave,stms,rchave):
        self.lchave = lchave
        self.stms = stms
        self.rchave = rchave
    def accept(self, visitor):
        return visitor.visitBodyLchaveStmsRchave(self)

class BodyLchaveRchave(Program):
    def __init__(self,lchave,rchave):
        self.lchave = lchave
        self.rchave = rchave
    def accept(self, visitor):
        return visitor.visitBodyLchaveRchave(self)

class BodyOrStmStm(Program):
    def __init__(self,stm):
        self.stm = stm
    def accept(self, visitor):
        return visitor.visitBodyOrStmStm(self)

class BodyOrStmBody(Program):
    def __init__(self,body):
        self.body = body
    def accept(self, visitor):
        return visitor.visitBodyOrStmBody(self)

class BodyOrStmBodyElseStm(Program):
    def __init__(self,body,elsee,stm):
        self.body = body
        self.elsee = elsee
        self.stm = stm
    def accept(self, visitor):
        return visitor.visitBodyOrStmBodyElseStm(self)

class BodyOrStmBodyElseBody(Program):
    def __init__(self,body,elsee,bodyy):
        self.body = body
        self.elsee = elsee
        self.body = bodyy
    def accept(self, visitor):
        return visitor.visitBodyOrStmBodyElseBody(self)

class StmsStm(Program):
    def __init__(self,stm):
        self.stm = stm
    def accept(self, visitor):
        return visitor.visitStmsStm(self)

class StmsStmStms(Program):
    def __init__(self,stm,stms):
        self.stm = stm
        self.stms = stms
    def accept(self, visitor):
        return visitor.visitStmsStmStms(self)

class StmExpSemicolon(Program):
    def __init__(self,exp,semicolon):
        self.exp = exp
        self.semicolon = semicolon
    def accept(self, visitor):
        return visitor.visitStmExpSemicolon(self)

class StmWhileLparenExpRparenBody(Program):
    def __init__(self,whilee,lparen,exp,rparen,body):
        self.whilee = whilee
        self.lparen = lparen
        self.exp = exp
        self.rparen = rparen
        self.body = body
    def accept(self, visitor):
        return visitor.visitStmWhileLparenExpRparenBody(self)

class StmReturnExpSemicolon(Program):
    def __init__(self,returnn,exp,seimcolon):
        self.returnn = returnn
        self.exp = exp
        self.seimcolon = seimcolon
    def accept(self, visitor):
        return visitor.visitStmReturnExpSemicolon(self)

class StmIfLparenExpRparenBodyorstm(Program):
    def __init__(self,iff,lparen,exp,rparen,bodyorstm):
        self.iff = iff
        self.lparen = lparen
        self.exp = exp
        self.rparen = rparen
        self.bodyorstm = bodyorstm
    def accept(self, visitor):
        return visitor.visitStmIfLparenExpRparenBodyorstm(self)

class StmDeclvar(Program):
    def __init__(self,declvar):
        self.declvar = declvar
    def accept(self, visitor):
        return visitor.visitStmDeclvar(self)

class StmForLparenTipoIdInIdRparenBody(Program):
    def __init__(self,forr,lparen,tipo,idd,inn,iddd,rparen,body):
        self.forr = forr
        self.lparen = lparen
        self.tipo = tipo
        self.idd = idd
        self.inn = inn
        self.iddd = iddd
        self.rparen = rparen
        self.body = body
    def accept(self, visitor):
        return visitor.visitStmForLparenTipoIdInIdRparenBody(self)

class StmForFor(Program):
    #FOR LPAREN tiposassign INTERROGATION SEMI_COLON exp INTERROGATION SEMI_COLON exp INTERROGATION  RPAREN body
    def __init__(self,forr,lparen,tiposassign,interrogation1,semicolon1,exp1,interrogation2,semicolon2,exp2,interrogation3,rparen,body):
        self.forr = forr
        self.lparen = lparen
        self.tiposassign = tiposassign
        self.interrogation1 = interrogation1
        self.semicolon1 = semicolon1
        self.exp1 = exp1
        self.interrogation2 = interrogation2
        self.semicolon2 = semicolon2
        self.exp2 = exp2
        self.interrogation3 = interrogation3
        self.rparen = rparen
        self.body = body
    def accept(self, visitor):
        return visitor.visitStmForFor(self)

class Exp(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

# class SomaExp(Exp):
#     def __init__(self, exp1, exp2):
#         self.exp1 = exp1
#         self.exp2 = exp2
#     def accept(self, visitor):
#         return visitor.visitSomaExp(self)


# class SubExp(Exp):
#     def __init__(self, exp1, exp2):
#         self.exp1 = exp1
#         self.exp2 = exp2
#     def accept(self, visitor):
#         return visitor.visitSubExp(self)

# class Num(Exp):
#     def __init__(self, num) :
#         self.num = num
#     def accept(self, visitor):
#         visitor.visitNum(self)
