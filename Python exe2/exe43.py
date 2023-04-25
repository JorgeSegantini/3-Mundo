# calcuylo do imc
alt = float(input('Qual é sua altura? '))
peso = float(input('Qual é seu peso? '))
imc = peso / (alt * alt)
print(f'{imc}')
if imc < 18.5:
    print(f'Seu imc é {imc} e voce esta abaixo do peso')
elif 18.5 <= imc < 25:
    print((f'Seu imc é {imc} e voce esta com o peso ideal'))
elif imc > 25 or imc <= 30:
    (f'Seu imc é {imc} e voce esta com sobrepeso')
elif imc > 30 or imc <= 40:
    (f'Seu imc é {imc} e voce esta com obesidade')
elif imc > 40 :
    (f'Seu imc é {imc} e voce esta com obesidade mórbida')
