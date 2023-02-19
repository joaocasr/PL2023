from CSVParser import CSVParser
from tabulate import tabulate
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
            dic = csvparser.calcula_Por_Sexo()
            counts=list()
            categories=list()
            for k in dic:
                categories.append(k)
                counts.append(dic[k])
            plt.xlabel("Sexo")
            plt.ylabel("Nº de doentes")
            plt.bar(categories, counts, width=0.5)
            plt.show()
            continue
        if(opcao=="5"):
            print()
            l=list()
            counts=list()
            categories=list()
            dic=csvparser.calcula_Dist_Esc()
            for k in dic:
                categories.append(k)
                counts.append(dic[k])
            plt.xlabel("Escalão")
            plt.ylabel("Nº de doentes")
            plt.bar(categories, counts, width=0.5)
            plt.show()
            continue
        if(opcao=="6"):
            print()
            dic=csvparser.calcula_Dist_Colestrol()
            counts=list()
            categories=list()
            for k in dic:
                categories.append(k)
                counts.append(dic[k])
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