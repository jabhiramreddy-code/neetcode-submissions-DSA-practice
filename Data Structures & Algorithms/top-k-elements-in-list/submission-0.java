class Solution {
    static HashMap<Integer, Integer> sortByValue(Map<Integer, Integer> hm) {
        // Create a list from elements of HashMap
        List<Map.Entry<Integer, Integer> > list =
               new LinkedList<Map.Entry<Integer, Integer> >(hm.entrySet());

        // Sort the list
        Collections.sort(list, new Comparator<Map.Entry<Integer, Integer> >() {
            public int compare(Map.Entry<Integer, Integer> o1, 
                               Map.Entry<Integer, Integer> o2) {
                return -(o1.getValue()).compareTo(o2.getValue());
            }
        });
        
        // put data from sorted list to hashmap 
        HashMap<Integer, Integer> temp = new LinkedHashMap<Integer, Integer>();
        for (Map.Entry<Integer, Integer> aa : list) {
            temp.put(aa.getKey(), aa.getValue());
        }
        return temp;
    }
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer,Integer> count = new HashMap<>();
        for(int i:nums){
            count.put(i,count.getOrDefault(i,0)+1);
        }
        int[] ans = new int[k];
       Map<Integer,Integer> x=sortByValue(count);
       for (Map.Entry<Integer, Integer> en : x.entrySet()) {
            System.out.println(en.getKey() + 
                          ": " + en.getValue());
                          k--;
                          ans[k]=en.getKey();
                          if(k==0)return ans;
        }
        return ans;
    }
}
