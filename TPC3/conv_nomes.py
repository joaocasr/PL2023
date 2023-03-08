#!/usr/bin/env python3
import re
import sys
#FICHA 2 ex2
texto = """Este texto foi feito por Sofia Guilherme Rodrigues dos Santos, com 
base no texto original de Pedro Rafael Paiva Moura, com a ajuda
de Pedro Rangel Henriques e José João Antunes Guimarães Dias de Almeida.
Apesar de partilharem o mesmo apelido, a Sofia não é da mesma família do famoso
autor José Rodrigues dos Santos."""

def conv_name(txt):
    return re.sub(r'(?P<nome>((?P<first>[A-Z]\w+)\s([A-Z]\w+\s)+(de|dos|da)?\s?(?P<last>[A-Z]\w+))|([A-Z]\w+\s?[A-Z]\w+)+)',"\g<last>, \g<first>",txt)

def main():
    if(len(sys.argv)==2):
        file= sys.argv[1]
        with open(file,'r') as f:
            texto = f.read()
    else:
        texto=sys.stdin.read()
    print("\n>>> Ouput:")
    print(conv_name(texto))

if __name__=="__main__":
    main()