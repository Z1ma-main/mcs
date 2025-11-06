M, N = map(int, input("Введите размеры матрицы (M N): ").split())
matrix = [list(map(int, input("Введите строку: ").split())) for i in range(M)]
k_index = int(input("Введите номер строки для сортировки")) - 1
sorted_indices = sorted(range(N), key=lambda j: matrix[k_index][j])
sorted_matrix = [[matrix[i][j] for j in sorted_indices] for i in range(M)]
print("Отсортированная матрица")
for row in sorted_matrix:
    print(' '.join(map(str, row)))
