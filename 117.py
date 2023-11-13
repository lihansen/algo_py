from leetcode import Node

from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # BFS
        if not root:
            return root
        q = deque()
        
        q.append(root)
        
        while q:
            size = len(q)
            startNode = None
            for i in range(size):
                node = q.popleft()
                if startNode:
                    startNode.next = node
                
                startNode = node

                if node.left:
                    q.append(node.left)
                if node.right:
                    
                    q.append(node.right)

        return root
    
class Solution1:
    def connect(self, root):
        if not root:
            return root
        
        father = root
        child_head = Node() # head of linked list of each level 

        while father:
            child = child_head 
            while father :
                if father.left:
                    child.next = father.left 
                    child = child.next

                if father.right:
                    child.next = father.right 
                    child = child.next

                father = father.next

            father = child_head.next
            child_head.next = None 

        return root 
    
    