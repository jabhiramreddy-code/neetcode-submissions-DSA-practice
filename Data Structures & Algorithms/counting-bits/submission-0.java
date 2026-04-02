class Solution {
    public int[] countBits(int n) {
        int[] ans=new int[n+1];
        for(int i=0;i<=n;i++){
            int currAns=0;
            for(int j=0;j<32;j++){
                if((1<<j & i)!=0)currAns++;
            }
            ans[i]=currAns;
        }
        return ans;
    }
}
