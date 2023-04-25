from datetime import date
nsc = int(input('Em que ano voce nasceu: '))
atual = date.today().year
idade = atual - nsc
print(f'{idade}')
if idade == 18:
    print(f'Voce precisa se alistar esse ano ')
elif idade > 18:
    saldo = idade - 18
    print(f'já passou o ano de alistamento, foi a {saldo}anos')
elif idade < 16:
    saldo = 18 - idade 
    if saldo == 1:
        print(f'Voce precisa esperar {saldo} ano para se alistar')
    else: 
        print(f'Voce precisa esperar {saldo} anos para se alistar')
