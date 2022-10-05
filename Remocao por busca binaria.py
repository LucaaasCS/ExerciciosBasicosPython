import random
lista1= []
lista2= []
lista_final= []
cont = 0

def gerar(cont):
  while cont < 6:
    num = random.randint(1,6)
    lista1.append(num)
    num = random.randint(1,6)
    lista2.append(num)
    cont+= 1
  lista_final = lista1 + lista2
  print (lista_final)
  lista_final.sort()
  print(lista_final)
  ret = int(input(f'Digite um número para retirar da lista: '))
  lista_final.remove(ret)
  print(lista_final)
  return lista_final

def busca_binaria(busca, lista_final):
  inicio = 0
  fim = len(lista_final) - 1
  while inicio <= fim:
      meio = (inicio + fim) // 2

      if busca == lista_final [meio]:
        return meio

      elif busca < lista_final[meio]:
        fim = meio - 1

      else:
            inicio = meio + 1
  return 'Não encontrado'

gerar(cont)
busca = int(input(f'Digite um valor para buscar: '))
print (f'A posição do numero {busca} é {busca_binaria(busca, lista_final)}')
