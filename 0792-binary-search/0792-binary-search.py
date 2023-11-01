class TreeNode:
    def __init__(self, val, index):
        self.val = val
        self.index = index
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums, start, end):
        if start > end:
            return None
        
        mid = (start + end) // 2
        node = TreeNode(nums[mid], mid)
        node.left = self.sortedArrayToBST(nums, start, mid - 1)
        node.right = self.sortedArrayToBST(nums, mid + 1, end)
        return node

    def search(self, nums, target):
        root = self.sortedArrayToBST(nums, 0, len(nums) - 1)
        return self.searchInBST(root, target)

    def searchInBST(self, node, target):
        if not node:
            return -1
        
        if node.val == target:
            return node.index
        
        if target < node.val:
            return self.searchInBST(node.left, target)
        else:
            return self.searchInBST(node.right, target)