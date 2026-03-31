class Solution {
    public int characterReplacement(String s, int k) {
        int n=s.length();
        if(k==n)return k;
        
        HashMap<Character,Integer> save = new HashMap<>();
        int j=0,maxf=0,res=0;
        for(int i=0;i<n;i++){
            char c=s.charAt(i);
            save.put(c,save.getOrDefault(c,0)+1);
            maxf=Math.max(save.get(c),maxf);
            while((i-j+1)-maxf>k){
                save.put(s.charAt(j),save.get(s.charAt(j))-1);
                j++;
            }
            res=Math.max(i-j+1,res);
        }
        return res;
    }
}
