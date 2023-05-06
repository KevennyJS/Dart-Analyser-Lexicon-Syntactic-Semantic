from abc import abstractmethod
from abc import ABCMeta

class Program(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class Declvar(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class Funcdecl(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class Signature(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class SigParams(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class Body(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class Bodyorstm(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class Stms(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class Stm(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class Tiposassign(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
###############################################################
#cuidado que sao coisas diferentes
class Tipoassigns(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class Midfor(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class Call(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class Exp(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class Params(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class Assign(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class Tipo(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

#################################################################################################
#################################################################################################
#################################################################################################
#################################################################################################
#################################################################################################
#################################################################################################
#################################################################################################
#################################################################################################
#################################################################################################
#################################################################################################



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
    def __init__(self, tipo,idd):
        self.tipo = tipo
        self.id = idd
    def accept(self, visitor):
        return visitor.visitDeclvarTipoInterrogationIdSemiColon(self)
        
class DeclvarTipoAssignSemicolon(Program):
    def __init__(self,tipo,assign):
        self.tipo = tipo
        self.assign = assign
    def accept(self, visitor):
        return visitor.visitDeclvarTipoAssignSemicolon(self)

class FuncdeclSignatureBody(Program):
    def __init__(self,signature,body):
        self.signature = signature
        self.body = body
    def accept(self, visitor):
        return visitor.visitFuncdeclSignatureBody(self)

class SignatureTipoIdLparenSigparamsRparen(Program):
    def __init__(self,tipo,idd,sigparams):
        self.tipo = tipo
        self.idd = idd
        self.sigparams = sigparams
    def accept(self, visitor):
        return visitor.visitSignatureTipoIdLparenSigparamsRparen(self)

class SignatureTipoIdLparenRparen(Program):
    def __init__(self,tipo,idd):
        self.tipo = tipo
        self.idd = idd
    def accept(self, visitor):
        return visitor.visitSignatureTipoIdLparenRparen(self)

class SigParamsTipoId(Program):
    def __init__(self,tipo,idd):
        self.tipo = tipo
        self.idd = idd
    def accept(self, visitor):
        return visitor.visitSigParamsTipoId(self)

class SigParamsTipoIdVirgulaSigparams(Program):
    def __init__(self,tipo,idd,sigparams):
        self.tipo = tipo
        self.idd = idd
        self.sigparams = sigparams
    def accept(self, visitor):
        return visitor.visitSigParamsTipoIdVirgulaSigparams(self)

class BodyLchaveStmsRchave(Program):
    def __init__(self,stms):
        self.stms = stms
    def accept(self, visitor):
        return visitor.visitBodyLchaveStmsRchave(self)

class BodyLchaveRchave(Program):
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
    def __init__(self,body,stm):
        self.body = body
        self.stm = stm
    def accept(self, visitor):
        return visitor.visitBodyOrStmBodyElseStm(self)

class BodyOrStmBodyElseBody(Program):
    def __init__(self,body,bodyy):
        self.body = body
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
    def __init__(self,exp):
        self.exp = exp
    def accept(self, visitor):
        return visitor.visitStmExpSemicolon(self)

class StmWhileLparenExpRparenBody(Program):
    def __init__(self,exp,body):
        self.exp = exp
        self.body = body
    def accept(self, visitor):
        return visitor.visitStmWhileLparenExpRparenBody(self)

class StmReturnExpSemicolon(Program):
    def __init__(self,exp):
        self.exp = exp
    def accept(self, visitor):
        return visitor.visitStmReturnExpSemicolon(self)

class StmIfLparenExpRparenBodyorstm(Program):
    def __init__(self,exp,bodyorstm):
        self.exp = exp
        self.bodyorstm = bodyorstm
    def accept(self, visitor):
        return visitor.visitStmIfLparenExpRparenBodyorstm(self)

class StmDeclvar(Program):
    def __init__(self,declvar):
        self.declvar = declvar
    def accept(self, visitor):
        return visitor.visitStmDeclvar(self)

class StmForLparenTipoIdInIdRparenBody(Program):
    def __init__(self,tipo,idd,iddd,body):
        self.tipo = tipo
        self.idd = idd
        self.iddd = iddd
        self.body = body
    def accept(self, visitor):
        return visitor.visitStmForLparenTipoIdInIdRparenBody(self)

class StmForFor(Program):
    #FOR LPAREN tiposassign INTERROGATION SEMI_COLON exp INTERROGATION SEMI_COLON exp INTERROGATION  RPAREN body
    def __init__(self,tiposassign,midfor1,midfor2,body):
        self.tiposassign = tiposassign
        self.midfor1 = midfor1
        self.midfor2 = midfor2
        self.body = body
    def accept(self, visitor):
        return visitor.visitStmForFor(self)

class ExpMoreExp(Program):
    def __init__(self,exp1,exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitExpMoreExp(self)

class ExpLessExp(Program):
    def __init__(self,exp1,exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitExpLessExp(self)

class ExpRestExp(Program):
    def __init__(self,exp1,exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitExpRestExp(self)

class ExpMultiplicationExp(Program):
    def __init__(self,exp1,exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitExpMultiplicationExp(self)

class ExpDivideExp(Program):
    def __init__(self,exp1,exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitExpDivideExp(self)

class ExpMoreEqualExp(Program):
    def __init__(self,exp1,exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitExpMoreEqualExp(self)

class ExpMoreThanExp(Program):
    def __init__(self,exp1,exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitExpMoreThanExp(self)

class ExpLessEqualExp(Program):
    def __init__(self,exp1,exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitExpLessEqualExp(self)

class ExpLessThanExp(Program):
    def __init__(self,exp1,exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitExpLessThanExp(self)

class ExpAsExp(Program):
    def __init__(self,exp1,exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitExpAsExp(self)

class ExpIsExp(Program):
    def __init__(self,exp1,exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitExpIsExp(self)

class ExpIsExclamationExp(Program):
    def __init__(self,exp1,exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitExpIsExclamationExp(self)

class ExpEqualExp(Program):
    def __init__(self,exp1,exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitExpEqualExp(self)

class ExpExclamationEqual(Program):
    def __init__(self,exp1,exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitExpExclamationEqual(self)

class ExpAndExp(Program):
    def __init__(self,exp1,exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitExpAndExp(self)

class ExpOrExp(Program):
    def __init__(self,exp1,exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitExpOrExp(self)

class ExpIfNullExp(Program):
    def __init__(self,exp1,exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitExpIfNullExp(self)

class ExpInterrogationExpColonExp(Program):
    def __init__(self,exp1,exp2,exp3):
        self.exp1 = exp1
        self.exp2 = exp2
        self.exp3 = exp3
    def accept(self, visitor):
        return visitor.visitExpInterrogationExpColonExp(self)

class ExpMultiplocationEqualExp(Program):
    def __init__(self,exp1,exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitExpMultiplocationEqualExp(self)

class ExpDivideEqualExp(Program):
    def __init__(self,exp1,exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitExpDivideEqualExp(self)

class ExpSomaEqualExp(Program):
    def __init__(self,exp1,exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitExpSomaEqualExp(self)

class ExpSubEqualExp(Program):
    def __init__(self,exp1,exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitExpSubEqualExp(self)

class ExpMoreMore(Program):
    def __init__(self,exp1):
        self.exp1 = exp1
    def accept(self, visitor):
        return visitor.visitExpMoreMore(self)

class ExpLessLess(Program):
    def __init__(self,exp1):
        self.exp1 = exp1
    def accept(self, visitor):
        return visitor.visitExpLessLess(self)

class ExpLparenExpRparen(Program):
    def __init__(self,exp1):
        self.exp1 = exp1
    def accept(self, visitor):
        return visitor.visitExpLparenExpRparen(self)

class ExpAwaitExp(Program):
    def __init__(self,exp1):
        self.exp1 = exp1
    def accept(self, visitor):
        return visitor.visitExpAwaitExp(self)

class ExpDotDotExp(Program):
    def __init__(self,exp1):
        self.exp1 = exp1
    def accept(self, visitor):
        return visitor.visitExpDotDotExp(self)

class ExpInterrogationDotDotExp(Program):
    def __init__(self,exp1):
        self.exp1 = exp1
    def accept(self, visitor):
        return visitor.visitExpInterrogationDotDotExp(self)

class ExpCall(Program):
    def __init__(self,exp1):
        self.exp1 = exp1
    def accept(self, visitor):
        return visitor.visitExpCall(self)

class ExpIdReceiveValueExp(Program):
    def __init__(self,exp1,exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitExpIdReceiveValueExp(self)

class ExpId(Program):
    def __init__(self,exp1):
        self.exp1 = exp1
    def accept(self, visitor):
        return visitor.visitExpId(self)

class ExpNumInt(Program):
    def __init__(self,exp1):
        self.exp1 = exp1
    def accept(self, visitor):
        return visitor.visitExpNumInt(self)

class ExpNumDouble(Program):
    def __init__(self,exp1):
        self.exp1 = exp1
    def accept(self, visitor):
        return visitor.visitExpNumDouble(self)

class ExpStrString(Program):
    def __init__(self,exp1):
        self.exp1 = exp1
    def accept(self, visitor):
        return visitor.visitExpStrString(self)

class ExpBoolean(Program):
    def __init__(self,exp1):
        self.exp1 = exp1
    def accept(self, visitor):
        return visitor.visitExpBoolean(self)

class ParamsExp(Program):
    def __init__(self,exp1):
        self.exp1 = exp1
    def accept(self, visitor):
        return visitor.visitParamsExp(self)

class ParamsExpVirgulaParams(Program):
    def __init__(self,exp1,exp3):
        self.exp1 = exp1
        self.exp3 = exp3
    def accept(self, visitor):
        return visitor.visitParamsExpVirgulaParams(self)

class AssignIdReceiveValueExp(Program):
    def __init__(self,exp1,exp3):
        self.exp1 = exp1
        self.exp3 = exp3
    def accept(self, visitor):
        return visitor.visitAssignIdReceiveValueExp(self)

class TipoDouble(Program):
    def accept(self, visitor):
        return visitor.visitTipoDouble(self)

class TipoInt(Program):
    def accept(self, visitor):
        return visitor.visitTipoInt(self)

class TipoString(Program):
    def accept(self, visitor):
        return visitor.visitTipoString(self)

class TipoBoolean(Program):
    def accept(self, visitor):
        return visitor.visitTipoBoolean(self)

class TipoVoid(Program):
    def accept(self, visitor):
        return visitor.visitTipoVoid(self)



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
