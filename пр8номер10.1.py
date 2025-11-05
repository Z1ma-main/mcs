def is_sorted(r):
    return r==sorted(r) or r==sorted(r, reverse=True)
rs = int(input("Введите количество строк матрицы: "))
matrix = []
for i in range(rs):
    ri= input("Введите элементы строки: ")
    r= list(map(int, ri.split()))
    matrix.append(r)
maxe= None
for r in matrix:
    if is_sorted(r):
        mi = max(r)
        if maxe is None or mi > maxe:
            maxe = mi
if maxe is not None:
    print("Максимальный элемент из отсортированных строк:", maxe)
else:
    print("Нет отсортированных строк.")
