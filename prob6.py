def mAritmetica (val1, val2, val3):
    soma = val1 + val2 + val3
    media = soma/3
    return media

#Os pesos foram previamente arbitrados
def mPonderada  (val1, val2, val3):
    media = (val1*1 + val2*2 + val3*3)/6 
    return media

def mHarmonica (val1, val2, val3):
    media = 3/(1/val1 + 1/val2 + 1/val3)
    return media

tipoDeMedia =  input("Qual tipo de media você deseja utilizar?")
if tipoDeMedia == "aritmetica":
    entrada1 = float(input("Digite o primeiro número: "))
    entrada2 = float(input("Digite o segundo número: "))
    entrada3 = float(input("Digite o terceiro número: "))
    mediaA = mAritmetica (entrada1, entrada2, entrada3)
    print("A média aritmética desses números é {}.".format(mediaA))
    
elif tipoDeMedia == "harmonica":
    entrada1 = float(input("Digite o primeiro número: "))
    entrada2 = float(input("Digite o segundo número: "))
    entrada3 = float(input("Digite o terceiro número: "))
    mediaH = mHarmonica (entrada1, entrada2, entrada3)
    print("A média harmônica desses números é {}.".format(mediaH))
    
elif tipoDeMedia == "ponderada":
    entrada1 = float(input("Digite o primeiro número: "))
    entrada2 = float(input("Digite o segundo número: "))
    entrada3 = float(input("Digite o terceiro número: "))
    mediaP = mPonderada (entrada1, entrada2, entrada3)
    print("A média ponderada desses números é {}.".format(mediaP))
    