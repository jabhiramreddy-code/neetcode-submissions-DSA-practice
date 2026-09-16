class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        conList = {}
        ans = 0
        for i in nums:
            conList[i] = i
        for i in nums:
            elm = i
            while (elm - 1) in conList:
                elm -= 1
                if conList[elm] != elm:
                    break;
            conList[i] = conList[elm]
            ans = max(ans, i - conList[i]+1)
        return ans
