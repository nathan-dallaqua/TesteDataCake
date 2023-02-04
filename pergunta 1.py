from time import sleep
#Array solicitada
numeros=[2, 1, 5, 2, 5, 2, 1, 1, 1, 7, 9, 13, 127, 21]

#Lista que irá receber os números 1 retirados
um=[]


#Apresentando os números na tela
print(f'''Os números listados são:
{numeros}''')
sleep(1)

#Ler a lista e retirar todos os numeros 1
for n in numeros:
  if n == 1:
    numeros.remove(1)
    um.append(1)

#Adiciona-los denovo no início
for n in um:
  numeros.insert(0,1)



#Resultado final
print(' ')
print(f'''Ordenando apenas o número 1 na array temos:
{numeros}
''')