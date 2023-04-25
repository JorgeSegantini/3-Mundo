n1 = float(input('Digite o primereio valor: '))
n2 = float(input('Digite o segundo valor: '))
if n1 > n2:
    maior = n1
    print(f'O maior valor é {maior:.2f}')
elif n2 > n1:
    maior = n2
    print(f'O maior valor é {maior:.2f}')
else:
    print('Não existe valor maior os dois são iguais')