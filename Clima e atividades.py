faz_sol = input(f'Irá fazer sol?S/N: ').upper() == 'SIM!'
feriado =  input(f'Será feriado?S/N: ').upper() == 'SIM!'

def analisar(faz_sol, feriado):
  if (faz_sol and feriado):

    print (f'Vá para praia!')

  elif (faz_sol and not (feriado)):

    print (f'Passear no taquaral')

  elif (not (faz_sol) and feriado):

    print (f'Assistir filme!')

  else:

    print (f'Ler um livro!')
