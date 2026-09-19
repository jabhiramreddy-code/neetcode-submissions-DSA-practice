class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charMap=defaultdict(int)
        ans = 0
        n = len(s)
        maxf = 0
        l = 0
        for i in range(n):
            charMap[s[i]] = charMap[s[i]] + 1
            maxf = max(maxf, charMap[s[i]])
            while (i - l - maxf + 1) > k:
                charMap[s[l]] -= 1
                l += 1
            ans = max(ans, i-l+1);
        return ans

