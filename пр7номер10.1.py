def count_numbers_from_digits(N,a,b,c):
    c=0
    for x in range(100,N+1):
        s=str(x)
        if all( h==str(a) or h==str(b) or h==str(c) for h in s):
            c+=1
    return c
N=int(input("Введите число N (210<N<231)"))
if not(210<N<231):
    print ("N должно быть в диапазоне 210<N<231")
a=int(input("Введите цифру от 0 до 9"))
b=int(input("Введите цифру от 0 до 9"))
c=int(input("Введите цифру от 0 до 9"))
r=count_numbers_from_digits(N,a,b,c)
print("Количество подходящих чисел",r)

