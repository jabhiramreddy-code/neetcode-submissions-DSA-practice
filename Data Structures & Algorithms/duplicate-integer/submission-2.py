class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # nums.sort()
        # for i in range(1, len(nums)):
        #     if nums[i]==nums[i-1]:
        #         return True
        # return False;
        hasSet = set();
        for i in range(0, len(nums)):
            if nums[i] in hasSet:
                return True;
            hasSet.add(nums[i]);
        return False


        
        