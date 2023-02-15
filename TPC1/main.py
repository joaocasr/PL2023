from CSVParser import CSVParser
from tabulate import tabulate
 
def main():
    csvparser = CSVParser()
    csvparser.parse("/home/joao/PL2023/TPC1/myheart.csv")
    while(1):
        print()
        opcoes={1:"Tabela da distribuição da doença por sexo.",
                2:"Tabela da distribuição da doença por escalões etários.",
                3:"Tabela da distribuição da doença por niveis de colestrol."}
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
        linhas=list()
        for estatistica in estatisticas.items():
            linhas.append(list(estatistica))

        if(opcao=="1"):print(tabulate(linhas, csvparser.get_Header_Por_Sexo()))
        if(opcao=="2"):print(tabulate(linhas, csvparser.get_Header_Por_Escalao()))
        if(opcao=="3"):print(tabulate(linhas, csvparser.get_Header_Por_Colestrol()))

if __name__ == "__main__":
    main()