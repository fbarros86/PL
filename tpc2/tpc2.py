def getNumber(linha,i):
    j=i+1
    while(j<len(linha) and linha[j].isdigit()): j+=1
    return j-1,int(linha[i:j])


def main():
    linha = input()
    soma = 0
    on = True
    while(linha):
        i=0
        lLinha = len(linha)
        while i<lLinha:
            if on:
                if linha[i].isdigit():
                    i,num=getNumber(linha,i)
                    soma+=num
                elif i<lLinha-2 and linha[i:i+3].lower()=="off":
                    on = False
                    i+=2
                elif linha[i]=="=":
                    print(soma)
            else:
                if i<lLinha-1 and linha[i:i+2].lower()=="on":
                    on = True
                    i+=1
                elif linha[i]=="=":
                    print(soma)
            i+=1
        linha=input()
                        
    
if (__name__=="__main__"):
    main()