class Solution {

    public String encode(List<String> strs) {
        String s="12aughaiu32";
        String x= new String();
        for(String str : strs){
            if(str.equals(""))x+=str+"adasxxcesc";
            System.out.print(str.equals(""));
            x+=str+s;
        }
        if(strs.size() ==0)return null;
        return x;
    }

    public List<String> decode(String str) {
String sas="12aughaiu32";
System.out.print(str);
        List<String> ans = new ArrayList<>();
        if(str == null) return ans;
    String[] s = str.split(sas);
        for(String cd : s){
            // if(cd != ""){
            if(cd.equals("adasxxcesc")) ans.add("");
                else ans.add(cd);
            // }
        }
        return ans;
    }
}
