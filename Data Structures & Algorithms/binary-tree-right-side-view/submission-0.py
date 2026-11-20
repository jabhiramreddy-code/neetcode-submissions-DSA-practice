# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([root])
        store = []
        while  q:
            l = len(q)
            storetemp = []
            for i in range(l):
                temp = q.popleft();
                if temp:
                    storetemp.append(temp.val)
                    q.append(temp.left)
                    q.append(temp.right)
            if storetemp:
                store.append(storetemp)
        ans = []
        for i in store:
            ans.append(i[len(i)-1])
        return ans

        