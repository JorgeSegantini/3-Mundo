#Tuplas
lanche = 'burger'
lanche = 'suco' #Elimina o burger 
lanche = 'burger, suco, pizza, pudin' #Variavel composta  

#1-Tuplas 2-Lista 3-Dicionario
#Elementos são indicados por indice 0,1,2...

print(lanche[2]) #Mostra a pizza
print(lanche[0:2]) #Mostra 0 e 1 
print(lanche[1:]) #Começa no 1 e vai até o fim
print(lanche[-1]) #-1 == pudin 
len(lanche) #Mostra o comprimento

for c in lanche:
    print(c) #Vai imprimir os lanches na ordem 
#"As tuplas são imutáveis"

