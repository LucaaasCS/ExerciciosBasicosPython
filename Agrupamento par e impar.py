lista = []
lista_par= []
lista_impar= []

def Lista():
  for i in range(1,15):
    num=int(input(f'Digite um número: '))

    lista.append(num)

    if num % 2 == 0:
      lista_par.append(num)

    else: 
      lista_impar.append(num)

  return lista , lista_par, lista_impar

