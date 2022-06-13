print ('{:=^40}'.format(' LOJAS GABRIELLO '))
preço = float(input('Preço das compras: R$ '))
print ('''FORMAS DE PAGAMENTO
[1] À vista dinheiro / cheque
[2] À vista no cartão
[3] Até 2x no cartão
[4] 3x ou mais no cartão''')
opção = int(input('Digite sua opção: '))
if opção == 1:
    resultado = preço - (preço * 10 / 100)
    print('O valor final com 10% de desconto é R${:.2f}'.format(resultado))
elif opção == 2:
    resultado = preço - (preço * 5 / 100)
    print ('O valor final com 5% de desconto é R${:.2f}'.format(resultado))
elif opção == 3:
    resultado = preço
    parcela = preço / 2
    print('Sua compra será parcelada em 2x de R${:.2f} e custará R${:.2f}'.format(parcela, resultado))
elif opção == 4:
    parcelas = int(input('Em quantas vezes deseja parcelar?'))
    resultado = preço + (preço * 20 / 100)
    parcela = resultado / parcelas
    print ('''Sua compra de R${:.2f} será parcelada em {}x de R${:.2f}, 
    valor total de R${:.2f}'''.format(preço, parcelas, parcela, resultado))
else:
    print ('OPÇÃO INVÁLIDA, TENTE NOVAMENTE')

    
