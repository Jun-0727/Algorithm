def search2DMatrix(matrix: list, target):
    for x in range(len(matrix)):
        if matrix[x][0] > target:
            break

        for y in range(len(matrix[0])):
            if matrix[x][y] == target:
                return True
            
            if matrix[x][y] > target:
                break
    
    return False


# print(search2DMatrix([[1,4,7,11,15], [2,5,8,12,19], [3,6,9,16,22], [10,13,14,17,24]], 20))

def search_matrix(matrix, target):
    return any(target in row for row in matrix)

print(search_matrix([[1,4,7,11,15], [2,5,8,12,19], [3,6,9,16,22], [10,13,14,17,24]], 20))