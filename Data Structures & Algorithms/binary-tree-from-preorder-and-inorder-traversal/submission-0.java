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
    int preOrderRoot;
    Map<Integer,Integer> inOrderRoots;
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        preOrderRoot=0;
        inOrderRoots = new HashMap<>();
        for(int i=0;i<inorder.length;i++){
            inOrderRoots.put(inorder[i],i);
        }
        return tree(preorder,0,inorder.length-1);                         
    }
    public TreeNode tree(int[] preOrder,int left,int right){
        if(left>right)return null;
        int rootVal=preOrder[preOrderRoot++];
       TreeNode root=new TreeNode(rootVal);
        int mid = inOrderRoots.get(rootVal);
        root.left=tree(preOrder,left,mid-1);
        root.right=tree(preOrder,mid+1,right);
        return root;
    }
}
