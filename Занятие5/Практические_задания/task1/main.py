if __name__ == "__main__":
    # матрица или таблица это список строк,
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    for row_index in range(len(matrix)):  # перебираем все индексы строк
        for col_index in range(len(matrix[row_index])):
            print(matrix[row_index][col_index], end=" ")
        print()
