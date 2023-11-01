class Tree:
    def __init__(self, val, index):
        self.val = val
        self.index = index
        self.left = None
        self.right = None

class Solution:
    def sort(self, nums, start, end): #트리 만들기
        if start > end:
            return None
        
        mid = (start + end) 
        node = Tree(nums[mid], mid)
        node.left = self.sort(nums, start, mid - 1)
        node.right = self.sort(nums, mid + 1, end)
        return node

    def search(self, nums, target):
        root = self.sort(nums, 0, len(nums) - 1)
        return self.searchTree(root, target)

    def searchTree(self, node, target):# 인덱스 찾기
        if not node:
            return -1
        
        if node.val == target:
            return node.index
        
        if target < node.val:
            return self.searchTree(node.left, target)
        else:
            return self.searchTree(node.right, target)