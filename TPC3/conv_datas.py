#!/usr/bin/env python3
import re
import sys
#FICHA 2 ex1
texto = """A 03/01/2022, Pedro viajou para a praia com a sua família.
Eles ficaram hospedados num hotel e aproveitaram o sol e o mar durante toda a semana.
Mais tarde, no dia 12/01/2022, Pedro voltou para casa e começou a trabalhar num novo projeto.
Ele passou muitas horas no escritório, mas finalmente terminou o projeto a 15/01/2022."""

# ...

def iso_8601(txt):
    return re.sub(r'(?P<dia>\d{2})/(?P<dia>\d{2})/(?P<ano>\d{4})',r'\g<ano>-\g<mes>-\g<dia>',txt)
    #pattern2= re.sub(r'(\d{2})/(\d{2})/(\d{4})',r'\3-\2-\1',txt)
    #pattern3 = re.sub(r'(\d{2})/(\d{2})/(\d{4})',lambda x:f"{x[3]-x[2]-x[1]}",txt)

def main():
    if(len(sys.argv)==2):
        file= sys.argv[1]
        with open(file,'r') as f:
            texto = f.read()
    else:
        texto=sys.stdin.read()
    print(iso_8601(texto))

if __name__=="__main__":
    main()