class WordDictionary {
    private static class TrieNode{
        Map<Character,TrieNode> children = new HashMap<>();;
        boolean isWord=false;
    }
    private TrieNode root;
    public WordDictionary() {
        root=new TrieNode();
    }

    public void addWord(String word) {
        TrieNode curr=root;
        for(char c:word.toCharArray()){
            curr.children.putIfAbsent(c, new TrieNode());
            curr=curr.children.get(c);
        }
        curr.isWord=true;
    }

    public boolean search(String word) {
        return dfs(root,0,word);
    }
    public static boolean dfs(TrieNode root,int j,String word){
       if(j==word.length())return root.isWord;
       char c=word.charAt(j);
       if(c=='.'){
        for(TrieNode child: root.children.values()){
            if(dfs(child,j+1,word)){
                return true;
            }
        }
        return false;
       }
       else{
        if(!root.children.containsKey(c))
        return false;
        return dfs(root.children.get(c), j + 1, word);
       }
    }
}
