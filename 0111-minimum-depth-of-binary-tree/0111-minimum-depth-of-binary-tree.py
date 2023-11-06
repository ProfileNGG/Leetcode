# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        '''if root==None:
            return 0
        if root.left==None and root.right==None:
            return 1
        if root.left==None:
            return self.minDepth(root.right)+1
        if root.right==None:
            return self.minDepth(root.left)+1
        lh=self.minDepth(root.left)
        rh=self.minDepth(root.right)
        return 1+min(lh,rh)'''
        st=[root]
        t=1
        if root==None:
            return 0
        while st:
            for i in range(len(st)):
                curr=st.pop(0)
                if curr.left==None and curr.right==None:
                    return t
                if curr.left:
                    st.append(curr.left)
                if curr.right:
                    st.append(curr.right)
            t=t+1
    
        