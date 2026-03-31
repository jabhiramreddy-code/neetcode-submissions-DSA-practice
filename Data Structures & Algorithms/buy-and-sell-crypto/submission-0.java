class Solution {
    public int maxProfit(int[] prices) {
        int res = 0,n=prices.length;
        int min = prices[0];
        for(int i=1;i<n;i++){
            min = Math.min(prices[i],min);
            res = Math.max(prices[i]-min,res);
        }
        return res;

    }
}
