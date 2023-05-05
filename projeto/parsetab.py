
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightRECEIVE_VALUEMULTIPLICATION_EQUALDIVIDE_EQUALSOMA_EQUALSUB_EQUALleftDOT_DOTrightINTERROGATIONCOLONleftORANDIF_NULLnonassocEQUALEXCLAMATION_EQUALnonassocMORE_EQUALMORETHANLESS_EQUALLESSTHANASISIS_EXCLAMATIONleftCOMMERCIAL_EleftMORELESSleftMULTIPLICATIONDIVIDERESTnonassocMORE_MORELESS_LESSEXCLAMATIONAWAITABSTRACT ALL AND AS ASSERTS ASYNC AT_SIGN AWAIT BOO_BOOLEAN BREAK CASE CATCH CLASS COLON COMMENT COMMERCIAL_E CONST CONTINUE COVARIANT DEFAULT DEFERRED DIVIDE DIVIDE_EQUAL DO DOT DOT_DOT DYNAMIC ELSE ENUM EQUAL EXCLAMATION EXCLAMATION_EQUAL EXPORT EXTENDS EXTENSION EXTERNAL FACTORY FALSE FINAL FINALLY FOR FUNCTION GET HIDE ID IF IF_NULL IMPLEMENTS IMPORTS IN INTERFACE INTERROGATION IS IS_EXCLAMATION LATE LBRACKET LCHAV LESS LESSTHAN LESS_EQUAL LESS_LESS LIBRARY LPAREN MIXIN MORE MORETHAN MORE_EQUAL MORE_MORE MULTIPLICATION MULTIPLICATION_EQUAL NEW NULL NUM_DOUBLE NUM_INT ON OPERATOR OR PART RBRACKET RCHAV RECEIVE_VALUE REQUIRED REST RETHROW RETURN RPAREN SEMI_COLON SET SHOW SOMA_EQUAL SPACE STATIC STR_STRING SUB_EQUAL SUPER SWITCH SYNC THIS THROW TIPO_BOOLEAN TIPO_DOUBLE TIPO_INT TIPO_STRING TIPO_VOID TRUE TRY TYPEDEF VAR VIRGULA WHILE WITH YIELDprogram : funcdecl\n                | funcdecl program\n                | declvar\n                | declvar program\n    declvar : tipo assign SEMI_COLON\n               | tipo INTERROGATION ID SEMI_COLON\n    funcdecl : signature bodysignature : tipo ID LPAREN sigParams RPAREN \n    | tipo ID LPAREN RPAREN sigParams : tipo ID \n                | tipo ID VIRGULA sigParams\n    body : LCHAV stms RCHAV \n            | LCHAV RCHAV \n    bodyorstm : stm \n                | body\n                | body ELSE stm\n                | body ELSE body\n    stms : stm  \n            | stm  stms\n    stm : exp SEMI_COLON \n        | WHILE LPAREN exp RPAREN body\n        | RETURN exp SEMI_COLON \n        | IF LPAREN exp RPAREN bodyorstm\n        | FOR LPAREN tiposassign INTERROGATION SEMI_COLON exp INTERROGATION SEMI_COLON exp INTERROGATION  RPAREN body\n        | FOR LPAREN tipo ID IN ID RPAREN body\n        | declvar\n    tiposassign : tipo  assign \n                | tipo tipoassigns\n    tipoassigns : assign \n                | assign VIRGULA tipoassigns\n    call : ID LPAREN params RPAREN \n            | ID LPAREN RPAREN \n    exp : exp MORE exp\n           | exp LESS exp\n           | exp MULTIPLICATION exp \n           | exp DIVIDE exp \n           | exp REST exp\n           | exp MORE_EQUAL exp\n           | exp MORETHAN exp \n           | exp LESS_EQUAL exp\n           | exp LESSTHAN exp \n           | exp AS exp\n           | exp IS exp\n           | exp IS_EXCLAMATION exp\n           | exp EQUAL exp\n           | exp EXCLAMATION_EQUAL exp\n           | exp AND exp\n           | exp OR exp\n           | exp IF_NULL exp\n           | exp INTERROGATION exp COLON exp\n           | exp MULTIPLICATION_EQUAL exp\n           | exp DIVIDE_EQUAL exp\n           | exp SOMA_EQUAL exp\n           | exp SUB_EQUAL exp\n           | exp MORE_MORE \n           | exp LESS_LESS\n           | LPAREN exp RPAREN\n           | AWAIT exp\n           | DOT_DOT exp \n           | INTERROGATION DOT_DOT exp\n           | call  \n           | ID RECEIVE_VALUE exp\n           | ID\n           | NUM_INT\n           | NUM_DOUBLE\n           | STR_STRING\n           | BOO_BOOLEAN\n    params : exp VIRGULA params \n            | exp\n    assign : ID RECEIVE_VALUE exptipo : TIPO_DOUBLE \n    | TIPO_INT\n    | TIPO_STRING \n    | TIPO_BOOLEAN\n    | TIPO_VOID'
    
_lr_action_items = {'TIPO_DOUBLE':([0,2,3,13,14,19,20,30,38,40,42,44,73,80,109,122,129,131,132,133,134,140,145,146,150,154,],[6,6,6,-7,6,-13,6,-26,-5,6,-12,-20,6,-6,-22,6,6,-21,-23,-14,-15,6,-17,-16,-25,-24,]),'TIPO_INT':([0,2,3,13,14,19,20,30,38,40,42,44,73,80,109,122,129,131,132,133,134,140,145,146,150,154,],[7,7,7,-7,7,-13,7,-26,-5,7,-12,-20,7,-6,-22,7,7,-21,-23,-14,-15,7,-17,-16,-25,-24,]),'TIPO_STRING':([0,2,3,13,14,19,20,30,38,40,42,44,73,80,109,122,129,131,132,133,134,140,145,146,150,154,],[8,8,8,-7,8,-13,8,-26,-5,8,-12,-20,8,-6,-22,8,8,-21,-23,-14,-15,8,-17,-16,-25,-24,]),'TIPO_BOOLEAN':([0,2,3,13,14,19,20,30,38,40,42,44,73,80,109,122,129,131,132,133,134,140,145,146,150,154,],[9,9,9,-7,9,-13,9,-26,-5,9,-12,-20,9,-6,-22,9,9,-21,-23,-14,-15,9,-17,-16,-25,-24,]),'TIPO_VOID':([0,2,3,13,14,19,20,30,38,40,42,44,73,80,109,122,129,131,132,133,134,140,145,146,150,154,],[10,10,10,-7,10,-13,10,-26,-5,10,-12,-20,10,-6,-22,10,10,-21,-23,-14,-15,10,-17,-16,-25,-24,]),'$end':([1,2,3,11,12,13,19,38,42,80,],[0,-1,-3,-2,-4,-7,-13,-5,-12,-6,]),'LCHAV':([4,83,119,121,122,140,148,153,],[14,-9,-8,14,14,14,14,14,]),'INTERROGATION':([5,6,7,8,9,10,14,19,20,21,23,24,28,29,30,31,32,33,34,35,36,37,38,41,42,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,74,76,77,78,79,80,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,113,114,116,117,120,122,125,126,127,128,130,131,132,133,134,135,140,141,143,144,145,146,147,149,150,151,152,154,],[16,-71,-72,-73,-74,-75,27,-13,27,62,27,27,16,-63,-26,27,27,-61,-64,-65,-66,-67,-5,27,-12,-20,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,-55,-56,27,62,62,27,27,27,27,-58,62,-6,62,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,62,62,62,62,62,62,-57,-22,62,123,62,62,-32,62,27,27,-27,-28,-31,27,62,-21,-23,-14,-15,27,27,147,-29,-30,-17,-16,27,27,-25,152,27,-24,]),'ID':([5,6,7,8,9,10,14,16,19,20,23,24,28,30,31,32,38,41,42,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,69,72,74,76,77,80,81,109,112,120,122,128,131,132,133,134,135,136,137,140,145,146,147,149,150,152,154,],[17,-71,-72,-73,-74,-75,29,39,-13,29,29,29,75,-26,29,29,-5,29,-12,-20,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,-6,118,-22,124,29,29,29,-21,-23,-14,-15,29,142,75,29,-17,-16,29,29,-25,29,-24,]),'RCHAV':([14,18,19,20,30,38,42,43,44,80,109,131,132,133,134,145,146,150,154,],[19,42,-13,-18,-26,-5,-12,-19,-20,-6,-22,-21,-23,-14,-15,-17,-16,-25,-24,]),'WHILE':([14,19,20,30,38,42,44,80,109,122,131,132,133,134,140,145,146,150,154,],[22,-13,22,-26,-5,-12,-20,-6,-22,22,-21,-23,-14,-15,22,-17,-16,-25,-24,]),'RETURN':([14,19,20,30,38,42,44,80,109,122,131,132,133,134,140,145,146,150,154,],[24,-13,24,-26,-5,-12,-20,-6,-22,24,-21,-23,-14,-15,24,-17,-16,-25,-24,]),'IF':([14,19,20,30,38,42,44,80,109,122,131,132,133,134,140,145,146,150,154,],[25,-13,25,-26,-5,-12,-20,-6,-22,25,-21,-23,-14,-15,25,-17,-16,-25,-24,]),'FOR':([14,19,20,30,38,42,44,80,109,122,131,132,133,134,140,145,146,150,154,],[26,-13,26,-26,-5,-12,-20,-6,-22,26,-21,-23,-14,-15,26,-17,-16,-25,-24,]),'LPAREN':([14,17,19,20,22,23,24,25,26,29,30,31,32,38,41,42,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,69,72,74,76,77,80,109,120,122,128,131,132,133,134,135,140,145,146,147,149,150,152,154,],[23,40,-13,23,69,23,23,72,73,77,-26,23,23,-5,23,-12,-20,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,-6,-22,23,23,23,-21,-23,-14,-15,23,23,-17,-16,23,23,-25,23,-24,]),'AWAIT':([14,19,20,23,24,30,31,32,38,41,42,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,69,72,74,76,77,80,109,120,122,128,131,132,133,134,135,140,145,146,147,149,150,152,154,],[31,-13,31,31,31,-26,31,31,-5,31,-12,-20,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,-6,-22,31,31,31,-21,-23,-14,-15,31,31,-17,-16,31,31,-25,31,-24,]),'DOT_DOT':([14,19,20,23,24,27,30,31,32,38,41,42,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,69,72,74,76,77,80,109,120,122,128,131,132,133,134,135,140,145,146,147,149,150,152,154,],[32,-13,32,32,32,74,-26,32,32,-5,32,-12,-20,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,-6,-22,32,32,32,-21,-23,-14,-15,32,32,-17,-16,32,32,-25,32,-24,]),'NUM_INT':([14,19,20,23,24,30,31,32,38,41,42,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,69,72,74,76,77,80,109,120,122,128,131,132,133,134,135,140,145,146,147,149,150,152,154,],[34,-13,34,34,34,-26,34,34,-5,34,-12,-20,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,-6,-22,34,34,34,-21,-23,-14,-15,34,34,-17,-16,34,34,-25,34,-24,]),'NUM_DOUBLE':([14,19,20,23,24,30,31,32,38,41,42,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,69,72,74,76,77,80,109,120,122,128,131,132,133,134,135,140,145,146,147,149,150,152,154,],[35,-13,35,35,35,-26,35,35,-5,35,-12,-20,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,-6,-22,35,35,35,-21,-23,-14,-15,35,35,-17,-16,35,35,-25,35,-24,]),'STR_STRING':([14,19,20,23,24,30,31,32,38,41,42,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,69,72,74,76,77,80,109,120,122,128,131,132,133,134,135,140,145,146,147,149,150,152,154,],[36,-13,36,36,36,-26,36,36,-5,36,-12,-20,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,-6,-22,36,36,36,-21,-23,-14,-15,36,36,-17,-16,36,36,-25,36,-24,]),'BOO_BOOLEAN':([14,19,20,23,24,30,31,32,38,41,42,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,69,72,74,76,77,80,109,120,122,128,131,132,133,134,135,140,145,146,147,149,150,152,154,],[37,-13,37,37,37,-26,37,37,-5,37,-12,-20,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,-6,-22,37,37,37,-21,-23,-14,-15,37,37,-17,-16,37,37,-25,37,-24,]),'SEMI_COLON':([15,21,29,33,34,35,36,37,39,67,68,71,78,79,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,103,104,105,106,108,113,114,116,123,127,130,147,],[38,44,-63,-61,-64,-65,-66,-67,80,-55,-56,109,-58,-59,-70,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-51,-52,-53,-54,-57,-60,-62,-32,135,-31,-50,149,]),'RECEIVE_VALUE':([17,29,75,124,],[41,76,41,41,]),'ELSE':([19,42,134,],[-13,-12,140,]),'MORE':([21,29,33,34,35,36,37,67,68,70,71,78,79,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,110,113,114,116,117,127,130,141,151,],[45,-63,-61,-64,-65,-66,-67,-55,-56,45,45,-58,45,45,-33,-34,-35,-36,-37,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,-57,45,45,45,-32,45,-31,45,45,45,]),'LESS':([21,29,33,34,35,36,37,67,68,70,71,78,79,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,110,113,114,116,117,127,130,141,151,],[46,-63,-61,-64,-65,-66,-67,-55,-56,46,46,-58,46,46,-33,-34,-35,-36,-37,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,-57,46,46,46,-32,46,-31,46,46,46,]),'MULTIPLICATION':([21,29,33,34,35,36,37,67,68,70,71,78,79,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,110,113,114,116,117,127,130,141,151,],[47,-63,-61,-64,-65,-66,-67,-55,-56,47,47,-58,47,47,47,47,-35,-36,-37,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,-57,47,47,47,-32,47,-31,47,47,47,]),'DIVIDE':([21,29,33,34,35,36,37,67,68,70,71,78,79,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,110,113,114,116,117,127,130,141,151,],[48,-63,-61,-64,-65,-66,-67,-55,-56,48,48,-58,48,48,48,48,-35,-36,-37,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,-57,48,48,48,-32,48,-31,48,48,48,]),'REST':([21,29,33,34,35,36,37,67,68,70,71,78,79,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,110,113,114,116,117,127,130,141,151,],[49,-63,-61,-64,-65,-66,-67,-55,-56,49,49,-58,49,49,49,49,-35,-36,-37,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,-57,49,49,49,-32,49,-31,49,49,49,]),'MORE_EQUAL':([21,29,33,34,35,36,37,67,68,70,71,78,79,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,110,113,114,116,117,127,130,141,151,],[50,-63,-61,-64,-65,-66,-67,-55,-56,50,50,-58,50,50,-33,-34,-35,-36,-37,None,None,None,None,None,None,None,50,50,50,50,50,50,50,50,50,50,50,-57,50,50,50,-32,50,-31,50,50,50,]),'MORETHAN':([21,29,33,34,35,36,37,67,68,70,71,78,79,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,110,113,114,116,117,127,130,141,151,],[51,-63,-61,-64,-65,-66,-67,-55,-56,51,51,-58,51,51,-33,-34,-35,-36,-37,None,None,None,None,None,None,None,51,51,51,51,51,51,51,51,51,51,51,-57,51,51,51,-32,51,-31,51,51,51,]),'LESS_EQUAL':([21,29,33,34,35,36,37,67,68,70,71,78,79,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,110,113,114,116,117,127,130,141,151,],[52,-63,-61,-64,-65,-66,-67,-55,-56,52,52,-58,52,52,-33,-34,-35,-36,-37,None,None,None,None,None,None,None,52,52,52,52,52,52,52,52,52,52,52,-57,52,52,52,-32,52,-31,52,52,52,]),'LESSTHAN':([21,29,33,34,35,36,37,67,68,70,71,78,79,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,110,113,114,116,117,127,130,141,151,],[53,-63,-61,-64,-65,-66,-67,-55,-56,53,53,-58,53,53,-33,-34,-35,-36,-37,None,None,None,None,None,None,None,53,53,53,53,53,53,53,53,53,53,53,-57,53,53,53,-32,53,-31,53,53,53,]),'AS':([21,29,33,34,35,36,37,67,68,70,71,78,79,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,110,113,114,116,117,127,130,141,151,],[54,-63,-61,-64,-65,-66,-67,-55,-56,54,54,-58,54,54,-33,-34,-35,-36,-37,None,None,None,None,None,None,None,54,54,54,54,54,54,54,54,54,54,54,-57,54,54,54,-32,54,-31,54,54,54,]),'IS':([21,29,33,34,35,36,37,67,68,70,71,78,79,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,110,113,114,116,117,127,130,141,151,],[55,-63,-61,-64,-65,-66,-67,-55,-56,55,55,-58,55,55,-33,-34,-35,-36,-37,None,None,None,None,None,None,None,55,55,55,55,55,55,55,55,55,55,55,-57,55,55,55,-32,55,-31,55,55,55,]),'IS_EXCLAMATION':([21,29,33,34,35,36,37,67,68,70,71,78,79,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,110,113,114,116,117,127,130,141,151,],[56,-63,-61,-64,-65,-66,-67,-55,-56,56,56,-58,56,56,-33,-34,-35,-36,-37,None,None,None,None,None,None,None,56,56,56,56,56,56,56,56,56,56,56,-57,56,56,56,-32,56,-31,56,56,56,]),'EQUAL':([21,29,33,34,35,36,37,67,68,70,71,78,79,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,110,113,114,116,117,127,130,141,151,],[57,-63,-61,-64,-65,-66,-67,-55,-56,57,57,-58,57,57,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,None,None,57,57,57,57,57,57,57,57,57,-57,57,57,57,-32,57,-31,57,57,57,]),'EXCLAMATION_EQUAL':([21,29,33,34,35,36,37,67,68,70,71,78,79,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,110,113,114,116,117,127,130,141,151,],[58,-63,-61,-64,-65,-66,-67,-55,-56,58,58,-58,58,58,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,None,None,58,58,58,58,58,58,58,58,58,-57,58,58,58,-32,58,-31,58,58,58,]),'AND':([21,29,33,34,35,36,37,67,68,70,71,78,79,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,110,113,114,116,117,127,130,141,151,],[59,-63,-61,-64,-65,-66,-67,-55,-56,59,59,-58,59,59,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,59,59,59,59,59,59,-57,59,59,59,-32,59,-31,59,59,59,]),'OR':([21,29,33,34,35,36,37,67,68,70,71,78,79,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,110,113,114,116,117,127,130,141,151,],[60,-63,-61,-64,-65,-66,-67,-55,-56,60,60,-58,60,60,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,60,60,60,60,60,60,-57,60,60,60,-32,60,-31,60,60,60,]),'IF_NULL':([21,29,33,34,35,36,37,67,68,70,71,78,79,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,110,113,114,116,117,127,130,141,151,],[61,-63,-61,-64,-65,-66,-67,-55,-56,61,61,-58,61,61,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,61,61,61,61,61,61,-57,61,61,61,-32,61,-31,61,61,61,]),'MULTIPLICATION_EQUAL':([21,29,33,34,35,36,37,67,68,70,71,78,79,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,110,113,114,116,117,127,130,141,151,],[63,-63,-61,-64,-65,-66,-67,-55,-56,63,63,-58,-59,63,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,63,63,63,63,63,63,-57,63,-60,63,-32,63,-31,-50,63,63,]),'DIVIDE_EQUAL':([21,29,33,34,35,36,37,67,68,70,71,78,79,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,110,113,114,116,117,127,130,141,151,],[64,-63,-61,-64,-65,-66,-67,-55,-56,64,64,-58,-59,64,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,64,64,64,64,64,64,-57,64,-60,64,-32,64,-31,-50,64,64,]),'SOMA_EQUAL':([21,29,33,34,35,36,37,67,68,70,71,78,79,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,110,113,114,116,117,127,130,141,151,],[65,-63,-61,-64,-65,-66,-67,-55,-56,65,65,-58,-59,65,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,65,65,65,65,65,65,-57,65,-60,65,-32,65,-31,-50,65,65,]),'SUB_EQUAL':([21,29,33,34,35,36,37,67,68,70,71,78,79,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,110,113,114,116,117,127,130,141,151,],[66,-63,-61,-64,-65,-66,-67,-55,-56,66,66,-58,-59,66,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,66,66,66,66,66,66,-57,66,-60,66,-32,66,-31,-50,66,66,]),'MORE_MORE':([21,29,33,34,35,36,37,67,68,70,71,78,79,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,110,113,114,116,117,127,130,141,151,],[67,-63,-61,-64,-65,-66,-67,-55,-56,67,67,None,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,-57,67,67,67,-32,67,-31,67,67,67,]),'LESS_LESS':([21,29,33,34,35,36,37,67,68,70,71,78,79,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,110,113,114,116,117,127,130,141,151,],[68,-63,-61,-64,-65,-66,-67,-55,-56,68,68,None,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,-57,68,68,68,-32,68,-31,68,68,68,]),'RPAREN':([29,33,34,35,36,37,40,67,68,70,77,78,79,82,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,103,104,105,106,107,108,110,113,114,115,116,117,118,127,130,138,139,142,152,],[-63,-61,-64,-65,-66,-67,83,-55,-56,108,116,-58,-59,119,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-51,-52,-53,-54,121,-57,122,-60,-62,127,-32,-69,-10,-31,-50,-68,-11,148,153,]),'VIRGULA':([29,33,34,35,36,37,67,68,78,79,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,103,104,105,106,108,113,114,116,117,118,125,127,130,143,],[-63,-61,-64,-65,-66,-67,-55,-56,-58,-59,-70,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-51,-52,-53,-54,-57,-60,-62,-32,128,129,137,-31,-50,137,]),'COLON':([29,33,34,35,36,37,67,68,78,79,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,108,113,114,116,127,130,],[-63,-61,-64,-65,-66,-67,-55,-56,-58,-59,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,120,-51,-52,-53,-54,-57,-60,-62,-32,-31,-50,]),'IN':([124,],[136,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,2,3,],[1,11,12,]),'funcdecl':([0,2,3,],[2,2,2,]),'declvar':([0,2,3,14,20,122,140,],[3,3,3,30,30,30,30,]),'signature':([0,2,3,],[4,4,4,]),'tipo':([0,2,3,14,20,40,73,122,129,140,],[5,5,5,28,28,81,112,28,81,28,]),'body':([4,121,122,140,148,153,],[13,131,134,145,150,154,]),'assign':([5,28,112,137,],[15,15,125,143,]),'stms':([14,20,],[18,43,]),'stm':([14,20,122,140,],[20,20,133,146,]),'exp':([14,20,23,24,31,32,41,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,69,72,74,76,77,120,122,128,135,140,147,149,152,],[21,21,70,71,78,79,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,110,113,114,117,130,21,117,141,21,102,151,102,]),'call':([14,20,23,24,31,32,41,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,69,72,74,76,77,120,122,128,135,140,147,149,152,],[33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'sigParams':([40,129,],[82,139,]),'tiposassign':([73,],[111,]),'params':([77,128,],[115,138,]),'tipoassigns':([112,137,],[126,144,]),'bodyorstm':([122,],[132,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> funcdecl','program',1,'p_program','expression_parser.py',18),
  ('program -> funcdecl program','program',2,'p_program','expression_parser.py',19),
  ('program -> declvar','program',1,'p_program','expression_parser.py',20),
  ('program -> declvar program','program',2,'p_program','expression_parser.py',21),
  ('declvar -> tipo assign SEMI_COLON','declvar',3,'p_declvar','expression_parser.py',37),
  ('declvar -> tipo INTERROGATION ID SEMI_COLON','declvar',4,'p_declvar','expression_parser.py',38),
  ('funcdecl -> signature body','funcdecl',2,'p_funcdecl','expression_parser.py',47),
  ('signature -> tipo ID LPAREN sigParams RPAREN','signature',5,'p_signature','expression_parser.py',52),
  ('signature -> tipo ID LPAREN RPAREN','signature',4,'p_signature','expression_parser.py',53),
  ('sigParams -> tipo ID','sigParams',2,'p_sigParams','expression_parser.py',61),
  ('sigParams -> tipo ID VIRGULA sigParams','sigParams',4,'p_sigParams','expression_parser.py',62),
  ('body -> LCHAV stms RCHAV','body',3,'p_body','expression_parser.py',71),
  ('body -> LCHAV RCHAV','body',2,'p_body','expression_parser.py',72),
  ('bodyorstm -> stm','bodyorstm',1,'p_bodyorstm','expression_parser.py',83),
  ('bodyorstm -> body','bodyorstm',1,'p_bodyorstm','expression_parser.py',84),
  ('bodyorstm -> body ELSE stm','bodyorstm',3,'p_bodyorstm','expression_parser.py',85),
  ('bodyorstm -> body ELSE body','bodyorstm',3,'p_bodyorstm','expression_parser.py',86),
  ('stms -> stm','stms',1,'p_stms','expression_parser.py',100),
  ('stms -> stm stms','stms',2,'p_stms','expression_parser.py',101),
  ('stm -> exp SEMI_COLON','stm',2,'p_stm','expression_parser.py',110),
  ('stm -> WHILE LPAREN exp RPAREN body','stm',5,'p_stm','expression_parser.py',111),
  ('stm -> RETURN exp SEMI_COLON','stm',3,'p_stm','expression_parser.py',112),
  ('stm -> IF LPAREN exp RPAREN bodyorstm','stm',5,'p_stm','expression_parser.py',113),
  ('stm -> FOR LPAREN tiposassign INTERROGATION SEMI_COLON exp INTERROGATION SEMI_COLON exp INTERROGATION RPAREN body','stm',12,'p_stm','expression_parser.py',114),
  ('stm -> FOR LPAREN tipo ID IN ID RPAREN body','stm',8,'p_stm','expression_parser.py',115),
  ('stm -> declvar','stm',1,'p_stm','expression_parser.py',116),
  ('tiposassign -> tipo assign','tiposassign',2,'p_tiposassign','expression_parser.py',138),
  ('tiposassign -> tipo tipoassigns','tiposassign',2,'p_tiposassign','expression_parser.py',139),
  ('tipoassigns -> assign','tipoassigns',1,'p_tipoassigns','expression_parser.py',144),
  ('tipoassigns -> assign VIRGULA tipoassigns','tipoassigns',3,'p_tipoassigns','expression_parser.py',145),
  ('call -> ID LPAREN params RPAREN','call',4,'p_call','expression_parser.py',150),
  ('call -> ID LPAREN RPAREN','call',3,'p_call','expression_parser.py',151),
  ('exp -> exp MORE exp','exp',3,'p_exp','expression_parser.py',166),
  ('exp -> exp LESS exp','exp',3,'p_exp','expression_parser.py',167),
  ('exp -> exp MULTIPLICATION exp','exp',3,'p_exp','expression_parser.py',168),
  ('exp -> exp DIVIDE exp','exp',3,'p_exp','expression_parser.py',169),
  ('exp -> exp REST exp','exp',3,'p_exp','expression_parser.py',170),
  ('exp -> exp MORE_EQUAL exp','exp',3,'p_exp','expression_parser.py',171),
  ('exp -> exp MORETHAN exp','exp',3,'p_exp','expression_parser.py',172),
  ('exp -> exp LESS_EQUAL exp','exp',3,'p_exp','expression_parser.py',173),
  ('exp -> exp LESSTHAN exp','exp',3,'p_exp','expression_parser.py',174),
  ('exp -> exp AS exp','exp',3,'p_exp','expression_parser.py',175),
  ('exp -> exp IS exp','exp',3,'p_exp','expression_parser.py',176),
  ('exp -> exp IS_EXCLAMATION exp','exp',3,'p_exp','expression_parser.py',177),
  ('exp -> exp EQUAL exp','exp',3,'p_exp','expression_parser.py',178),
  ('exp -> exp EXCLAMATION_EQUAL exp','exp',3,'p_exp','expression_parser.py',179),
  ('exp -> exp AND exp','exp',3,'p_exp','expression_parser.py',180),
  ('exp -> exp OR exp','exp',3,'p_exp','expression_parser.py',181),
  ('exp -> exp IF_NULL exp','exp',3,'p_exp','expression_parser.py',182),
  ('exp -> exp INTERROGATION exp COLON exp','exp',5,'p_exp','expression_parser.py',183),
  ('exp -> exp MULTIPLICATION_EQUAL exp','exp',3,'p_exp','expression_parser.py',184),
  ('exp -> exp DIVIDE_EQUAL exp','exp',3,'p_exp','expression_parser.py',185),
  ('exp -> exp SOMA_EQUAL exp','exp',3,'p_exp','expression_parser.py',186),
  ('exp -> exp SUB_EQUAL exp','exp',3,'p_exp','expression_parser.py',187),
  ('exp -> exp MORE_MORE','exp',2,'p_exp','expression_parser.py',188),
  ('exp -> exp LESS_LESS','exp',2,'p_exp','expression_parser.py',189),
  ('exp -> LPAREN exp RPAREN','exp',3,'p_exp','expression_parser.py',190),
  ('exp -> AWAIT exp','exp',2,'p_exp','expression_parser.py',191),
  ('exp -> DOT_DOT exp','exp',2,'p_exp','expression_parser.py',192),
  ('exp -> INTERROGATION DOT_DOT exp','exp',3,'p_exp','expression_parser.py',193),
  ('exp -> call','exp',1,'p_exp','expression_parser.py',194),
  ('exp -> ID RECEIVE_VALUE exp','exp',3,'p_exp','expression_parser.py',195),
  ('exp -> ID','exp',1,'p_exp','expression_parser.py',196),
  ('exp -> NUM_INT','exp',1,'p_exp','expression_parser.py',197),
  ('exp -> NUM_DOUBLE','exp',1,'p_exp','expression_parser.py',198),
  ('exp -> STR_STRING','exp',1,'p_exp','expression_parser.py',199),
  ('exp -> BOO_BOOLEAN','exp',1,'p_exp','expression_parser.py',200),
  ('params -> exp VIRGULA params','params',3,'p_params','expression_parser.py',207),
  ('params -> exp','params',1,'p_params','expression_parser.py',208),
  ('assign -> ID RECEIVE_VALUE exp','assign',3,'p_assign','expression_parser.py',213),
  ('tipo -> TIPO_DOUBLE','tipo',1,'p_tipo','expression_parser.py',217),
  ('tipo -> TIPO_INT','tipo',1,'p_tipo','expression_parser.py',218),
  ('tipo -> TIPO_STRING','tipo',1,'p_tipo','expression_parser.py',219),
  ('tipo -> TIPO_BOOLEAN','tipo',1,'p_tipo','expression_parser.py',220),
  ('tipo -> TIPO_VOID','tipo',1,'p_tipo','expression_parser.py',221),
]
