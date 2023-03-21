from time import sleep

sim=[]
arr=[1, 15, 2, 7, 2, 5, 7, 1, 4]
print(f'Esté é o array informado:{arr}')
sleep(1.5)


#Adicionar os valores nesta nova lista
nova=[]

#Informar o valor desejado
valor=int(input('Informe o argumento para ser somado: '))


#Adicionando os números na nova lista
for n in arr:
    nova.append([n])

#Realizando o cálculo
for x in range (0,9):
    for c in range (0,9):
        if sum(nova[x] + nova[c]) == valor:
            sim.append(+1)
            break
if len(sim) > 0:
    sim = True
else:
    sim = False
print(sim)