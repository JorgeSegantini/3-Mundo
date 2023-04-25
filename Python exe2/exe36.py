vlc = float(input('Qual é o valor da casa que deseja comprar? '))
sal = float(input('Qual é o valor so seu salário? '))
ano = float(input('Em quantos anos voce deseja pagar? '))
mes = ano * 12
salm = sal * mes
if vlc < salm * 0.3: 
    print('seu emprestimo foi aprovado!')
else:
    print('Desculpe mas sua solicitação de emprestimo foi negada!')

