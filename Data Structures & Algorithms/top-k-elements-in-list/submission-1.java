class Solution {
   
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer,Integer> count = new HashMap<>();
        for(int i:nums){
            count.put(i,count.getOrDefault(i,0)+1);
        }
        int n=nums.length;
        int[] ans = new int[k];
        List<Integer>[] fre = new List[n+1];
        for(int i=0;i<fre.length;i++){
            fre[i]=new ArrayList<Integer>();
        }
        for(Map.Entry<Integer,Integer> a : count.entrySet()){
            fre[a.getValue()].add(a.getKey());
        }
        int index=0;
        for(int i=n;i>0 && index<k;i--){
            for(int num:fre[i]){
                ans[index]=num;
                index++;
                if(index==k)return ans;
            }          
        }
        return ans;
    }
}
