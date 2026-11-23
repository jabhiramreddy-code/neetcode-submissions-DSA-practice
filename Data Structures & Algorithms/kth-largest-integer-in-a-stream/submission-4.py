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
        self.minheap = nums
        heapq.heapify(self.minheap)
        while len(self.minheap)>k:
            heapq.heappop(self.minheap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minheap,val)
        while len(self.minheap)>self.k:
            heapq.heappop(self.minheap)
        return self.minheap[0]
        
