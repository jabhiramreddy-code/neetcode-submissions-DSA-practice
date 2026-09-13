class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        exist = {}
        for i,n in enumerate(nums):
            if target - n in exist:
                return [exist[target-n], i]
            else:
                exist[n]=i
        return [-1,-1]
        