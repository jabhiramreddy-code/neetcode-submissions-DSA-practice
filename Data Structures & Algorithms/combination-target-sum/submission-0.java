class Solution {
    public List<List<Integer>> combinationSum(int[] nums, int target) {
        List<List<Integer>> ans =new ArrayList<>();
        List<Integer> curr = new ArrayList<>();
        dfs(nums,target,ans,curr,0,0); return ans;
    }
    public void dfs(int[] num, int target, List<List<Integer>> ans, List<Integer> curr, int sum, int i){
        if(target == sum){
            ans.add(new ArrayList(curr));
            return;
        }
        if(i>=num.length || sum> target)return;
        curr.add(num[i]);
        dfs(num, target,ans,curr,sum+num[i],i);
        curr.remove(curr.size() - 1);
        dfs(num, target,ans,curr,sum,i+1);
    }
}
