public class TreeNode{
    TreeNode[] children=new TreeNode[26];
    boolean end=false;
}

class PrefixTree {
    private TreeNode root;

    public PrefixTree() {
        root=new TreeNode();
    }

    public void insert(String word) {
        TreeNode curr=root;
        for(char c: word.toCharArray()){
            int i=c-'a';
            if(curr.children[i]==null){
                curr.children[i]=new TreeNode();
            }
            curr=curr.children[i];
        }
        curr.end=true;
    }

    public boolean search(String word) {
        TreeNode curr=root;
        for(char c:word.toCharArray()){
            int i=c-'a';
            if(curr.children[i]==null)return false;
            curr=curr.children[i];
        }
        return curr.end;
    }

    public boolean startsWith(String prefix) {
  TreeNode curr=root;
        for(char c:prefix.toCharArray()){
            int i=c-'a';
            if(curr.children[i]==null)return false;
            curr=curr.children[i];
        }
        return true;
    }
}
