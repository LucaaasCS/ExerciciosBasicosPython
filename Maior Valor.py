# Recebemos valores do usuário

a = input("Digite um valor: ")
b = input("\nDigite um valor: ")
c = input("\nDigite um valor: ")

# Variáveis auxiliares para representar a posição dos números na exibição

primeira = "" # O maior número
segunda = "" # O número médio
terceira = "" # O menor número

# Comparamos a e b para ver qual das duas é maior e temporariamente definir qual é o maior número

if int(a) > int(b):
  primeira = a
  segunda = b
elif int(b) > int(a):
  primeira = b
  segunda = a

# Comparamos o c com a variável "primeira" porque não sabemos qual é maior entre a e b, e na execução a variável "primeira" já vai representar o maior entre os dois

# Caso a variável c seja menor que a variável "primeira" ela ainda precisa ser comparada com a variável "segunda", pois pode ser menor ou maior que esta

if int(primeira) > int(c) and int(c) > int(segunda):
  terceira = segunda
  segunda = c
elif int(primeira) > int(c) and int(c) < int(segunda):
  terceira = c
  # Se a variável c não for menor que a primeira, ela não precisa ser comparada com mais nenhuma
  # Agora, atribuímos o valor da segunda à terceira, da primeira à segunda, e o c se torna a primeira
  # Fazemos essa atribuição de forma "invertida" porque se fizermos pela ordem tradicional, perderemos os valores importantes (exemplo: se atribuirmos c à primeira, perdemos o antigo valor da primeira)
else:
  terceira = segunda
  segunda = primeira
  primeira = c
  
#elif int(c) > int(a) and int(c) > int)(b):
#  primeira = c

  print(terceira)
  print(segunda)
  print(primeira)
