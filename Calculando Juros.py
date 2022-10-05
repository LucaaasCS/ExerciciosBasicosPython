cod_cliente = 1

while cod_cliente > 0:
    
    cod_cliente = int(input())
    
    if cod_cliente <= 0:
        break
    
    tipo_conta = int(input())
    
    valor_investido = float(input())
    
    if tipo_conta == 1:
        
        print (f'Valor investido R$ {valor_investido:.2f} e Juros: R$ {(valor_investido * 1.5) / 100:.2f}')
    
    elif tipo_conta == 2:
        
        print (f'Valor investido R$ {valor_investido:.2f} e Juros: R$ {(valor_investido * 2) / 100:.2f}')
   
    elif tipo_conta == 3:
        
        print (f'Valor investido R$ {valor_investido:.2f} e Juros: R$ {(valor_investido * 4) / 100:.2f}')
