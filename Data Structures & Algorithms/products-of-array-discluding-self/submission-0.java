class Solution {
    public int[] productExceptSelf(int[] nums) {
        int zeroCount=0;
        int product=1;
        for(int i: nums){
            if(i==0)zeroCount++;
            product*=i;
        }
        if(zeroCount == 2){
            for(int i=0;i<nums.length;i++){
                nums[i]=0;
            }
            return nums;
        }
        int n=nums.length;
        int[] suffix=new int[n];
        int[] prefix=new int[n];
        suffix[0]=nums[0];
        prefix[n-1]=nums[n-1];
        for(int i=1;i<n-1;i++){
            suffix[i]=suffix[i-1]*nums[i];
        }
        for(int i=n-2;i>=0;i--){
            prefix[i]= prefix[i+1]*nums[i];
        }
        for(int i=0;i<n;i++){
            if(i==0){
                nums[i]=prefix[i+1];
            }
            else if(i==n-1){
                nums[i]=suffix[i-1];
            }
            else{
                nums[i] = suffix[i-1]* prefix[i+1];
            }
        }
        return nums;
    }
}  
