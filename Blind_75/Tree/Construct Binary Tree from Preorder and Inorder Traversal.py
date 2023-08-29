# https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
# Problem: 105. Construct Binary Tree from Preorder and Inorder Traversal
# Given two integer arrays preorder and inorder where preorder is the preorder traversal
# of a binary tree and inorder is the inorder traversal of the same tree,
# construct and return the binary tree.
from typing import List


# Example 1:
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]

# Example 2:
# Input: preorder = [-1], inorder = [-1]

# Output: [-1]

# Constraints:
# 1 <= preorder.length <= 3000
# inorder.length == preorder.length
# -3000 <= preorder[i], inorder[i] <= 3000
# preorder and inorder consist of unique values.
# Each value of inorder also appears in preorder.
# preorder is guaranteed to be the preorder traversal of the tree.

# inorder = [9,3,15,20,7]
# preorder = [3,9,20,15,7]


# inorder = [9,3,15,20,7]
# preorder = [3,9,20,15,7]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):

#         self.val = val

#         self.left = left


#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        index = inorder.index(preorder[0])

        # totol num of left subtree in inorder: 0~index, indexing in preorder, 1 ~ index + 1
        root.left = self.buildTree(preorder[1:index+1], inorder[:index])
        # right subtree: preorder: after left subtree, inorder: after root
        root.right = self.buildTree(preorder[index + 1:], inorder[index+1:])
        return root
