lanche = ('Hamburger', 'Suco', 'pizza', 'Pudim')
#lanche[2] = 'sucodelanranja'
for comida in lanche:
    print(f'Eu vou comer {comida}')
#print(lanche[2]) 
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print(sorted(lanche))
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b #Ordem importa
print(c)
print(len(c))
c.count(5) #Mostra quantas desse numero tem nessa Tupla
c.index(8) #Mostra a posição
c.index(5, 1) #Deslocamento
pessoa = (1, 2, 'M', 4, 'Jorge', 6.56)
del()#Apagar a Tupla inteira