import ply.lex as lex
import re

texto="""Era uma vez um gato/ maltês."""

tokens = [
    'WORD',
    'VIRGULA',
    'OUTROS'
]

t_WORD = r'\w+'
t_VIRGULA = r','
t_OUTROS=r'[!?."]'

t_ignore = ' \t\n'

def t_error(t):
    print(f"Carácter ilegal {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

lexer.input(texto)

while tok:=lexer.token():
    print(tok)