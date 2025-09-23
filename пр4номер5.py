n=int(input("Введие натуральное число n"))
sum=0
for i in range(1,n+1):
    sum+=i**3
print('Сумма кубов',sum)
