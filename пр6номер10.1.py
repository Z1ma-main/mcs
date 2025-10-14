a=list(map(int,input("Введите ряд целых чисел").split()))
b=[]
for i in a:
    if a.count(i)>1:
        b.append(i)
if b:
    print("Повторяющиеся эдементы",b)
else:
    print("Повторяющихся элементов нет")
