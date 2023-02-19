import matplotlib.pyplot as plt
import math

class Doente:
    def __init__(self,idade,sexo,tensão,colesterol,batimento):
        self.idade=int(idade)
        self.sexo=sexo
        self.tensão=tensão
        self.colesterol=int(colesterol)
        self.batimento=batimento

def dSexo(doentes):
    m = 0
    f= 0
    for doente in doentes:
        if doente.sexo=="M": m+=1
        elif doente.sexo=="F": f+=1
    return [m,f]

def dIdade(doentes):
    distribuicao = {}
    for doente in doentes:
        rangeIdade=f"{int(doente.idade/5) * 5}-{int(doente.idade/5) * 5 + 5}"
        if rangeIdade not in distribuicao: distribuicao[rangeIdade]=0
        distribuicao[rangeIdade]+=1
    sorted_keys= sorted(distribuicao.keys())
    sorted_values={key:distribuicao[key] for key in sorted_keys}
    return list(sorted_keys),list(sorted_values.values())
    
def dColesterol(doentes,limiteInf):
    distribuicao = {}
    for doente in doentes:
        rangeColesterol=f"{int((doente.colesterol-limiteInf)/10)*10 + limiteInf}-{int((doente.colesterol-limiteInf)/10)*10 + limiteInf + 10}"
        if rangeColesterol not in distribuicao: distribuicao[rangeColesterol]=0
        distribuicao[rangeColesterol]+=1
    sorted_keys= sorted(distribuicao.keys())
    sorted_values={key:distribuicao[key] for key in sorted_keys}
    return list(sorted_keys),list(sorted_values.values())

def printTabela(nome, parametros, valores):
    data = [nome]
    for i in range(len(parametros)):
        data.append((parametros[i],valores[i]))

    fig, ax = plt.subplots()

    # Hide axes
    ax.axis('off')
    


    # Create table
    table = ax.table(cellText=data, loc='center')

    table.set_fontsize(8)

    # Set cell height and width
    table.scale(0.4, 0.8)

    plt.show()

def printGrafico(nome, nomey, parametros,valores):
    fig = plt.figure(figsize = (15, 7))
 
    # creating the bar plot
    plt.bar(parametros, valores, color ='maroon',
            width = 0.4)
    
    plt.ylabel(nomey)
    plt.title(nome)
    plt.show()



def main():
    f=open("myheart.csv")
    lines = f.readlines()
    doentes = []
    limInferiorColesterol= math.inf
    for line in lines[1:]:
        idade,sexo,tensão,colesterol,batimento,temDoença = line.split(",")
        if int(temDoença)==1:
            doentes.append(Doente(idade,sexo,tensão,colesterol,batimento))
            if int(colesterol)<limInferiorColesterol: limInferiorColesterol=int(colesterol)
    saida = -1
    while saida != 0:
        print("1-Distribuição por sexo")
        print("2-Distribuição por idade")
        print("3-Distribuição por colesterol")
        print("0-Sair")
        saida = int(input("Introduza a sua opcao-> "))
        if saida == 0:
            print("A sair .....")
        elif saida == 1:
            distSexo = dSexo(doentes)
            opcao = 1
            while(opcao):
                print("1-Tabela")
                print("2-Gráfico")
                opcao = int(input("Introduza a sua opcao-> "))
                if (opcao==1):
                    printTabela(['Sexo', 'Quantidade'],["M","F"],distSexo)
                    break
                elif(opcao==2):
                    printGrafico("Distribuição dos doentes por sexo","Número de doentes",["M","F"],distSexo)
                    break
                else: print("Opcão inválida")
        elif saida == 2:
            idades,distIdade = dIdade(doentes)
            opcao = 1
            while(opcao):
                print("1-Tabela")
                print("2-Gráfico")
                opcao = int(input("Introduza a sua opcao-> "))
                if (opcao==1):
                    printTabela(['Idade', 'Quantidade'],idades,distIdade)
                    break
                elif(opcao==2):
                    printGrafico("Distribuição dos doentes por idade","Número de doentes",idades,distIdade)
                    break
                else: print("Opcão inválida")
        elif saida == 3:
            c,distColestrol = dColesterol(doentes,limInferiorColesterol)
            opcao = 1
            while(opcao):
                print("1-Tabela")
                print("2-Gráfico")
                opcao = int(input("Introduza a sua opcao-> "))
                if (opcao==1):
                    printTabela(['Colesterol', 'Quantidade'],c,distColestrol)
                    break
                elif(opcao==2):
                    printGrafico("Distribuição dos doentes por colesterol","Número de doentes",c,distColestrol)
                    break
                else: print("Opcão inválida")
            
            
        
    
if (__name__=="__main__"):
    main()