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
    public int ans=-1,i=0;
    public void dfs(TreeNode root, List arr){
        if(root==null) return;
        dfs(root.left,arr);
        arr.add(root.val);
        dfs(root.right, arr);
    }
    public int kthSmallest(TreeNode root, int k) {
        List<Integer> ans=new ArrayList<>();
        dfs(root,ans);
        return ans.get(k-1);
    }
}
