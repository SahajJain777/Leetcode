# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        if root == None: return 
        curr = root
        while(curr!=None):
            if(curr.left!=None):
                rm = curr.left
                while(rm.right!=None):
                    rm = rm.right
                
                rm.right = curr.right
                curr.right = curr.left
                curr.left = None
            curr = curr.right