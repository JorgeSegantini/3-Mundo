times = 'fluminense', 'bota', 'fort', 'Pal', 'Vasco', 'inter', 'brag', 'flam', 'goias'
#for pos, camp in enumerate(times[:5]):
for cont in range(0, len(times)):      
    print(f'essa é a clacificação {cont} {times[cont]} ')
for cont in range(0, len(times[:5])):
    print(f'Os 5 primeiros colocados são {cont+1} {times[cont]} ')
for pos, time in enumerate(times[-4:]):
    print(f'Os 4 ultimos colocados são {time}')
print('pal'.find in times)

