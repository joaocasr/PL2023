from Soma import Soma

def main():
    l=0
    soma = Soma()
    while(1):
        print(">>> ",end="") 
        line=input("")
        if(soma.check_OFF(line)==1):
            soma.on=False
        elif(soma.check_OFF(line)==0):
            soma.on=True
        if(soma.check_Eq(line)):
            if(soma.on): soma.dict_lines[l]=line
            soma.filter_numbs()
            total=soma.calcula_Soma()
            print(total)
            soma.clear()
        elif(soma.on and soma.check_OFF(line)==-1):
            soma.dict_lines[l]=line
            l+=1

if __name__=="__main__":
    main()

