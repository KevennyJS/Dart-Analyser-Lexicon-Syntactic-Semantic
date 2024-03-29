import ply.lex as lex
from testes import *

reservadas = {
    'abstract':'ABSTRACT',
    'as':'AS',
    'asserts':'ASSERTS',
    'async':'ASYNC',
    'await':'AWAIT',
    'break':'BREAK',
    'case':'CASE',
    'catch':'CATCH',
    'class':'CLASS',
    'const':'CONST',
    'continue':'CONTINUE',
    'covariant':'COVARIANT',
    'default':'DEFAULT',
    'deferred':'DEFERRED',
    'do':'DO',
    'dynamic':'DYNAMIC',
    'else':'ELSE',
    'enum':'ENUM',
    'export':'EXPORT',
    'extends':'EXTENDS',
    'extension':'EXTENSION',
    'external':'EXTERNAL',
    'factory':'FACTORY',
    'false':'FALSE',
    'final':'FINAL',
    'finally':'FINALLY',
    'for':'FOR',
    'function':'FUNCTION',
    'get':'GET',
    'hide':'HIDE',
    'if':'IF',
    'implements':'IMPLEMENTS',
    'imports':'IMPORTS',
    'in':'IN',
    'interface':'INTERFACE',
    'is':'IS',
    'late':'LATE',
    'library':'LIBRARY',
    'mixin':'MIXIN',
    'new':'NEW',
    'null':'NULL',
    'on':'ON',
    'operator':'OPERATOR',
    'part':'PART',
    'required':'REQUIRED',
    'rethrow':'RETHROW',
    'return':'RETURN',
    'set':'SET',
    'show':'SHOW',
    'static':'STATIC',
    'super':'SUPER',
    'switch':'SWITCH',
    'sync':'SYNC',
    'this':'THIS',
    'throw':'THROW',
    'true':'TRUE',
    'try':'TRY',
    'typedef':'TYPEDEF',
    'var':'VAR',
    'while':'WHILE',
    'with':'WITH',
    'yield':'YIELD',
    'void':'TIPO_VOID',
    'double' : 'TIPO_DOUBLE',
    'int' : 'TIPO_INT',
    'String' : "TIPO_STRING",
    'boolean' : 'TIPO_BOOLEAN',

}

tokens = ['ID', 'LPAREN', 'RPAREN', 'EQUAL', 'LCHAV', 'RCHAV','SPACE', 'RECEIVE_VALUE',
           'SEMI_COLON','NUM_DOUBLE', 'NUM_INT', 'VIRGULA', 'DOT','ALL','MORETHAN', 'LESSTHAN'
           ,"STR_STRING",'MORE',"LESS","MULTIPLICATION","DIVIDE","REST","EXCLAMATION",
           "COMMENT","INTERROGATION","COLON","OR","AND","IF_NULL","AT_SIGN","LBRACKET","RBRACKET"
           ,"BOO_BOOLEAN","COMMERCIAL_E","MORE_EQUAL","LESS_EQUAL","EXCLAMATION_EQUAL","MULTIPLICATION_EQUAL",
           "DIVIDE_EQUAL","SOMA_EQUAL","SUB_EQUAL","MORE_MORE","LESS_LESS","DOT_DOT","IS_EXCLAMATION",
           ] + list(reservadas.values())


teste = vere_codes

t_ignore  = ' \t\n'


def t_error(t):
    print("Caractere ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

# t_TIPO_DOUBLE = 'double'
# t_TIPO_STRING = 'String'
# t_TIPO_INT = 'int'
# t_TIPO_BOOLEAN = 'boolean'
# t_TIPO_VOID = 'void'

t_IS_EXCLAMATION = "IS!"
t_DOT_DOT = "\.\."
t_LESS_LESS = "\-\-"
t_MORE_MORE = "\+\+"
t_SUB_EQUAL = "\-="
t_SOMA_EQUAL = "\+="
t_DIVIDE_EQUAL = "/="
t_MULTIPLICATION_EQUAL = "\*="
t_EXCLAMATION_EQUAL = "!="
t_LESS_EQUAL = "<="
t_MORE_EQUAL = ">="
t_AT_SIGN = '@'
t_BOO_BOOLEAN = r'true | false'
t_COMMENT = r'(//.* | /\* ([^*]|[\n])* \*+/)'
t_NUM_DOUBLE = '-?[0-9]+\.[0-9]+'
t_NUM_INT = '-?[0-9]+'
t_DOT = '\.'
t_OR = '\|\|'
t_IF_NULL = '\?\?'
t_AND = '&&'
t_VIRGULA = ','
t_MORE = '\+'
t_LESS = '\-'
t_EXCLAMATION = "!"
t_MULTIPLICATION = '\*'
t_DIVIDE = '/'
t_REST = "%"
t_COMMERCIAL_E = '\&'
t_SEMI_COLON = r'\;'
t_EQUAL = r'={2}'
t_RECEIVE_VALUE = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LCHAV = r'\{'
t_RCHAV = r'\}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_MORETHAN = r'\>'
t_LESSTHAN = r'\<'
t_INTERROGATION = r'\?'
t_COLON = ':'
t_STR_STRING = r"""(".*" | '.*')"""
t_ABSTRACT = 'abstract'
t_AS = 'as'
t_ASSERTS = 'asserts'
t_ASYNC = 'async'
t_AWAIT = 'await'
t_EXPORT = 'export'
t_EXTENDS = 'extends'
t_EXTENSION = 'extension'
t_EXTERNAL = 'external'
t_FACTORY = 'factory'
t_FALSE = 'false'
t_FINAL = 'final'
t_FINALLY = 'finally'
t_FOR = 'for'
t_FUNCTION = 'function'
t_GET = 'get'
t_HIDE = 'hide'
t_IF = 'if'
t_IMPLEMENTS = 'implements'
t_IMPORTS = 'imports'
t_IN = 'in'
t_INTERFACE = 'interface'
t_IS = 'is'
t_LATE = 'late'
t_LIBRARY = 'library'
t_MIXIN = 'mixin'
t_NEW = 'new'
t_NULL = 'null'
t_ON = 'on'
t_OPERATOR = 'operator'
t_PART = 'part'
t_REQUIRED = 'required'
t_RETHROW = 'rethrow'
t_RETURN = 'return'
t_SET = 'set'
t_SHOW = 'show'
t_STATIC = 'static'
t_SUPER = 'super'
t_SWITCH = 'switch'
t_SYNC = 'sync'
t_THIS = 'this'
t_THROW = 'throw'
t_TRUE = 'true'
t_TRY = 'try'
t_TYPEDEF = 'typedef'
t_VAR = 'var'
t_WHILE = 'while'
t_WITH = 'with'
t_YIELD = 'yield'

def t_ID(t):
    #t_ID = r'[a-zA-Z_]+[a-zA-Z_0-9]*'
    r'[a-zA-Z_]+[a-zA-Z_0-9]*'

    t.type = reservadas.get(t.value,t.type)
    return t

lexer = lex.lex()
lexer.input(teste)
#for tok in lexer:
#  print(tok.type, tok.value, tok.lineno, tok.lexpos) 
