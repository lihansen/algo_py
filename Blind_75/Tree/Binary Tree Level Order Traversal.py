# https://leetcode.cn/problems/binary-tree-level-order-traversal/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        self.helper(res, 0, root)
        return res


    def helper(self, res, level, root):
        if root:
            if level >= len(res):
                res.append([root.val])
            else:
                res[level].append(root.val)
            if root.left:
                self.helper(res, level +1, root.left)
            if root.right:
                self.helper(res, level +1, root.right)



