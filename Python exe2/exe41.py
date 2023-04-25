from datetime import date
ano = int(input('Em qual ano voce nasceu: '))
idade = date.today().year - ano
mir = idade <= 9
inf = idade > 9 and idade <= 14
jun = idade >= 14 and idade <19
sen = idade >= 19 and idade <=20 
mas = idade > 20
if mir:
    print('Voce é da categoria Mirin')
elif inf:
    print('Voce é da categoria Infantil')
elif jun:
    print('Voce é da categoria Junior')
elif sen:
    print('Voce é da categoria Senior')
elif mas:
    print('Voce é da categoria Master')