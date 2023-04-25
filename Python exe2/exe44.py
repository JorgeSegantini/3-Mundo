#produto, preço e condição de pagamento.
print(f'{" Loja do Seu Jorge ":=^40}')
pre = float(input('Qual é o preço do produto? '))
cond = int(input('''\033[44m
[ 1 ] À vista 
[ 2 ] À vista cartão
[ 3 ] 2x no cartao
[ 4 ] 3x no cartaoo
Selecione a forma de pagamento:\033[m'''))
if cond == 1:
    print(f'O valor total da compra é R${pre - (pre * 0.10)}')
elif cond == 2:
    valor = pre 
    print(f'O valor da sua compra é R${valor}')
elif cond == 3:
    valor = pre + (pre * (10 / 100))
    par = int(input('Em quantas vez deseja pagar? '))  
    vp = valor / par    
    print(f'Sua compra será parcelada em {par}x de {vp:.2f} com juros')
    print(f'sua compra de R${pre} vai custar R${valor:.2f} no final.')
elif cond == 4:
    valor = pre + (pre * (20 / 100))
    par = int(input('Em quantas vez deseja pagar? '))
    vp = valor / par
    print(f'Sua compra será parcelada em {par}x de {vp:.2f} com juros')
    print(f'sua compra de R${pre} vai custar R${valor:.2f} no final.')
else: 
    total = 0 
    print('\033[36m Opção invalida de pagamento tente outra vez\033[m')
    
