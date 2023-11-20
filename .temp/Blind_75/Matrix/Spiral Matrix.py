# https://leetcode.cn/problems/spiral-matrix/description/

# Problem: 54. Spiral Matrix


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        a = matrix
        left = 0
        right = len(a[0]) - 1
        up = 0
        bottom = len(a) - 1
        i = 0
        j = 0
        f = lambda: len(res) < len(a[0]) * len(a) # indexing from 0

        while f():

            while f():
                res.append(a[up][j])
                if j != right:
                    j += 1
                else:
                    i += 1
                    up += 1
                    break

            while f():
                res.append(a[i][right])
                if i != bottom:
                    i += 1
                else:
                    j -= 1
                    right -= 1
                    break

            while f():
                res.append(a[bottom][j])
                if j != left:
                    j -= 1
                else:
                    i -= 1
                    bottom -= 1
                    break

            while f():
                res.append(a[i][left])
                if i != up:
                    i -= 1
                else:
                    j += 1
                    left += 1
                    break

        return res

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            res += matrix.pop(0)
            matrix = list(zip(*matrix))[::-1]
        return res