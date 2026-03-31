class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length()!=t.length())return false;
        int n=s.length();
        int[] first=new int[26];
        int[] secound=new int[26];
        for(int i=0;i<n;i++){
            first[(s.charAt(i)-'a')]++;
            secound[(t.charAt(i)-'a')]++;
        }
        return Arrays.equals(first,secound);
    }
}
