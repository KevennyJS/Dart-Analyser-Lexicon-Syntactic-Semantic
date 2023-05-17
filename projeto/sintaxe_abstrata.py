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

class DeclvarTipoInterrogationIdSemiColon(Declvar):
    def __init__(self, tipo,idd):
        self.tipo = tipo
        self.id = idd
    def accept(self, visitor):
        return visitor.visitDeclvarTipoInterrogationIdSemiColon(self)
        
class DeclvarTipoAssignSemicolon(Declvar):
    def __init__(self,tipo,assign):
        self.tipo = tipo
        self.assign = assign
    def accept(self, visitor):
        return visitor.visitDeclvarTipoAssignSemicolon(self)

class FuncdeclSignatureBody(Funcdecl):
    def __init__(self,signature,body):
        self.signature = signature
        self.body = body
    def accept(self, visitor):
        return visitor.visitFuncdeclSignatureBody(self)

class SignatureTipoIdLparenSigparamsRparen(Signature):
    def __init__(self,tipo,idd,sigparams):
        self.tipo = tipo
        self.idd = idd
        self.sigparams = sigparams
    def accept(self, visitor):
        return visitor.visitSignatureTipoIdLparenSigparamsRparen(self)

class SignatureTipoIdLparenRparen(Signature):
    def __init__(self,tipo,idd):
        self.tipo = tipo
        self.idd = idd
    def accept(self, visitor):
        return visitor.visitSignatureTipoIdLparenRparen(self)

class SigParamsTipoId(SigParams):
    def __init__(self,tipo,idd):
        self.tipo = tipo
        self.idd = idd
    def accept(self, visitor):
        return visitor.visitSigParamsTipoId(self)

class SigParamsTipoIdVirgulaSigparams(SigParams):
    def __init__(self,tipo,idd,sigparams):
        self.tipo = tipo
        self.idd = idd
        self.sigparams = sigparams
    def accept(self, visitor):
        return visitor.visitSigParamsTipoIdVirgulaSigparams(self)

class BodyLchaveStmsRchave(Body):
    def __init__(self,stms):
        self.stms = stms
    def accept(self, visitor):
        return visitor.visitBodyLchaveStmsRchave(self)

class BodyLchaveRchave(Body):
    def accept(self, visitor):
        return visitor.visitBodyLchaveRchave(self)

class BodyOrStmStm(Bodyorstm):
    def __init__(self,stm):
        self.stm = stm
    def accept(self, visitor):
        return visitor.visitBodyOrStmStm(self)

class BodyOrStmBody(Bodyorstm):
    def __init__(self,body):
        self.body = body
    def accept(self, visitor):
        return visitor.visitBodyOrStmBody(self)

class BodyOrStmBodyElseStm(Bodyorstm):
    def __init__(self,body,stm):
        self.body = body
        self.stm = stm
    def accept(self, visitor):
        return visitor.visitBodyOrStmBodyElseStm(self)

class BodyOrStmBodyElseBody(Bodyorstm):
    def __init__(self,body,bodyy):
        self.body = body
        self.body = bodyy
    def accept(self, visitor):
        return visitor.visitBodyOrStmBodyElseBody(self)

class StmsStm(Stms):
    def __init__(self,stm):
        self.stm = stm
    def accept(self, visitor):
        return visitor.visitStmsStm(self)

class StmsStmStms(Stms):
    def __init__(self,stm,stms):
        self.stm = stm
        self.stms = stms
    def accept(self, visitor):
        return visitor.visitStmsStmStms(self)

class StmExpSemicolon(Stm):
    def __init__(self,exp):
        self.exp = exp
    def accept(self, visitor):
        return visitor.visitStmExpSemicolon(self)

class StmWhileLparenExpRparenBody(Stm):
    def __init__(self,exp,body):
        self.exp = exp
        self.body = body
    def accept(self, visitor):
        return visitor.visitStmWhileLparenExpRparenBody(self)

class StmReturnExpSemicolon(Stm):
    def __init__(self,exp):
        self.exp = exp
    def accept(self, visitor):
        return visitor.visitStmReturnExpSemicolon(self)

class StmIfLparenExpRparenBodyorstm(Stm):
    def __init__(self,exp,bodyorstm):
        self.exp = exp
        self.bodyorstm = bodyorstm
    def accept(self, visitor):
        return visitor.visitStmIfLparenExpRparenBodyorstm(self)

class StmDeclvar(Stm):
    def __init__(self,declvar):
        self.declvar = declvar
    def accept(self, visitor):
        return visitor.visitStmDeclvar(self)

class StmForLparenTipoIdInIdRparenBody(Stm):
    def __init__(self,tipo,idd,iddd,body):
        self.tipo = tipo
        self.idd = idd
        self.iddd = iddd
        self.body = body
    def accept(self, visitor):
        return visitor.visitStmForLparenTipoIdInIdRparenBody(self)

class StmForFor(Stm):
    #FOR LPAREN tiposassign INTERROGATION SEMI_COLON exp INTERROGATION SEMI_COLON exp INTERROGATION  RPAREN body
    def __init__(self,tiposassign,midfor1,midfor2,body):
        self.tiposassign = tiposassign
        self.midfor1 = midfor1
        self.midfor2 = midfor2
        self.body = body
    def accept(self, visitor):
        return visitor.visitStmForFor(self)

class TipoassignsTipoAssign(Tiposassign):
    def __init__(self,tipo,assign):
        self.tipo = tipo
        self.assign = assign
    def accept(self, visitor):
        return visitor.visitTipoassignsTipoAssign(self)

class TipoassignsTipoAssingVirgula(Tiposassign):
    def __init__(self,tipo,assign,tipoAssign):
        self.tipo = tipo
        self.assign = assign
        self.tipoAssign = tipoAssign
    def accept(self, visitor):
        return visitor.visitTipoassignsTipoAssingVirgula(self)

class TipoassignsAssign(Tipoassigns):
    def __init__(self,assign):
        self.assign = assign
    def accept(self, visitor):
        return visitor.visitTipoassignsAssign(self)

class TipoAssagnsAssagnVirgula(Tipoassigns):
    def __init__(self,assign,tipoAssign):
        self.assign = assign
        self.tipoAssign = tipoAssign
    def accept(self, visitor):
        return visitor.visitTipoAssagnsAssagnVirgula(self)

class MidForExp(Midfor):
    def __init__(self,exp):
        self.exp = exp
    def accept(self, visitor):
        return visitor.visitMidForExp(self)

class CallParams(Call):
    def __init__(self,idd, params):
        self.idd = idd
        self.params = params
    def accept(self, visitor):
        return visitor.visitCallParams(self)

class CallNoParams(Call):
    def __init__(self,idd):
        self.idd = idd
    def accept(self, visitor):
        return visitor.visitCallNoParams(self)

class ExpMoreExp(Exp):
    def __init__(self,exp1,exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitExpMoreExp(self)

class ExpLessExp(Exp):
    def __init__(self,exp1,exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitExpLessExp(self)

class ExpRestExp(Exp):
    def __init__(self,exp1,exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitExpRestExp(self)

class ExpMultiplicationExp(Exp):
    def __init__(self,exp1,exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitExpMultiplicationExp(self)

class ExpDivideExp(Exp):
    def __init__(self,exp1,exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitExpDivideExp(self)

class ExpMoreEqualExp(Exp):
    def __init__(self,exp1,exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitExpMoreEqualExp(self)

class ExpMoreThanExp(Exp):
    def __init__(self,exp1,exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitExpMoreThanExp(self)

class ExpLessEqualExp(Exp):
    def __init__(self,exp1,exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitExpLessEqualExp(self)

class ExpLessThanExp(Exp):
    def __init__(self,exp1,exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitExpLessThanExp(self)

class ExpAsExp(Exp):
    def __init__(self,exp1,exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitExpAsExp(self)

class ExpIsExp(Exp):
    def __init__(self,exp1,exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitExpIsExp(self)

class ExpIsExclamationExp(Exp):
    def __init__(self,exp1,exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitExpIsExclamationExp(self)

class ExpEqualExp(Exp):
    def __init__(self,exp1,exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitExpEqualExp(self)

class ExpExclamationEqualExp(Exp):
    def __init__(self,exp1,exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitExpExclamationEqualExp(self)

class ExpAndExp(Exp):
    def __init__(self,exp1,exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitExpAndExp(self)

class ExpOrExp(Exp):
    def __init__(self,exp1,exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitExpOrExp(self)

class ExpIfNullExp(Exp):
    def __init__(self,exp1,exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitExpIfNullExp(self)

class ExpInterrogationExpColonExp(Exp):
    def __init__(self,exp1,exp2,exp3):
        self.exp1 = exp1
        self.exp2 = exp2
        self.exp3 = exp3
    def accept(self, visitor):
        return visitor.visitExpInterrogationExpColonExp(self)

class ExpMultiplocationEqualExp(Exp):
    def __init__(self,exp1,exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitExpMultiplocationEqualExp(self)

class ExpDivideEqualExp(Exp):
    def __init__(self,exp1,exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitExpDivideEqualExp(self)

class ExpSomaEqualExp(Exp):
    def __init__(self,exp1,exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitExpSomaEqualExp(self)

class ExpSubEqualExp(Exp):
    def __init__(self,exp1,exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitExpSubEqualExp(self)

class ExpMoreMore(Exp):
    def __init__(self,exp1):
        self.exp1 = exp1
    def accept(self, visitor):
        return visitor.visitExpMoreMore(self)

class ExpLessLess(Exp):
    def __init__(self,exp1):
        self.exp1 = exp1
    def accept(self, visitor):
        return visitor.visitExpLessLess(self)

class ExpLparenExpRparen(Exp):
    def __init__(self,exp1):
        self.exp1 = exp1
    def accept(self, visitor):
        return visitor.visitExpLparenExpRparen(self)

class ExpAwaitExp(Exp):
    def __init__(self,exp1):
        self.exp1 = exp1
    def accept(self, visitor):
        return visitor.visitExpAwaitExp(self)

class ExpDotDotExp(Exp):
    def __init__(self,exp1):
        self.exp1 = exp1
    def accept(self, visitor):
        return visitor.visitExpDotDotExp(self)

class ExpInterrogationDotDotExp(Exp):
    def __init__(self,exp1):
        self.exp1 = exp1
    def accept(self, visitor):
        return visitor.visitExpInterrogationDotDotExp(self)

class ExpCall(Exp):
    def __init__(self,call):
        self.call = call
    def accept(self, visitor):
        return visitor.visitExpCall(self)

class ExpIdReceiveValueExp(Exp):
    def __init__(self,idd,exp3):
        self.idd = idd
        self.exp3 = exp3
    def accept(self, visitor):
        return visitor.visitExpIdReceiveValueExp(self)

class ExpId(Exp):
    def __init__(self,idd):
        self.idd = idd
    def accept(self, visitor):
        return visitor.visitExpId(self)

class ExpNumInt(Exp):
    def __init__(self,exp1):
        self.exp1 = exp1
    def accept(self, visitor):
        return visitor.visitExpNumInt(self)

class ExpNumDouble(Exp):
    def __init__(self,exp1):
        self.exp1 = exp1
    def accept(self, visitor):
        return visitor.visitExpNumDouble(self)

class ExpStrString(Exp):
    def __init__(self,exp1):
        self.exp1 = exp1
    def accept(self, visitor):
        return visitor.visitExpStrString(self)

class ExpBoolean(Exp):
    def __init__(self,exp1):
        self.exp1 = exp1
    def accept(self, visitor):
        return visitor.visitExpBoolean(self)

class ParamsExp(Params):
    def __init__(self,exp):
        self.exp = exp
    def accept(self, visitor):
        return visitor.visitParamsExp(self)

class ParamsExpVirgulaParams(Params):
    def __init__(self,exp,params):
        self.exp = exp
        self.params = params
    def accept(self, visitor):
        return visitor.visitParamsExpVirgulaParams(self)

class AssignIdReceiveValueExp(Assign):
    def __init__(self,idd,exp):
        self.idd = idd
        self.exp = exp
    def accept(self, visitor):
        return visitor.visitAssignIdReceiveValueExp(self)

class TipoDouble(Tipo):
    def accept(self, visitor):
        return visitor.visitTipoDouble(self)

class TipoInt(Tipo):
    def accept(self, visitor):
        return visitor.visitTipoInt(self)

class TipoString(Tipo):
    def accept(self, visitor):
        return visitor.visitTipoString(self)

class TipoBoolean(Tipo):
    def accept(self, visitor):
        return visitor.visitTipoBoolean(self)

class TipoVoid(Tipo):
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
