# eu fiz um pouco diferente do propostro, eu tentei deixa melhor do que foi propostro.
F1= input("Escreva um item para ser adicionado a lista de filmes:")
F2= input("Escreva um segundo item para ser adicionado a lista de filmes:")
F3= input("Escreva um terceiro item para ser adicionado a lista de filmes:")
listaF = [ F1, F2, F3]

J1= input("Escreva um item para ser adicionado a lista de jogos:")
J2= input("Escreva um segundo item para ser adicionado a lista de jogos:")
J3= input("Escreva um terceiro item para ser adicionado a lista de jogos:")
listaJ = [ J1, J2, J3]

L1= input("Escreva um item para ser adicionado a lista de livros:")
L2= input("Escreva um segundo item para ser adicionado a lista de livros:")
L3= input("Escreva um terceiro item para ser adicionado a lista de livros:")
listaL = [ L1, L2, L3]

E1= input("Escreva um item para ser adicionado a lista de esportes:")
E2= input("Escreva um segundo item para ser adicionado a lista de esportes:")
E3= input("Escreva um terceiro item para ser adicionado a lista de esportes:")
listaE = [ E1, E2, E3]


le= input("Digite um item que voce que quer procurar nas listas:")

if le in listaF:
    print("Sim, está na lista Filmes!")
else:
    print("Não está na lista Filmes")

if le in listaJ:
    print("Sim, está na lista Jogos!")
else:
    print("Não está na lista Jogos")

if le in listaL:
    print("Sim, está na lista Livros!")
else:
    print("Não está na lista Livros")

if le in listaE:
    print("Sim, está na lista Esportes!")
else:
    print("Não está na lista Esportes")





