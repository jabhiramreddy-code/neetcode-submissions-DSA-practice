class Solution {
    public int lengthOfLongestSubstring(String s) {
        int res=0,n=s.length(),i=0,j=0;
        HashSet<Character> check = new HashSet<>();
        for(i=0;i<n;i++){
            while(check.contains(s.charAt(i)))
            {
                check.remove(s.charAt(j));
                j++;
            }
            check.add(s.charAt(i));
            res= Math.max(res, i-j+1);
        }
        return res;
    }
}
