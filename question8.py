rows=columns=2
matrix=[[0 for i in range(columns)] for j in range(rows)]
matrix[0][0]=1
matrix[0][1]=2
matrix[1][0]=3
matrix[1][1]=4
for i in range(rows):
    for j in range(columns):
        print(matrix[j][i],end=' ')
    print()

