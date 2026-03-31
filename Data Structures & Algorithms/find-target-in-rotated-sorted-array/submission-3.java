class Solution {
    public int search(int[] nums, int target) {
        int i=0,n=nums.length,j=n-1;
        while(j>=i){
            int m=i+(j-i)/2;
            System.out.println(i+" d "+j);
           if(nums[m]==target)return m;
            if(nums[i]<=nums[m]){
                if(target > nums[m] || target < nums[i] ){
                    i=m+1;
                }
                else
                    j=m-1;
            }
            else
                {
                    if(target < nums[m] || target > nums[j])
                    j=m-1;
                    else 
                    i=m+1;
                }
        }
        return -1;
    }
}

//6
// 3 4 5 6 7 1 2
    //    m