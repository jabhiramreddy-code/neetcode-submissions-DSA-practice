class Solution {
    public int maxArea(int[] heights) {
        int n=heights.length,i=0,j=n-1;
        // while(i<n-1 && heights[i]<heights[i+1])i++;
        // while(j>0 && heights[j-1]>heights[j])j--;
        if(i==n-1 || j == 0)return 0;
        int res=0,sum=0;
        while(i<j && i<n && j>0){
        int minHeight=Math.min(heights[i],heights[j]);
        sum = minHeight*(j-i);
        res = Math.max(sum,res);
        System.out.println(sum+" "+res);
        if(heights[i]<=heights[j]){
            while(i<n-1 && heights[i]>heights[i+1])i++;
            i++;
        }
        else{
            while(j>i && heights[j]>heights[j-1])j--;
            j--;
        }
        }
        return res;
    }
}
