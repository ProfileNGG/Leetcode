# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def height(self,root):
        if root==None:
            return 0
        return 1+max(self.height(root.left),self.height(root.right))

    def isBalanced(self, root):
        if root == None:
            return 0, True
        lh= self.height(root.left)
        rh= self.height(root.right)
        if lh-rh>1 or rh-lh>1:
            return False
        isleftBalanced = self.isBalanced(root.left)
        isrightBalanced = self.isBalanced(root.right)
        if isleftBalanced and isrightBalanced:
            return True
        return False