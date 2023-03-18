import re

flag=0
saldo=0
moedasvalidas=["1c","2c","5c","10c","20c","50c","1e","2e"]
while True:
    linha=input()
    if(flag):
        if re.match("(?i:MOEDA)",linha):
            moedas = re.findall(r"\d+[ce]",linha)
            for moeda in moedas:
                if moeda in moedasvalidas:
                    if(moeda[-1]=="c"): saldo+=int(moeda[:-1])
                    elif(moeda[-1]=="e"): saldo+=int(moeda[:-1])*100
                else:
                    print(f"{moeda} - moeda inválida; ")
            print(f"saldo = {int(saldo/100)}e{saldo%100}c")
        elif re.match("(?i:POUSAR)",linha):
            print(f"troco = {int(saldo/100)}e{saldo%100}c; Volte sempre!")
            flag=0
            saldo=0
        elif re.match("(?i:ABOrtar)",linha):
            flag=0
            saldo=0
        elif re.match("(?i:t=)",linha):
            numero = re.search(r'[^(601|641)](\d{9}|00\d+)$',linha).group(1)
            if(numero):
                if re.match(r"00",numero):
                    if(saldo<150):
                        print("Saldo insuficiente.")
                    else:
                        saldo-=150
                elif numero[0]=="2":
                    if(saldo<25):
                        print("Saldo insuficiente.")
                    else:
                        saldo-=25
                elif re.match(r"808",numero):
                    if(saldo<10):
                        print("Saldo insuficiente.")
                    else:
                        saldo-=10
                print(f"Saldo = {int(saldo/100)}e{saldo%100}c")
            else:
                print("Esse número não é permitido neste telefone. Queira discar novo número!")     
    else:
        if re.match("(?i:levantar)",linha):
            flag=1
            print("Introduza moedas.")