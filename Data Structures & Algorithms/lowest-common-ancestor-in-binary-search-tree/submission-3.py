# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        stack = [root]
        while stack:
            temp = stack.pop()
            if (p.val<=temp.val and q.val>=temp.val) or (p.val>=temp.val and q.val<=temp.val):
                return temp;
            if (p.val>temp.val and q.val>temp.val):
                stack.append(temp.right)
            else:
                stack.append(temp.left)
