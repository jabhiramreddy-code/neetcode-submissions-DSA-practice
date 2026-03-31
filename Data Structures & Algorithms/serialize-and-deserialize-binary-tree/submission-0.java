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

public class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        List<String> l=new ArrayList<>();
        dfsSerialize(root,l);
        System.out.println("asdasd"+String.join(",",l));
        return String.join(",",l);
    }

    public static void dfsSerialize(TreeNode root,List<String> l){
        if(root==null){
            l.add("N");
            return;
        }
        l.add(String.valueOf(root.val));
        dfsSerialize(root.left,l);
        dfsSerialize(root.right,l);

    }
    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        String[] s=data.split(",");
        System.out.println(data);
        int[] i={0};
        return dfsDeserialize(s,i);
    }
    public TreeNode dfsDeserialize(String[] s,int[] i){
        if(s[i[0]].equals("N")){
            i[0]++;
            return null;
        }
        TreeNode root=new TreeNode(Integer.parseInt(s[i[0]]));i[0]++;
        root.left=dfsDeserialize(s,i);
        root.right=dfsDeserialize(s,i);
        return root;
    }
}
