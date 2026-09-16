class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        i,j = 0, n-1
        while i<n and j>=0 and i<j:
            if numbers[i] + numbers[j] == target:
                return [i+1,j+1]
            while i < n and numbers[i] + numbers[j] < target:
                i += 1
            while j >= 0 and numbers[i] + numbers[j] > target:
                j -= 1
        return []
        