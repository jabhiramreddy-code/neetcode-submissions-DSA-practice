class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String,List<String>> savingAnagrams = new HashMap<>();
        for(int i=0;i<strs.length;i++){
            char[] c=strs[i].toCharArray();
            Arrays.sort(c);
            String s=Arrays.toString(c);
            if(savingAnagrams.containsKey(s)){
                savingAnagrams.get(s).add(strs[i]);
            }
            else{
                savingAnagrams.put(s,new ArrayList<>());
                savingAnagrams.get(s).add(strs[i]);
            }
        }
        return new ArrayList<>(savingAnagrams.values());
    }
}
