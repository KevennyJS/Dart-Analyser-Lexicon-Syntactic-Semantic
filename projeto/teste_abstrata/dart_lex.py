import ply.lex as lex

tokens = ["NUM", "MAIS", "LPAREN", "RPAREN", "MENOS"]


t_ignore  = ' \t\n'

t_LPAREN = "\("
t_RPAREN = "\)"
t_NUM = r"[0-9]+"
t_MAIS = r"\+"
t_MENOS = r"\-"

def t_error(t):
    print("Caractere ilegal '%s'" % t.value[0])
    t.lexer.skip(1)
    
lexer = lex.lex()
lexer.input("8 + 8")
