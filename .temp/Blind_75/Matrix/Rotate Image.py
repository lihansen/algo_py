# https://leetcode.cn/problems/rotate-image/description/

# Problem: 48. Rotate Image

# flip diagonally and then reverse each row
# same effect as rotate 90 degree clockwise
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i < j:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if j < len(matrix[i]) // 2:
                    matrix[i][j], matrix[i][- j -1] = matrix[i][- j -1], matrix[i][j]
