with open("АсеевЕвгенийЮрьевич_УБ-51_vvod.txt", "r") as file:
    matrix=[]
    for line in file:
        muy=[int(x) for x in line.split()]
        matrix.append(muy)


def is_sorted(r):
    return r == sorted(r) or r == sorted(r, reverse=True)

maxe = None
for r in matrix:
    if is_sorted(r):
        mi = max(r)
        if maxe is None or mi > maxe:
            maxe = mi


with open("АсеевЕвгенийЮрьевич_УБ-51_vivod.txt", "w") as file:
    file.write("Исходная матрица:\n")
    for muy in matrix:
        file.write(" ".join(str(x) for x in muy) + "\n")

        
    if maxe is not None:
        file.write(f"\nМаксимальный элемент из отсортированных строк: {maxe}\n")
    else:
        file.write("\nНет отсортированных строк.\n")
