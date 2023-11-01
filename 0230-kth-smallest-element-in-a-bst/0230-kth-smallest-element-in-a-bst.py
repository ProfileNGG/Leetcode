# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.k = k # 전역변수로 재귀하면서도 변수 유지
        self.kth = 0
        self.find(root)
        return self.kth
        
    def find(self, root): # 노드 순회하면서 몇번인지 확인
        if not root:
            return
        self.find(root.left)
        self.k -= 1
        if self.k == 0:
            self.kth = root.val
            return
        self.find(root.right)