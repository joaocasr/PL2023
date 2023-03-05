import re

def main():
    with open("processos.txt","r") as txtfile:
        processos=txtfile.readlines()   
    while(True):
        print("*************************************")
        print("1- Frequência de registos por ano")
        print("2- Distribuição de primeiros nomes por século")
        print("3- Distribuição de apelidos por século")
        print("4- Top 5 nomes mais usados")
        print("5- Top 5 apelidos mais usados")
        print("6- Frequência dos graus de parentesco.")
        print("7- Converter os 20 registos para JSON.")
        print("**************************************\n")
        opcao = input("Digite a opcao:")

        dateList_dic = []
        dict_years = dict()
        dict_fstnameCentury= dict()
        dict_lstnameCentury= dict()
        dict_allNames = dict()
        dict_allApelidos= dict()
        dict_relations = dict()

        if(opcao=="1"):
            # FREQUENCIA POR ANOS
            for line in processos:
                pattern_Date = re.match(r'\d+::(?P<ano>[0-9]+)-(?P<mes>[0-9]+)-(?P<dia>[0-9]+)',line)
                if(pattern_Date!=None):
                    dateList_dic.append(pattern_Date.groupdict())
            for d in dateList_dic:
                if(d['ano'] not in dict_years):
                    dict_years[d['ano']]=1
                else: dict_years[d['ano']]+=1

            print("*** Distribuição de registos por ano ***")
            for regist in dict_years:
                print("Ano "+regist+" -> "+str(dict_years[regist])+" registos") 
            print("****************************************")

        if(opcao=="2"):
            # FREQUENCIA PRIMEIROS NOMES
            for line in processos:
                pattern_name = re.match(r'\d+::(?P<ano>[0-9]+)-\d+-\d+::(?P<nome>[a-zA-Z]+)\s?\w*',line)
                if(pattern_name!=None):
                    century = int(pattern_name.groupdict()['ano']) // 100 +1
                    if(century not in dict_fstnameCentury): 
                        dict_fstnameCentury[century] = dict()
                        dict_fstnameCentury[century][pattern_name.groupdict()['nome']]=1
                    else: 
                        if(pattern_name.groupdict()['nome'] in dict_fstnameCentury[century]):
                            dict_fstnameCentury[century][pattern_name.groupdict()['nome']]+=1
                        else: dict_fstnameCentury[century][pattern_name.groupdict()['nome']]=1
            print("*** Distribuição de nomes por séculos ***")
            for sec in dict_fstnameCentury:
                print("****** Séc. "+str(sec)+" *********")
                for name in dict_fstnameCentury[sec]:
                    print(name+" :"+ str(dict_fstnameCentury[sec][name]))
                print("")
            print("****************************************")

        if(opcao=="3"):
            # FREQUENCIA APELIDOS
            for line in processos:
                pattern_apelido = re.match(r'\d+::(?P<ano>[0-9]+)-\d+-\d+::(\w+\s)*(?P<apelido>[a-zA-Z]+)::\w*',line)
                if(pattern_apelido!=None):
                    century = int(pattern_apelido.groupdict()['ano']) // 100 +1
                    if(century not in dict_lstnameCentury): 
                        dict_lstnameCentury[century] = dict()
                        dict_lstnameCentury[century][pattern_apelido.groupdict()['apelido']]=1
                    else: 
                        if(pattern_apelido.groupdict()['apelido'] in dict_lstnameCentury[century]):
                            dict_lstnameCentury[century][pattern_apelido.groupdict()['apelido']]+=1
                        else: dict_lstnameCentury[century][pattern_apelido.groupdict()['apelido']]=1
            print("*** Distribuição de apelidos por séculos ***")
            for sec in dict_lstnameCentury:
                print("****** Séc. "+str(sec)+" *********")
                for apelido in dict_lstnameCentury[sec]:
                    print(apelido+" :"+ str(dict_lstnameCentury[sec][apelido]))
                print("")
            print("****************************************")

        if(opcao=="4"):
            # 5 nomes mais usados
            print("****************************************")
            print("TOP 5 nomes mais usados")
            print("****************************************")
            for line in processos:
                pattern_nome = re.match(r'\d+::\d+-\d+-\d+::(?P<nome>[a-zA-Z]+)\s?\w*',line)
                if(pattern_nome!=None):
                    if(pattern_nome.groupdict()['nome'] not in dict_allNames): 
                        dict_allNames[pattern_nome.groupdict()['nome']]=1
                    else: 
                        dict_allNames[pattern_nome.groupdict()['nome']]+=1
            aux = []
            for nome in dict_allNames:
                aux.append((nome,dict_allNames[nome]))
            aux.sort(key=lambda x:x[1],reverse=True)
            if(len(aux)<5):
                p=1
                for (nome,freq) in aux:
                    print(str(p)+"º -"+nome)
                    p+=1
            else:
                p=1
                for (nome,freq) in aux:
                    print(str(p)+"º -"+nome)
                    if(p==5): break
                    p+=1
        if(opcao=="5"):
            # 5 apelidos mais usados
            print("****************************************")
            print("TOP 5 apelidos mais usados")
            print("****************************************")
            for line in processos:
                pattern_apelido = re.match(r'\d+::\d+-\d+-\d+::(\w+\s)*(?P<apelido>[a-zA-Z]+)::\w*',line)
                if(pattern_apelido!=None):
                    if(pattern_apelido.groupdict()['apelido'] not in dict_allApelidos): 
                        dict_allApelidos[pattern_apelido.groupdict()['apelido']]=1
                    else: 
                        dict_allApelidos[pattern_apelido.groupdict()['apelido']]+=1
            aux = []
            for nome in dict_allApelidos:
                aux.append((nome,dict_allApelidos[nome]))
            aux.sort(key=lambda x:x[1],reverse=True)
            if(len(aux)<5):
                p=1
                for (nome,freq) in aux:
                    print(str(p)+"º -"+nome)
                    p+=1
            else:
                p=1
                for (nome,freq) in aux:
                    print(str(p)+"º -"+nome)
                    if(p==5): break
                    p+=1
        if(opcao=="6"):
            k=0
            for line in processos:
                pattern_family = re.findall(r',(?P<parentesco>([a-zA-Z]+\s?)*)\.',line)
                if(pattern_family!=None):
                    for parent in pattern_family:
                        if(parent[0] not in dict_relations):
                            dict_relations[parent[0]]=1
                        else:
                            dict_relations[parent[0]]+=1
            for parentesco in dict_relations:
                print(parentesco+" : "+ str(dict_relations[parentesco]) + " pessoas")

        if(opcao=="7"):
            with open("processos.json","w") as jsonfile:
                geraJSON="""{"""
                geraJSON+="""
                    "registos": [
                            """
                registos=0
                for line in processos:
                        prim_groups = re.match(r'(?P<pasta>\d+)::(?P<data>\d+-\d+-\d+)::(?P<nome>([a-zA-Z]+\s?)*)::(?P<pai>([a-zA-Z]+\s?)*)::(?P<mae>([a-zA-Z]+\s?)*).*',line)
                        obs_groups = re.findall(r'(?P<relacionados>(\w\s?)+),(?P<parentesco>(\w\s?)+)\.\sProc\.(?P<processo>\d+)\.',line)
                        if(prim_groups!=None):
                            geraJSON+="""
                            {"""
                            geraJSON+= f"""
                                "pasta":{prim_groups.groupdict()['pasta']},
                                "data":"{prim_groups.groupdict()['data']}",
                                "nome":"{prim_groups.groupdict()['nome']}",
                                "pai":"{prim_groups.groupdict()['pai']}",
                                "mae":"{prim_groups.groupdict()['mae']}",
                                "familia":["""  
                            #print(prim_groups.groupdict(),end="")
                            registos+=1
                        k=len(obs_groups)
                        if(k>=1 and prim_groups!=None):    
                            for parent in obs_groups:
                                #print(parent[0],parent[2],parent[4])
                                geraJSON+="""
                                    {"""    
                                geraJSON+=f"""  
                                    "nome":"{parent[0]}",
                                    "parentesco":"{parent[2]}",
                                    "processo":"{parent[4]}"
                                """
                                geraJSON+="""   }"""
                                if(k>=2):
                                    geraJSON+=""","""
                                    k-=1
                                elif(k>=1 and registos<20):
                                    geraJSON+="""
                                        ]
                                    },"""
                                    k-=1
                                    break
                        elif(k==0 and prim_groups!=None):
                            geraJSON+="""]
                            },"""
                        if(registos==20): break        
                geraJSON+="""
                            ]
                        }
                    ]
                }"""
                jsonfile.write(geraJSON)

if __name__ == "__main__":
    main()