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
        
        mid = (start + end) // 2 #중간 (이걸 안놔누면 연결 리스트로 만들 수 있음)
        node = Tree(nums[mid], mid) #중간 번호로 노드만들기 
        node.left = self.sort(nums, start, mid - 1)# l child 미드를 1 빼서 엔드에 넣음
        node.right = self.sort(nums, mid + 1, end)# r child 미드를 1 더해서 스타트에 넣음
        return node

    def search(self, nums, target): # 실행하는 함수
        root = self.sort(nums, 0, len(nums) - 1)
        return self.searchTree(root, target) #루트랑 타겠을 인자로 넣음

    def searchTree(self, node, target):# 인덱스 찾기
        if not node:
            return -1
        
        if node.val == target: #밸류가 타겟이랑 같으면 인덱스 리턴
            return node.index
        
        if target < node.val: # 타겟이 더 작으면 l차일드로 찾고 크면 r차일드 찾기
            return self.searchTree(node.left, target)
        else:
            return self.searchTree(node.right, target)