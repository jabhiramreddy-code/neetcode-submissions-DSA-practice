class Solution {
    public int hammingWeight(int n) {
        int ans=0;
            System.out.println(n);
        while(n!=0){
            if(n%2==1)ans++;
            n/=2;
        }
        return ans;
    }
}
