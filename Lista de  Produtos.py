nome = [0.0] * 5

preco = [0.0] * 5

nova_lista = [] * 5

for i in range(len(nome)):
    nome[i] = str(input())
    
for x in range(len(preco)):
    preco[x] = float(input())
    a = float(input())
    if a == preco[x]:
        nova_lista[x] += nome[x]

print(f'Os produtos escolhidos foram : {nova_lista}')


