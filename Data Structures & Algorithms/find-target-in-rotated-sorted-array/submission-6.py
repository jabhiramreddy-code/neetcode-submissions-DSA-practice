class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        i,j = 0,n-1
        while i<=j:
            m = (i+j)//2
            if nums[m] == target:
                return m
            if nums[i]<=nums[m]:
                if nums[i]<= target < nums[m]:
                    j = m-1
                else:
                    i = m+1
            else:
                if nums[m]< target <= nums[j]:
                    i = m+1
                else:
                    j = m-1
                    
        return -1;

        