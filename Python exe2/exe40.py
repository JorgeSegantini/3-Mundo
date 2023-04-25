n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
med = (n1 + n2) / 2
if med < 5:
    print('Voce foi REPROVADO')  
elif med >= 5 and med <= 6.99:
    print('Voce esta de recuperação!')
elif med >= 7:
    print('Voce foi aprovado')
print(f'Sua média é {med}')    