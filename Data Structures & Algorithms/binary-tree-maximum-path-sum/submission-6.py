# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = [root.val]
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            ans[0] = max(ans[0],root.val+left+right,root.val+left,root.val+right,root.val);
            return max(root.val,root.val+max(left,right))
        dfs(root)
        return ans[0]
        