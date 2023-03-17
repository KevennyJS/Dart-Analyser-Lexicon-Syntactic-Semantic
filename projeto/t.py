import ply.lex as lex # importando a biblioteca ply para o léxico
#Definindo Tokens e seus padroes
tokens = ("PLUS", "MINUS")
t_PLUS    = r'\+'
t_MINUS   = r'-'
#Criando analisador Lexico e realizando analise lexica
lexer = lex.lex()
lexer.input("+---+++")
for tok in lexer:
  print(tok.type, tok.value, tok.lineno, tok.lexpos) 
