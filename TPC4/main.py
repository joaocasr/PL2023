import re    

def isDigit(word):
    return str(word).isnumeric()

with open("alunos.csv","r") as csvfile:
    data=list()
    for line in csvfile:
        data.append(line.strip())
    header = list(data)[0]
    data.pop(0)

pattern = re.findall(r'(?P<campos>\w+)(,|{)?',header)
print(pattern)

colunas=list()
for (v,d) in pattern:
    if(isDigit(v)==False):
        colunas.append(v)

geraJSON="""{
                "registos":
                            [
    """

weights=list()
nums=""
it=0
for (variavel,delim) in pattern:
    if(delim=="," and (isDigit(variavel)==False)):
            weights.append(1)
    if(delim=="" and (isDigit(variavel)==True) and it==0):
            weights.append(int(variavel))
    if((delim=="," or delim=="}::" or delim=="") and (isDigit(variavel)==True)):
            if(it==0 and delim!=""):
                nums+="["+variavel
                it+=1
            elif(it==1):
                nums+=","+variavel+"]"
                weights.append(nums)
                nums=""
                it=0
                
            
            
print(weights)

lines=1
for line in data:
    c=0
    componentes=line.split(",")
    #print(componentes)
    i=0
    geraJSON+="""
                    {
            """
    for oc in weights:
        atrib = colunas[i]
        if isDigit(oc) and int(oc)==1:
            if(i<len(weights)-1):
                geraJSON+=f"""
                        "{atrib}":"{componentes[c]}","""
            else: 
                geraJSON+=f"""
                        "{atrib}":"{componentes[c]}" """
            c+=1
        if isDigit(oc) and int(oc)>1:
            geraJSON+=f"""
                        "{atrib}":["""
            if(i<len(weights)-1):        
                for j in range(0,int(oc)):
                    if(j<int(oc)-1): geraJSON+=f"""{componentes[c]},"""
                    if(j==int(oc)-1): geraJSON+=f"""{componentes[c]}],"""
                    c+=1
            else:
                for j in range(0,int(oc)):
                    if(j<int(oc)-1): geraJSON+=f"""{componentes[c]},"""
                    if(j==int(oc)-1): geraJSON+=f"""{componentes[c]}]"""
                    c+=1
        if(isDigit(oc)==False and isDigit(oc.split(",")[1].strip("]"))==True):
            for l in range(c,c+int(oc.split(",")[1].strip("]"))):
                if(isDigit(componentes[l])):
                    auxList.append(int(componentes[l]))
            geraJSON+=f"""
                        "{atrib}":["""
            if(i<len(weights)-1):        
                for j in range(0,len(auxList)):
                    #print(c)
                    if(j<len(auxList)-1): geraJSON+=f"""{auxList[j]},"""
                    if(j==len(auxList)-1): geraJSON+=f"""{auxList[j]}],"""
                
            else:
                for j in range(0,len(auxList)):
                    #print(c)
                    if(j<len(auxList)-1): geraJSON+=f"""{auxList[j]},"""
                    if(j==len(auxList)-1): geraJSON+=f"""{auxList[j]}]"""
            c+=int(oc.split(",")[1].strip("]"))
        auxList=list()
        i+=1
    if(lines<len(data)):
        geraJSON+="""  
                    },
        """     
    else: 
        geraJSON+="""  
                }
        ]
}
        """
    lines+=1

with open("registos.json","w") as jsonfile:
    jsonfile.write(geraJSON)
    
        


