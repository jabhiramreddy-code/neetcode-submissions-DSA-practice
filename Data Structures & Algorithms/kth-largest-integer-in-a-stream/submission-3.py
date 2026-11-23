class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
class KthLargest:

    # def insert(self,val,root):
    #     if not root:
    #         return Node(val)
    #     if val<root.val:
    #         root.left = self.insert(val,root.left)
    #     else:
    #         root.right = self.insert(val,root.right)
    #     return root
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.arr = nums

    def add(self, val: int) -> int:
        self.arr.append(val)
        self.arr.sort()
        return self.arr[len(self.arr)-self.k]
        
