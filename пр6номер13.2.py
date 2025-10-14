a=list(map(int,input("Введите 8 элементов массива").split()))
if len(a)==8:
    b=[]
    for i in a:
        if i<15:
            b.append(i*i)
        else:
            b.append(i)
    print("Преобразованный массив",b)
else:
    print("Введите 8 чисел")
