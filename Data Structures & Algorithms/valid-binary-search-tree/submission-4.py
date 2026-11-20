# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = [(root,TreeNode(float('-inf')),TreeNode(float('inf')))]
        while stack:
            temp,x,y = stack.pop()
            if temp.left:
                if temp.val > temp.left.val and x.val < temp.left.val:
                    stack.append((temp.left,x,temp))
                else:
                    return False
            if temp.right:
                if temp.val < temp.right.val and y.val > temp.right.val:
                    stack.append((temp.right,temp,y))
                else:
                    return False

        return True