class Solution {
    static String encodedString= "12aughaiu32";
    static String nullAvoiderString = "adasxxcesc";
    public String encode(List<String> strs) {
        String x= new String();
        for(String str : strs){
            if(str.equals(""))x+=str+nullAvoiderString;
            x+=str+encodedString;
        }
        if(strs.size() ==0)return null;
        return x;
    }

    public List<String> decode(String str) {
        List<String> ans = new ArrayList<>();
        if(str == null) return ans;
    String[] s = str.split(encodedString);
        for(String cd : s){
            // if(cd != ""){
            if(cd.equals(nullAvoiderString)) ans.add("");
                else ans.add(cd);
            // }
        }
        return ans;
    }
}
