from time import sleep
#Array solicitada
arr=[2, 1, 5, 2, 5, 2, 1, 1, 1, 7, 9, 13, 127, 21]

#Lista que irá receber os números 1 retirados
num1=[]


#Apresentando os números na tela
print(f'''Os números listados são:
{arr}''')
sleep(1)

#Ler a lista e retirar todos os numeros 1
for n in range(0,14):
  if 1 in arr:
    arr.remove(1)
    num1.append(1)

#Adiciona-los denovo no início
for n in num1:
  arr.insert(0,1)



#Resultado final
print(' ')
print(f'''Ordenando apenas o número 1 na array temos:
{arr}
''')