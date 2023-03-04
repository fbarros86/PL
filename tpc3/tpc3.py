import re
import json
import collections

def processosPorAno(processos):
    pass


def top5Names(nomes,apelidos):
    sortednomes = collections.OrderedDict(nomes, reverse=True)
    sortedapelido = collections.OrderedDict(apelidos, reverse=True)

    print("TOP 5 NOMES:")
    for proprio in list(sortednomes.keys())[:5]:
        print(f"{proprio}")
    print()
    print("TOP 5 APELIDOS: ")
    for apelido in list(sortedapelido.keys())[:5]:
        print(f"{apelido}")
    input()

    


def toJson():
    f=open("processos.txt")
    lines = f.readlines()
    f.close()
    f = open("processos.json","w")
    f.write("[\n")
    flag=0
    for line in lines[:20]:
        if flag:f.write(",\n")
        else: flag=1
        match = re.search(r"(?P<Pasta>\d+)::(?P<Data>\d+-\d+-\d+)::(?P<Nome>[A-Za-z]+[A-Za-z ]*?[A-Za-z]+)::(?P<Pai>[A-Za-z]+[A-Za-z ]*?[A-Za-z]+)?::(?P<Mae>[A-Za-z]+[A-Za-z ]*?[A-Za-z]+)?::(?P<Outro>.*?)::",line)
        json.dump(match.groupdict(),f)
    f.write("]\n")
    f.close()
        

def getSeculo(year):
    if year % 100 == 0:
        return year // 100
    else:
        return year // 100 + 1
    

def main():
    f=open("processos.txt")
    lines = f.readlines()
    f.close()
    datas = {}
    seculosnomes={}
    relacoes={}
    nprocessos=0
    for line in lines:
        if (line[0].isdigit()):
            nprocessos+=1
            data = re.search(r"::(\d+)-.*?::",line).group(1)
            nome = re.search(r"::([A-Za-z]+)[A-Za-z ]*?([A-Za-z]+)::",line).groups()
            rel = re.findall(",(\w[A-Za-z ]*\w)\.",line) 
            if (data not in datas): datas[data]=0
            datas[data]+=1
            seculo= getSeculo(int(data))
            if (seculo not in seculosnomes): seculosnomes[seculo]=({},{})
            if (nome[0] not in seculosnomes[seculo][0]):  seculosnomes[seculo][0][nome[0]]=0
            if (nome[1] not in seculosnomes[seculo][1]):  seculosnomes[seculo][1][nome[1]]=0
            seculosnomes[seculo][0][nome[0]]+=1
            seculosnomes[seculo][1][nome[1]]+=1
            for r in rel:
                if r.lower() not in relacoes: relacoes[r.lower()]=0
                relacoes[r.lower()]+=1

    saida = -1
    while saida != 0:
        print("1-Frequência absoluta de processos por ano")
        print("2-Frequência relativa de processos por ano")
        print("3-Top 5 nomes próprios e apelidos por séculos")
        print("4-Frequência de relações")
        print("5-Converter em JSON")
        print("0-Sair")
        saida = int(input("Introduza a sua opcao-> "))
        if saida == 0:
            print("A sair .....")
        elif saida == 1:
            dataPedida = input("Introduza a data-> ")
            if dataPedida not in datas: print(0)
            else:print(datas[dataPedida])
            input()
        elif saida == 2:
            dataPedida = input("Introduza a data-> ")
            if dataPedida not in datas: print(0)
            else:print(round(datas[dataPedida]/nprocessos,5))
            input()
        elif saida == 3:
            seculo = int(input("Introduza o século desejado-> "))
            print(top5Names(seculosnomes[seculo][0],seculosnomes[seculo][1]))
        elif saida == 4:
            relacao = input("Introduza a relação-> ").lower()
            print(relacoes[relacao])
            input()
        elif saida == 5:
            toJson()
            

if (__name__=="__main__"):
    main()