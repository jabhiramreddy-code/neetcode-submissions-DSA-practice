class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sMap = defaultdict(int)
        n = len(s)
        ans = 0
        l=0
        for i in range(n):
            if s[i] in sMap:
                l = max(sMap[s[i]] + 1, l)
            sMap[s[i]] = i
            ans = max(ans, i - l + 1)
            
        return ans

