#eu estou fazendo um pouco diferente dos proposto
I1= input("Escreva um item para ser adicionado a lista:")
I2= input("Escreva um segundo item para ser adicionado a lista:")
I3= input("Escreva um terceiro item para ser adicionado a lista:")

P1= input("Digite o item que voce procura na lista:")
lista1 = [ I1, I2, I3]

if P1 in lista1:
    
    print("Sim, este item está na lista!")
else:
    print("Não, este item não esta na lista")