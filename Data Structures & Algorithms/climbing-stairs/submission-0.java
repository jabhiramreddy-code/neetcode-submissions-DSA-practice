class Solution {
    public int climbStairs(int n) {
        if(n==1)return 1;
        if(n==2)return 2;
        int last=1,lastButOne=2,ans=0;
        for(int i=n-3;i>=0;i--){
            ans=last+lastButOne;
            last=lastButOne;
            lastButOne=ans;
        }
        return ans;

        
    }
}
