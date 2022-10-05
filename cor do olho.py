cont_idade = 0

cont_azul = 0

cont_altura = 0

for cont in range (1, 21):
    print(f'\n==== DADOS PESSOAIS ====')

    idade = int(input(f'Digite a idade: ')).lower
    
    peso = float(input(f'Digite o peso: ')).lower

    altura = float(input(f'Digite a altura: ')).lower

    cor_olhos = input(f'Digite  a cor dos olhos: ').lower

    while cor_olhos != 'castanho' or cor_olhos != 'azul' or cor_olhos != 'preto' or cor_olhos != 'verde':

        print (f'Digite uma cor para olhos válida!')
        
        cor_olhos = input(f'Digite  a cor dos olhos: ').lower

    if idade > 50 and peso < 60:
      cont_idade += 1

    if cor_olhos == 'azul':
      cont_azul+= 1
    
    if altura > 1.65 and cor_olhos != 'verde':
      cont_altura += 1


print (f'A quantidade de pessoas com idade superior a 50 anos e peso inferior a 60 quilos e de {cont_idade}')

print(f'A porcentagem de pessoas com olhos azuis entre todas as pessoas analisadas e de {(cont_azul*100)/20}')

print (f'A quantidade de pessoas com altura acima de 1,68 m e que não possuem olhos verdes e de {cont_altura}')
