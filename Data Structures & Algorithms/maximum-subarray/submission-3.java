class Solution {
    public int maxSubArray(int[] nums) {
        int res=-999999,n=nums.length,sum=0;
        for(int i=0;i<n;i++){
            sum+=nums[i];
            res=Math.max(sum,res);
            if(sum<0)sum=0;
        }
        return res;
    }
}
