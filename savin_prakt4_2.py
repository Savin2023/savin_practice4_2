print("Введите натуральное число")
n=int(input())
kolvo=0
for i in range(n):
    if n%(i+1)==0:
        kolvo+=1

print("Результат вычислений:",kolvo*2000000000)


