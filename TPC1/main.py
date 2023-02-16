from CSVParser import CSVParser
from tabulate import tabulate
import pandas as pd             
import matplotlib.pyplot as plt 

def main():
    csvparser = CSVParser()
    csvparser.parse("/home/joao/PL2023/TPC1/myheart.csv")
    while(1):
        print()
        print("------------ MyHeart.csv ------------")
        opcoes={1:"Tabela da distribuição da doença por sexo.",
                2:"Tabela da distribuição da doença por escalões etários.",
                3:"Tabela da distribuição da doença por niveis de colestrol.",
                4:"Gráfico da distribuição da doença por sexo.",
                5:"Gráfico da distribuição da doença por escalões etários.",
                6:"Gráfico da distribuição da doença por niveis de colestrol."}
        for op in opcoes:
            print(str(op)+":"+opcoes.get(op))
        print()
        opcao=input("Digite uma das opções disponibilizadas:")
        if(opcao=="1"):
            print()
            estatisticas=csvparser.calcula_Por_Sexo()
        if(opcao=="2"):
            print()
            estatisticas=csvparser.calcula_Dist_Esc()
        if(opcao=="3"):
            print()
            estatisticas=csvparser.calcula_Dist_Colestrol()
        if(opcao=="4"):
            print()
            l=list()
            lista = csvparser.calcula_Por_Sexo().items()
            for category in lista: #("M",420)
                l.extend(category[0]*int(category[1]))
            df = pd.DataFrame({'Sexo':l})
            categories = df['Sexo'].value_counts().index
            counts = df['Sexo'].value_counts().values
            plt.xlabel("Sexo")
            plt.ylabel("Nº de doentes")
            plt.bar(categories, counts, width=0.5)
            plt.show()
            continue
        if(opcao=="5"):
            print()
            l=list()
            lista = csvparser.calcula_Dist_Esc().items()
            for category in lista: 
                for j in range(0,int(category[1])):
                    l.append(str(category[0]))
            df = pd.DataFrame({'Escalao':l})
            categories = df['Escalao'].value_counts().index
            counts = df['Escalao'].value_counts().values
            plt.xlabel("Escalão")
            plt.ylabel("Nº de doentes")
            plt.bar(categories, counts, width=0.5)
            plt.show()
            continue
        if(opcao=="6"):
            print()
            l=list()
            lista = csvparser.calcula_Dist_Colestrol().items()
            for category in lista: 
                for j in range(0,int(category[1])):
                    l.append(str(category[0]))
            df = pd.DataFrame({'Nivel':l})
            categories = df['Nivel'].value_counts().index
            counts = df['Nivel'].value_counts().values
            plt.xlabel("Nível de colestrol")
            plt.ylabel("Nº de doentes")
            plt.bar(categories, counts, width=0.5)
            plt.show()
            continue
        linhas=list()
        for estatistica in estatisticas.items():
            linhas.append(list(estatistica))
        if(opcao=="1"):print(tabulate(linhas, csvparser.get_Header_Por_Sexo()))
        if(opcao=="2"):print(tabulate(linhas, csvparser.get_Header_Por_Escalao()))
        if(opcao=="3"):print(tabulate(linhas, csvparser.get_Header_Por_Colestrol()))

if __name__ == "__main__":
    main()