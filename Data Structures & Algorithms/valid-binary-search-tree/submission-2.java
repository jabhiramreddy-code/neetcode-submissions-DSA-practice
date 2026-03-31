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
    public boolean validate(TreeNode root, int left, int right){
        if(root==null)return true;
        if(!(left<root.val && right> root.val) )return false;
     return validate(root.left,left, root.val) && validate(root.right, root.val,right);
         
    }
    public boolean isValidBST(TreeNode root) {
     if(root==null)return true;

     
     return validate(root, -1001,1001) ;
    }
}
