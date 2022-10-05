import math

def quad_perfeito(i):

  if math.sqrt(i) - int(math.sqrt(i)) == 0:
      
    print (f'É um quadrado perfeito')
    
  else:
      print(f'Não é um quadrado perfeito')

i = int(input('Digite um número: '))

