/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    int res;
    public int maxPathSum(TreeNode root) {
        if(root==null)return 0;
        res=root.val;
        dfsSum(root);

        return res;
    }
    public int dfsSum(TreeNode root){
        if(root==null)return 0;
        int leftPath=Math.max(0,dfsSum(root.left));
        int rightPath=Math.max(0,dfsSum(root.right));
        res=Math.max(res,root.val + leftPath + rightPath);
        return root.val+Math.max(leftPath,rightPath);
    }
}
