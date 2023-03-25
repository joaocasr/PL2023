import ply.lex as lex
import re

txt="""
# jrhtjerhthjer
## gjdfigjdfigdfg
this idsf **dfdaf** sdfsdf
"""



tokens = [
    'TITLE',
    'OUTRO',
    'BOLD'
    ]


#(int,123) => (t.type,t.value)
def t_TITLE(t):
    r'\# .*'
    print(f"""<h1>{t.value.strip("# ")}</h1>""",end="")

def t_BOLD(t):
    r'\*\*.+?\*\*' #+? come o menos possível primeira ocorrencia de(**) **p1** ________ **p2**
    print(f"""<b>{t.value.strip("**")}</b>""",end="")


def t_OUTRO(t):
    r'.|\n'
    print(t.value,end="")

def t_error(t):
    print(f"Carácter ilegal {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

lexer.input(txt)

#while tok:=lexer.token():
#    print(tok)
lexer.token()