import sys
import re

current_state = 1

commands = ("LEVANTAR", #0
            "POUSAR",   #1
            "MOEDA",    #2
            "T",        #3
            "ABORTAR")  #4

custos = {
            "800":0,
            "808":0.10,
            "2":0.25,
            "00":1.50,
        }

valid_coins = ("10c","20c", "50c","1e","2e")
invalid_coins=list()
saldo=0.00
inserted_coins = list()

def valida_moedas(moedas):
    global saldo,invalid_coins
    maq_msg="maq: '"
    for m in moedas:
        if m in valid_coins:
            if("c" in m):
                coin = int(m.strip("c"))
                saldo+=(coin/100)
                inserted_coins.append(coin/100)
            if("e" in m):
                coin = int(m.strip("e"))
                saldo+=coin
                inserted_coins.append(coin)
        else:
            invalid_coins.append(m)
    if(len(invalid_coins)>0):
        for inv in invalid_coins:
            maq_msg+=inv
            maq_msg+=" "
        maq_msg+="- moeda(s) inválida(s); "
    maq_msg+="saldo = "
    maq_msg+=formato_saldo(saldo)
    print(maq_msg+"'")

def formato_saldo(value):
    valor=""
    sald = "{:.2f}".format(value)
    eur=str(sald).split(".")[0]+"e"
    cent=str(sald).split(".")[1]+"c"
    valor = eur+cent
    return valor

def valida_num(numero):
    global saldo
    if(len(numero)!=9):
        print("maq: 'Número introduzido não reconhecido.'")
    else:
        three=re.match(r'(\d{3})\d+',numero)
        two=re.match(r'(\d{2})\d+',numero)
        one=re.match(r'(\d{1})\d+',numero)
        if(three.group(1)=="601" or three.group(1)=="641"):
            print("maq: 'Esse número não é permitido neste telefone. Queira discar novo número!'")
        if(three.group(1)=="800"):
            print("maq: 'saldo = "+formato_saldo(saldo))
        if(three.group(1)=="808"):
            if(saldo<custos["808"]):
                falta=custos["808"]-saldo
                print("maq: Saldo insuficiente para efetuar a chamada. Introduza mais "+formato_saldo(falta)+" se quiser efetuar a chamada.")
            else:
                saldo-=custos["808"]
                print("maq: 'saldo = "+formato_saldo(saldo))
        if(two.group(1)=="00"):
            if(saldo<custos["00"]):
                falta=custos["00"]-saldo
                print("maq: Saldo insuficiente para efetuar a chamada. Introduza mais "+formato_saldo(falta)+" se quiser efetuar a chamada.")
            else:
                saldo-=custos["00"]
                print("maq: 'saldo = "+formato_saldo(saldo))
        if(one.group(1)=="2"):
            if(saldo<custos["2"]):
                falta=custos["2"]-saldo
                print("maq: Saldo insuficiente para efetuar a chamada. Introduza mais "+formato_saldo(falta)+" se quiser efetuar a chamada.")
            else:
                saldo-=custos["2"]
                print("maq: 'saldo = "+formato_saldo(saldo))


def abortar_operacao():
    global saldo
    troco=saldo
    saldo=0
    print("maq: 'Interação interrompida; Devolve = "+formato_saldo(troco)+" ; saldo = "+formato_saldo(saldo))

def terminar_operacao():
    global saldo
    troco = saldo
    saldo=0
    print("maq: troco="+formato_saldo(troco)+" ; Volte sempre!")

def levantar_operacao():
    print("maq: 'Introduza moedas.'")

def exception_commands(desired_command):
    exc =0
    global current_state
    if(desired_command== 2 and current_state==1):
        print("Levante o auscultador e depois introduza as moedas.")
        exc=1
    if(desired_command== 3 and current_state==1):
        print("Levante o auscultador e depois introduza as moedas.")
        exc=1
    if(desired_command== 4 and current_state==1):
        print("Não existem processos a abortar.")
        exc=1
    if(desired_command== 0 and current_state==0):
        print("O auscultador já se encontra levantado.")
        exc=1
    return exc

def read_command(command):
    global current_state,saldo
    valid=-1
    if(re.match(r'LEVANTAR$',command)!=None):
        valid=0
        if(exception_commands(0)==0):
            current_state=0
            levantar_operacao()
    if(re.match(r'POUSAR$',command)!=None):
        valid=0
        if(exception_commands(1)==0):
            current_state=1
            terminar_operacao()
    if((re.match(r'MOEDA\s(?P<moedas>(\d+(c|e),?\s?)+)',command))!=None):
        valid=0
        if(exception_commands(2)==0):
            current_state=2
            coins= re.findall(r'(\d+(c|e))(,\t)?',command)
            moedas=list()
            for coin in coins:
                m = coin[0]
                moedas.append(m)
            valida_moedas(moedas)
    if(re.match(r'T=\d+',command)!=None):
        valid=0
        if(exception_commands(3)==0):
            current_state=3
            num = re.match(r'T=(\d+)',command)
            valida_num(num.group(1))
    if(re.match(r'ABORTAR$',command)!=None):
        valid=0
        if(exception_commands(4)==0):
            current_state=4
            abortar_operacao()
    return valid        

        
def main():
    r=-1
    for line in sys.stdin:
        r=read_command(line)
        if(r==-1):
            print("maq: Operação inválida.")


if __name__=="__main__":
    main()
