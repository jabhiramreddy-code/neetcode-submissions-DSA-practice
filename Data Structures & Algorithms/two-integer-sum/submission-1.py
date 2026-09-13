class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        exist = {}
        for i in range(len(nums)):
            if target - nums[i] in exist:
                return [exist[target-nums[i]], i]
            else:
                exist[nums[i]]=i
        return [-1,-1]
        