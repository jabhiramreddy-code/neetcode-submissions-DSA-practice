class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
class KthLargest:

    def insert(self,val,root):
        if not root:
            return Node(val)
        if val<root.val:
            root.left = self.insert(val,root.left)
        else:
            root.right = self.insert(val,root.right)
        return root
    def __init__(self, k: int, nums: List[int]):
        self.root= None
        self.k = k
        for i in nums:
            self.root = self.insert(i,self.root)

    def add(self, val: int) -> int:
        if not self.root:
            self.root = self.insert(val,self.root);
        else:
            self.insert(val,self.root);
        k = self.k
        a = [-1111111]
        def dfs(root):
            if self.k == 0:
                return None
            if not root:
                return None
            # print(root.val)
            dfs(root.right)
            self.k -= 1
            if self.k == 0:
                a[0] = root.val
            dfs(root.left)
        dfs(self.root)
        self.k = k
        return a[0]
        
