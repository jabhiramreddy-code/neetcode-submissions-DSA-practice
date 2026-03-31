class Solution {
    static String encodedString= "12aughaiu32";
    static String nullAvoiderString = "adasxxcesc";
    public String encode(List<String> strs) {
    StringBuilder sb = new StringBuilder();
        for(String str : strs){
            if(str.equals(""))sb.append(str).append(nullAvoiderString);
            sb.append(str).append(encodedString);
        }
        if(strs.size() ==0)return null;
        return sb.toString();
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
