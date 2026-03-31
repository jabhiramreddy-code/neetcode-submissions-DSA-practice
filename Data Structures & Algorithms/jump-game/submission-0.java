class Solution {
    public boolean canJump(int[] nums) {
        int n=nums.length;
        boolean[] track=new boolean[n];
        track[n-1]=true;
        if(n==1)return true;
        int lastIndexVisited=n-1;
        for(int i=n-2;i>=0;i--){
            if(i+nums[i]>=lastIndexVisited){
                track[i]=true;
                lastIndexVisited=i;
            }
        } 
        return track[0];
    }
}
