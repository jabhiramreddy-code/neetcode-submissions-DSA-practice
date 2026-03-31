class Solution {
    public int findMin(int[] nums) {
        int i=0,n=nums.length,j=n-1;
        int m =0;
        while( j>i){
            m=i+(j-i)/2;
            if(nums[j]>nums[m])j=m;
            else i=m+1;
        }
        return  nums[i];
    }
}
