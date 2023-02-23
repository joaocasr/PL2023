import re as regex

soma=0
ativo=False

def main():
    on=ativo
    counter=soma
    while(True):
        line=input(">>> ")
        if(len(regex.findall("on|ON|On",line))>0):
            on=True
            print("Contador ativado.")
        if(len(regex.findall("off|OFF|Off",line))>0):
            on=False
            print("Contador desativado.")
        if(on==True):
            numbers=regex.findall("[0-9]+",line)
            for n in numbers:
                counter+=int(n)
        if(len(regex.findall("=",line))>0):
            print(counter)
        
if __name__== "__main__":
    main()