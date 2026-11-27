class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        ans = []
        def sub(nums,temp,i):
            if len(nums) == i:
                ans.append(temp.copy())
                return
            temp.append(nums[i])
            sub(nums,temp,i+1)
            temp.pop()
            sub(nums,temp,i+1)
        sub(nums,[],0)
        return ans
        