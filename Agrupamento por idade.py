idade = int(input('Digite a idade: '))

if idade < 5:
    print("Bebê")
elif idade >= 5 and idade < 8:
    print("Infantil A")
elif idade < 11:
    print("Infantil B")
elif idade < 14:
    print("Juvenil A")
elif idade < 18:
    print("Juvenil B")
else:
    print("Senior")
