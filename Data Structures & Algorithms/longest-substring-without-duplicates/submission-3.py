class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sMap = defaultdict(int)
        n = len(s)
        i = 0
        j = 0
        ans = 0
        while j<n and i <= j:
            temp = s[j]
            if temp not in sMap:
                sMap[temp] = 1   
                j += 1
            else:
                while temp in sMap:
                    # print(s[i] , temp, sMap)
                    del sMap[s[i]]
                    i += 1
                sMap[temp] = 1
                if j + 1 < n:
                    j = j+1
            # print(i,j)
            ans = max(ans, len(sMap))
        return ans

