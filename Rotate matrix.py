

def rotate_the_matrix(matrix):
    rotate_matrix = []
    for i in range(len(matrix)):
        sub_matrix = []
        for item in matrix:
            sub_matrix.append(item[i])
        rotate_matrix.append(sub_matrix[: : -1])
    return rotate_matrix










#You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

#You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
# DO NOT allocate another 2D matrix and do the rotation.

if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(rotate_the_matrix(matrix))