n=int(input('Введите число n'))
k=int(input('Введите число k'))
a=0
b=1
i=1
sum=0
while n>0:
    if i >=k:
        sum+=a
        n-=1
    a,b=b,a+b
    i+=1
print(sum)
