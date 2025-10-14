a=list(map(int,input("Введите 15 чисел/цифр").split()))
an=[]
for i in a:
    if i <10:
        an.append(0)
    if i>20:
        an.append(1)
print("Исходный массив:",a)
print("Преобразованный массив:", an)
