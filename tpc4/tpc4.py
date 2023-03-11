import re
import json

file=open("file5.csv")
lines = file.readlines()
groups = re.findall(r"\b([\w]+)(?:{([\d,]+)}(?:::(\w+))?)?\b",lines[0])
print(groups)
objetos=[]
for line in lines[1:]:
    if (line[-1]=="\n"): line=line[:-1]
    words = re.split(",",line)
    objeto = {}
    i=0
    for nome,lista,func in groups:
        word=words[i]
        if(nome):
            if(lista):
                cenas=[]
                for j in range(int(lista[-1])):
                    word=words[i]
                    if(word!=""):
                        cenas.append(int(word))
                    i+=1
                if (func):
                    if(func=="sum"):
                        objeto[nome]=sum(cenas)
                    elif(func=="media"):
                        objeto[nome]=sum(cenas)/len(cenas)
                else: objeto[nome]=cenas           
            else:
                objeto[nome]=word
                i+=1
    print(objeto)
    objetos.append(objeto)
file = open("file.json","w")
json.dump(objetos,file,indent=0,ensure_ascii=False)
file.close()