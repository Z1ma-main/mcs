def f(a, b):
    if a < b:
        return a
    return f(a - b, b)
a = int(input("Введите число а"))
b = int(input("Введите b>0 "))
print("Остаток от деления a на b", f(a, b))
