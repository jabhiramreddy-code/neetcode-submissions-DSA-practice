class Solution {
    public int numIslands(char[][] grid) {
        int n=grid.length;
        int m=grid[0].length;
    boolean[][] visited = new boolean[n][m];
    int ans=0;
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(grid[i][j]=='1' && !visited[i][j])
                { ans++;
                    dfs(grid,visited,n,m,i,j);
                }
            }
        }
        return ans;
    }
    public void dfs(char[][] grid,boolean[][] visited,int n,int m,int i,int j){
        if(i<0 || j<0 || i>=n || j>=m || grid[i][j]=='0' || visited[i][j])return;
        visited[i][j]=true;
        dfs(grid,visited,n,m,i,j+1);
        dfs(grid,visited,n,m,i,j-1);
        dfs(grid,visited,n,m,i+1,j);
        dfs(grid,visited,n,m,i-1,j);
    }
}
