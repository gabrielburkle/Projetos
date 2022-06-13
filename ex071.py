total = valor = 0
ced = 50
totalcedulas = 0
valor = int(input('Qual valor deseja sacar? R$ '))
while True:
    if valor >= ced:
        total -= ced
        totalcedulas += 1
    else:
        if totalcedulas > 0:
            print (f'Total de {totalcedulas} cedulas de R$ {ced:.2f}')
        if ced == 50:
            ced == 20
        elif ced == 20:
            ced == 10
        elif ced == 10:
            ced == 1
        totalcedulas = 0
        if total == 0:
            break
print ('Obrigado por sacar conosco')
