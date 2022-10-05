salario = float(input('Digite o salario: '))
tempo_casa = int(input('Digite o tempo de casa: '))

if tempo_casa >= 5:
    bonus = salario * 20 / 100
    print(f'O bonus é R$ {bonus:.2f}')
else:
    bonus = salario * 10 / 100
    print(f'O bonus é R$ {bonus:.2f}')
