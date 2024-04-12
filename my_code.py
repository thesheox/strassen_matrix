def partition_matrix(matrix):
    n = len(matrix)
    mid = n // 2
    top_left=[row[:mid] for row in matrix[:mid]]
    top_right = [row[mid:] for row in matrix[:mid]]
    bottom_left = [row[:mid] for row in matrix[mid:]]
    bottom_right = [row[mid:] for row in matrix[mid:]]
    return top_left, top_right, bottom_left, bottom_right
    print(top_left)
    print(top_right)
    print(bottom_left)
    print(bottom_right)




def add_matrix(matrix_1, matrix_2):

    n = len(matrix_1)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(len(matrix_1[0])):
            result[i][j] = matrix_1[i][j] + matrix_2[i][j]

    return result


def sub_matrix(matrix_1, matrix_2):

    n = len(matrix_1)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(len(matrix_1[0])):
            result[i][j] = matrix_1[i][j] - matrix_2[i][j]

    return result

def get_matrix_dimensions(matrix):
    return len(matrix), len(matrix[0])
def default_matrix_multiplication(a, b):
    """
    Only for 2x2 matrices
    """
    if len(a) != 2 or len(a[0]) != 2 or len(b) != 2 or len(b[0]) != 2:
        raise Exception('Matrices should be 2x2!')
    new_matrix = [[a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]],
                  [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]]]

    return new_matrix

result = [[0] * 2 for _ in range(2)]
def strassen(matrix_a,matrix_b):
    if get_matrix_dimensions(matrix_a) == (2, 2):
        return default_matrix_multiplication(matrix_a, matrix_b)
    a11,a12,a21,a22=partition_matrix(matrix_a)
    b11,b12,b21,b22=partition_matrix(matrix_b)
    m1=strassen(add_matrix(a11,a22),add_matrix(b11,b22))
    m2=strassen(add_matrix(a21,a22),b11)
    m3=strassen(a11,sub_matrix(b12,b22))
    m4=strassen(a22, sub_matrix(b21, b11))
    m5=strassen(add_matrix(a11,a12),b22)
    m6=strassen(sub_matrix(a21,a11),add_matrix(b11,b12))
    m7=strassen(sub_matrix(a12, a22), add_matrix(b21, b22))

    result[0][0] = add_matrix(sub_matrix(add_matrix(m1, m4), m5),m7)
    result[0][1] = add_matrix(m3, m5)
    result[1][0] = add_matrix(m2, m4)
    result[1][1] = add_matrix(sub_matrix(add_matrix(m1, m3), m2),m6)

    return result




A = [[1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]]

B = [[17, 18, 19, 20],
    [21, 22, 23, 24],
    [25, 26, 27, 28],
    [29, 30, 31, 32]]

matrix_A = [[4, 6],
            [12, 14]]

matrix_B = [[36, 38],
            [44, 46]]



#print(strassen(matrix_A,matrix_B))
javab=strassen(A,B)
for i in javab:
    print(i)
