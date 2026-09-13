class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # nums.sort()
        # for i in range(1, len(nums)):
        #     if nums[i]==nums[i-1]:
        #         return True
        # return False;
        # hasSet = set(nums);
        # for i in range(0, len(nums)):
        #     if nums[i] in hasSet:
        #         return True;
        # return False
        return len(set(nums)) != len(nums)


        
        