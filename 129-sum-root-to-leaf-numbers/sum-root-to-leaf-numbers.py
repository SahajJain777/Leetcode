# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):

        def dfs(node,s):
            if not node:
                return 0

            s  = s * 10 + node.val

            if(node.left == None and node.right == None):
                return s
            
            return dfs(node.left,s) + dfs(node.right,s)
        
        return dfs(root,0)


            

            
        