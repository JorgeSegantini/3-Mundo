from time import sleep
print('S2' * 30)
print('Analisando triangulos')
print('S2' * 30)
c1 = float(input('Digite o comprimento de uma reta: '))
c2 = float(input('Digite o comprimento de uma reta: '))
c3 = float(input('Digite o comprimento de uma reta: '))
sleep(2)
if c1 < c2 + c3 and c2 < c1 + c3 and c3 < c1 + c2:
    print('os segmentos acima PODEM FORMAR um triangulo!')
    if c1 == c2 == c3:
        print('')
    elif c1 != c2 != c3 != c1:
        print('')
    else:
        print('')
else:
    print('Os segmentos acima nao conseguem formar um triangulo!')

print('S2' * 30)