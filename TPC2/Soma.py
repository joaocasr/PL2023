class Soma:
    def __init__(self):
        self.all_Numbers=list()
        self.all_Numbers.append(0)  
        self.dict_lines = dict()
        self.on = False

    def is_numb(self,c):
        r=False
        if(c=='1' or c=='2' or c=='3' or c=='4' or c=='5' or c=='6' or c=='7' or c=='8' or c=='9'): r=True
        return r

    def filter_numbs(self):
        number=""
        for k in self.dict_lines:
            for ch in self.dict_lines[k]:
                if(self.is_numb(ch)):
                    number+=ch
                elif(self.is_numb(ch)!=True and number!=""):
                    numero=int(number)
                    self.all_Numbers.append(numero)
                    number=""
        if(number!=""):
            numero=int(number)
            self.all_Numbers.append(numero)                    

    def check_OFF(self,line):
        r=-1
        if("Off" in line or "OFF" in line or "off" in line): r=1
        if("On" in line or "ON" in line or "on" in line): r=0
        return r

    def check_Eq(self,line):
        r=False
        if("=" in line): r=True
        return r

    def calcula_Soma(self):
        c=0
        for n in self.all_Numbers:
            c+=n
        return c
    
    def clear(self):
        self.dict_lines.clear()