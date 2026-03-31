class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> visitedNumber=new HashMap<>();
        int[] ans=new int[2];
        visitedNumber.put(nums[0],0);
        for(int i=1;i<nums.length;i++){
            int isExiste =target-nums[i];
            if(visitedNumber.containsKey(isExiste)){
                ans[0]= visitedNumber.get(isExiste);
                ans[1]=i;
                return ans;
            }
            else
            visitedNumber.put(nums[i],i);
        }
        return ans;
    }
}
