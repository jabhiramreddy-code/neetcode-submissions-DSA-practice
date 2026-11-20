# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([root])
        ans = []
        while  q:
            l = len(q)
            right = None
            for i in range(l):
                temp = q.popleft();
                if temp:
                    right = temp
                    q.append(temp.left)
                    q.append(temp.right)
            if right:
                ans.append(right.val)
        return ans

        