class Solution {

    public String encode(List<String> strs) {
        StringBuilder s = new StringBuilder();
        for(String str: strs){
            s.append(str.length()).append("#").append(str);
        }
        return s.toString();
    }

    public List<String> decode(String str) {
        List<String> res = new ArrayList<>();
        int i=0,n=str.length();
        while(i<n){
            int temp = i;
            while(str.charAt(temp)!='#'){
                temp++;
            }
            int l=Integer.parseInt(str.substring(i,temp));
            i=temp+1;
            temp=i+l;
            res.add(str.substring(i,temp));
            i=temp;
        }
        return res;
    }
}
