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
    List<List<Integer>> ans =new ArrayList<>();
    public List<List<Integer>> levelOrder(TreeNode root) {
        // Queue<TreeNode> q=new LinkedList<>();
        // List<List<Integer>> ans = new  ArrayList<>();
        // q.add(root);
        // while(!q.isEmpty()){
        //     List<Integer> save=new ArrayList<>();
        //     for(int i=q.size();i>0;i--){
        //         TreeNode temp1 = q.poll();
        //         if(temp1!=null){
        //             save.add(temp1.val);
        //             q.add(temp1.left);
        //             q.add(temp1.right);
        //         }

        //     }
        //     if(save.size()>0)
        //     ans.add(save);
        // }
        // return ans;

        dfs(root,0);
        return ans;
    }
    public void dfs(TreeNode root, int depth){
        if(root==null)return;
        if(ans.size()==depth){
            ans.add(new ArrayList());
        }
        ans.get(depth).add(root.val);
        dfs(root.left,depth+1);
        dfs(root.right,depth+1);
    }
}
