from time import sleep
arr=[9, 2, 3, 1, 4]
novo=[]
print('Os números faltando na array:[9, 2, 3, 1, 4] são: ')
for n in range (1,9):
    for c in arr:
        if n not in sorted(arr):
            print(n)
            sleep(1)
            break
print()
print('FIM')
