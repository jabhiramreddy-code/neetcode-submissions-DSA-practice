# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        a =[0,-1]
        def dfs(root):
            if not root:
                return root;
            dfs(root.left)
            a[0]+=1
            if a[0] == k:
                a[1] = root.val
            # print(root.val)
            dfs(root.right)
        dfs(root)
        return a[1]