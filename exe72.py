numerolista = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezesssete', 'Dezoito', 'Dezenove', 'Vinte')
while True: 
    numero = int(input('Digite um número entre 0 e 20: '))         
    while numero > 20 or numero < 0:
        numero = int(input('Entrada invalida digite outro número entre 0 e 20: '))
    print(f'Eu vou comer {numerolista[numero]}')
    ct = str(input('Deseja continuar [S/N] ')).upper()
    if ct in 'Ss':
        print('vamos continuar')     
    elif ct in 'Nn':
        print('Voce saiu do programa ')
        break         


            

#for numero in numerolista:        
    #print(f'O número que voce digitou é {numerolista[numero]}')

    #if numero in (0, 20):
       # print(f'Você digitou o numero {numerolista[]}')
    #elif numero == 1:
        #print(numerolista[1])
    #else:
        #numero = int(input('Tente novamente.'))
