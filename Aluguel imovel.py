salario_ana = float(input())
salario_mario = float(input())
imovel_fiador = float(input())
if (salario_ana + salario_mario) < 5000 or imovel_fiador <= 650000:
    print('Não podem alugar o imóvel')
else:
    print('Podem alugar o imóvel')
