import re
cabecalho = "ab,cd{3,5}::sum,abc{4}::media"
for id,min,comp,func in re.findall(r'''
        (\w+)           #identificador
        (?:
            \{
                (?:
                    (\d+)   #minimo
                    ,
                )?
                (\d+)       # comprimento cd     
            \}
        )?
        (?:
            ::
            (\w+)           # funcao de agregacao
        )?           
'''
,cabecalho,flags=re.VERBOSE):
    print(id,min,comp,func)