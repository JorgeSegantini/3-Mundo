
num = int(input('Escreva um numero inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print(f'{num} convertido para Binário é igual a {bin(num)[2:]}')
elif opcao == 2:
    print(f'{num} convertido pra Octal é igual a {oct(num)[2:]}')
elif opcao == 3:
    print(f'{num} convertido para Hexadecimal é igual a {hex(num)[2:]}')
else:
    print('Opção invalida')
