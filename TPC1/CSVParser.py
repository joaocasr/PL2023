import csv

class CSVParser:

    def __init__(self):
        self.pacientes = dict()
        self.size = 0
        self.header = list()
        self.headersize= 0
        self.headerDistBySex=["Sexo","Nº de doentes"]
        self.distBySex = dict()
        self.headerDistByIdade=["Escalão Etário","Nº de doentes"]
        self.distByIdade = dict()
        self.headerDistByColestrol=["Níveis de Colestrol","Nº de doentes"]
        self.distByColestrol= dict()

    def fill_Header(self,cabecalho,n):
        i=0
        while(i<n):
            self.header.append(cabecalho[i])
            i+=1
        self.headersize=n

    def parse(self,filename):
        i=0
        with open(filename,"r") as csvfile:
            pacientes= list(csv.reader(csvfile, delimiter=','))
            self.fill_Header(pacientes[0],len(pacientes[0]))
            for paciente in pacientes: #paciente é uma linha do ficheiro
                if (i!=0):
                    self.pacientes[i]={}
                    for j in range(self.headersize):
                        self.pacientes[i][self.header[j]]=paciente[j]
                    #print(str(i)+":"+str(self.pacientes[i]))
                i+=1
                j=0
        self.size=i-1
        #print("size:"+str(self.size))

    #distribuicao da doenca por sexo
    def calcula_Por_Sexo(self):
        i=1
        self.distBySex={"M":0,"F":0}
        while(i<=self.size):
            if(self.pacientes[i][self.header[5]]=='1'):
                self.distBySex[self.pacientes[i][self.header[1]]]+=1
            i+=1
        return self.distBySex
    
    #calcula a idade do paciente mais velho
    def calcula_Max_Idade(self):
        i=1
        max=0
        while(i<=self.size):
            if int(self.pacientes[i][self.header[0]])>max:
                max=int(self.pacientes[i][self.header[0]])
            i+=1
        return max

    def calcula_Dist_Esc(self):
        passo=4
        idade_inicial=30
        max=self.calcula_Max_Idade()
        while(idade_inicial<max):
            if idade_inicial+passo<=max:
                self.distByIdade["["+str(idade_inicial)+"-"+str(idade_inicial+passo)+"]"]=0
            else: self.distByIdade["["+str(idade_inicial)+"-"+str(max)+"]"]=0
            idade_inicial+=passo
        i=1
        while(i<=self.size):
            for faixa in self.distByIdade:
                intervalo=faixa[1:-1] #drop first and last character
                idade_inf=intervalo.split("-")[0] #split the inferior limit and the superior limit by "-"
                idade_sup=intervalo.split("-")[1]
                if(int(self.pacientes[i][self.header[0]])>=int(idade_inf) and int(self.pacientes[i][self.header[0]])<=int(idade_sup) and 
                self.pacientes[i][self.header[5]]=='1'):
                    self.distByIdade[faixa]+=1
            i+=1
        return self.distByIdade

    def calcula_Max_Colestrol(self):
        i=1
        max=0
        while(i<=self.size):
            if(int(self.pacientes[i][self.header[3]])>max):
                max=int(self.pacientes[i][self.header[3]])
            i+=1
        return max
    
    def calcula_Min_Colestrol(self):
        i=1
        min=int(self.pacientes[i][self.header[3]])
        while(i<=self.size):
            if(int(self.pacientes[i][self.header[3]])<min):
                min=int(self.pacientes[i][self.header[3]])
            i+=1
        return min
    
    def calcula_Dist_Colestrol(self):
        passo=10
        maximum=self.calcula_Max_Colestrol()
        minimum=self.calcula_Min_Colestrol()
        while(minimum<maximum):
            if minimum+passo<=maximum:
                self.distByColestrol["["+str(minimum)+"-"+str(minimum+passo)+"]"]=0
            else: self.distByColestrol["["+str(minimum)+"-"+str(maximum)+"]"]=0
            minimum+=passo
        i=1
        while(i<=self.size):
            for colestrol in self.distByColestrol:
                intervalo=colestrol[1:-1] #drop first and last character
                colest_inf=intervalo.split("-")[0] #split the inferior limit and the superior limit by "-"
                colest_sup=intervalo.split("-")[1]
                if(int(self.pacientes[i][self.header[3]])>=int(colest_inf) and int(self.pacientes[i][self.header[3]])<=int(colest_sup) and 
                self.pacientes[i][self.header[5]]=='1'):
                    self.distByColestrol[colestrol]+=1
            i+=1
        return self.distByColestrol

    def get_Header_Por_Sexo(self):
        return self.headerDistBySex
    
    def get_Header_Por_Escalao(self):
        return self.headerDistByIdade

    def get_Header_Por_Colestrol(self):
        return self.headerDistByColestrol