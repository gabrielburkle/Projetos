from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
jogador = int(input('''Escolha sua jogada
[0] Pedra
[1] Papel
[2] Tesoura
'''))
print ('JO')
sleep(1)
print ('KEN')
sleep(1)
print ('PO!!!')
print ('-='*11)
print ('Jogador escolheu {}'.format(itens[jogador]))
print ('O computador escolheu {}'.format(itens[computador]))
print ('-='*11)
if computador == 0: #PEDRA#
    if jogador == 0: #PEDRA#
        print ('EMPATE!')
    elif jogador == 1: #PAPEL#
        print ('VOCÊ VENCEU!')
    elif jogador == 2: #TESOURA#
        print ('O COMPUTADOR VENCEU!')

elif computador == 1: #PAPEL#
    if jogador == 0: #PEDRA#
        print('O COMPUTADOR VENCEU!')
    elif jogador == 1: #PAPEL#
        print('EMPATE!')
    elif jogador == 2: #TESOURA#
        print('VOCÊ VENCEU!')

elif computador == 2: #TESOURA#
    if jogador == 0: #PEDRA#
        print ('VOCÊ VENCEU!')
    elif jogador == 1: #PAPEL#
        print ('O COMPUTADOR VENCEU!')
    elif jogador == 2: #TESOURA#
        print ('EMPATE!')

else:
    print ('OPÇÃO INVÁLIDA, TENTE NOVAMENTE')
