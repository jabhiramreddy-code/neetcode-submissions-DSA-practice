class Solution:
    def minWindow(self, s2: str, s1: str) -> str:
        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2:
            return ""
        s1count, s2count = defaultdict(int), defaultdict(int)
        for i in s1:
            s1count[i] += 1
        print(len(s1count))
        match = 0
        ans = len(s2)+1
        ansr = 0
        ansl = 0
        l=0
        target = len(s1count)
        for r in range(0,n2):
            index = s2[r]
            s2count[index] += 1
            if index in s1count and s1count[index] == s2count[index]:
                match +=1
            while l <= r and match == target:
                if ans > r-l+1:
                    ansr = r
                    ansl = l
                    ans = r-l+1
                if s1count[s2[l]] == s2count[s2[l]]:   
                    match -= 1
                s2count[s2[l]] -= 1
                l += 1


            
        if ans == (len(s2)+1):
            return ""
        return s2[ansl:ansr+1]   