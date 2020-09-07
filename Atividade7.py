# eu fiz um pouco diferente do propostro, eu tentei deixa melhor do que foi propostro.
Fonte= input("Escreva o nome da sua fonte desejada:")
Processador= input("Escreva o nome do Processor desejado :")
Gabinete= input("Escreva o nome do gabinite desejado :")
Ram = input("Escreva o o modelo da memória ram desejada :")
Hd = input("Escreva o nome do HD (disco rigido) desejado :")
Placamae= input("Escreva o nome da placa mãe desejada :")
Placavideo= input("Escreva o nome da placa de vídeo desejada :")
Placasom= input("Escreva o nome da placa de som desejada:")

Componentes = [ Fonte, Processador, Gabinete, Ram , Hd, Placamae, Placavideo, Placasom]

print("Esses são os componentes escolhidos: ", Componentes)

retira= int(input("Voce deseja retirar algum componete, digite 1 para sim e 0 para não: "))


if retira > 0:
    item = input("Escreva o item que deseja retirar: ")
    Componentes.remove(item)
    retira2= int(input("Deseja remover outro item, digite 1 para sim e 0 para não: "))
    
    if retira2 > 0:
        item = input("Escreva o item que deseja retirar: ")
        Componentes.remove(item)
    else:
        print("Compra Finalizada: ")      

else:
    print("Compra Finalizada")

print("Esses são os componentes escolhidos: ", Componentes)

