# https://leetcode.cn/problems/word-search/description/

# Problem: 79. Word Search

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = set()
        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == word[0]:
                    path.add((y,x))
                    if self.dfs(path, board, word, 0, y, x):
                        return True
                    path.remove((y,x))
        return False


    def dfs(self, path, board ,word, idx, i, j):
        if board[i][j] == word[idx]:
            if idx == len(word)-1:
                return True
            else:
                for pos in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if 0 <= pos[0] < len(board) and 0 <= pos[1] < len(board[0]) and pos not in path:
                        path.add(pos)
                        if self.dfs(path, board, word, idx + 1, pos[0], pos[1]):
                            return True
                        path.remove(pos)
        else:
            return False