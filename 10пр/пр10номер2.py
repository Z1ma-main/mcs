with open("АсеевЕвгенийЮрьевич_УБ-51_2_vvod.txt", "r") as file:
    M, N = map(int, file.readline().split())
    
    matrix = []
    for i in range(M):
        row = list(map(int, file.readline().split()))
        matrix.append(row)
    k_index = int(file.readline()) - 1

sorted_indices = sorted(range(N), key=lambda j: matrix[k_index][j])
sorted_matrix = [[matrix[i][j] for j in sorted_indices] for i in range(M)]

with open("АсеевЕвгенийЮрьевич_УБ-51_2_vivod.txt", "w") as file:
    file.write("Исходная матрица:\n")
    for row in matrix:
        file.write(' '.join(map(str, row)) + '\n')
    
    file.write(f"\nСтрока для сортировки (№ {k_index + 1}): {' '.join(map(str, matrix[k_index]))}\n")
    
    file.write("\nОтсортированная матрица:\n")
    for row in sorted_matrix:
        file.write(' '.join(map(str, row)) + '\n')
