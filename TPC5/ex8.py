import re

texto="""Em estilística, a repetição é um termo genérico que engloba as repetições de palavras e as repetições de sons. Ao utilizar a língua como um material sonoro, a repetição transmite pela acumulação de palavras ou sons idênticos uma maior força expressiva.
REPETIÇÕES DE PALAVRAS:
Entre as repetições de palavras, é possível encontrarem-se o epizeuxe (ou paliologia), que consiste em repetir uma palavra sem conjunção, obtendo-se assim um efeito de insistência e intensificação:
"E também o vento é vão, dizias, dizias. Que só o crepúsculo é verdadeiro, o crepúsculo dos deuses. Esse, repetes, repetes, pulsa na música de Wagner..."
"""

palavras = dict()

lista = re.finditer(r'(\w+)',texto)
for elem in lista:
    if elem.group(1).capitalize() in palavras:
        palavras[elem.group(1).capitalize()].append(elem.span())
    if elem.group(1).upper() in palavras:
        palavras[elem.group(1).upper()].append(elem.span())
    if elem.group(1).lower() in palavras:
        palavras[elem.group(1).lower()].append(elem.span())
    elif elem.group(1) not in palavras:
        palavras[elem.group(1)] = list()
        palavras[elem.group(1)].append(elem.span())
    else:
        palavras[elem.group(1)].append(elem.span())

counter=0
final=""
i=0
lista = list()
reps=list()
for word in palavras:  
    #print(word+" :",end="")
    #print(palavras[word])
    if(len(palavras[word])>1):
        for j in range(1,len(palavras[word])):
            reps.append(palavras[word][j])
    lista.append((word,palavras[word][0]))

size=len(lista)
begin=0
end=0
while(i<size):
    if(i<size -1):
        current=lista[i][0]
        next=lista[i+1][0]
        begin=lista[i][1][1]
        end=lista[i+1][1][0]
        final+=current
        for it in range(begin,end):
            if(re.match(r'\w',texto[it])==None):
                final+=texto[it]
    else:
        current=lista[i][0]
        final+=current
    i+=1
print(">>>>>>> ORIGINAL:")
print(texto)
print(">>>>>>> OUTPUT:")
print(final)