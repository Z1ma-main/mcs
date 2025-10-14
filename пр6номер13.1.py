a=list(map(int,input("Введите элементы массива").split()))
d=[]
p=[]
for s in a:
    if a.count(s)>1:
        p.append(s)    
for i in range(len(a)):
    if a.count(a[i])>1:
        d.append(i)
print("Повторяющиеся числа",p)
print("Индексы повторяющихся чисел",d)
