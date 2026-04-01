class Solution {
    public int maxProduct(int[] nums) {
        int max=1,min=1,res=nums[0];
        for(int i=0;i<nums.length;i++){
            int temp=max*nums[i];
            max = Math.max(Math.max(temp,min*nums[i]),nums[i]);
            min = Math.min(Math.min(temp,min*nums[i]),nums[i]);
            res = Math.max(max,res);
        }
        return res;
    }
}
