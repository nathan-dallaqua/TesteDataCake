from time import sleep
arr=[9, 2, 3, 1, 4]
print(f'Os números faltando na array:{arr}são: ')
for n in range (1,9):
    for c in arr:
        if n not in sorted(arr):
            print(n)
            sleep(1)
            break
print()
print('FIM')
