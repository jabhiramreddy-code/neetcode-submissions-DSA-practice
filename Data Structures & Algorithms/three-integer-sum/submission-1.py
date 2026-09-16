class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums = sorted(nums)
        ans = set()
        for i in range(n):
            start = i+1
            end = n-1
            while start < end:
                if nums[start] + nums[end] + nums[i] == 0:
                    ans.add((nums[i], nums[start], nums[end]))
                    start += 1
                    end -= 1
                elif nums[start] + nums[end] + nums[i] > 0:
                    end -= 1
                else:
                    start += 1
        l = []

        for i in ans:
            l.append(list(i))
        return l
