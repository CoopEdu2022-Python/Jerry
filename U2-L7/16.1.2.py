def matrix_diagonal_sum(matrix: list[list[int]]) -> int:
    x = []

    for _ in range(0,len(matrix)):
        x.append(matrix[_][_])
    for i in range(0,len(matrix)):
        x.append(matrix[len(matrix)-1-i][len(matrix)-1-i])
    if len(matrix) % 2 == 1:
        j =  len(matrix) // 2
        c = -(matrix[j][j])
        x.append(c)
        print(sum(x))
    else:print(sum(x))

matrix_diagonal_sum([[1,2,3],
                 [4,5,6],
                 [7,8,9]])