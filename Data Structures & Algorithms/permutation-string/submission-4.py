class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2:
            return False
        s1count, s2count = [0]*26, [0]*26
        for i in range(n1):
            s2count[ord(s2[i]) - ord('a')] += 1
            s1count[ord(s1[i]) - ord('a')] += 1
        match = 0
        l = 0
        for i in range(26):
            if s1count[i] == s2count[i]:
                match += 1
        for r in range(n1,n2):
            if match == 26:
                return True
            
            index = ord(s2[r])-ord('a')
            s2count[index] +=1
            if s1count[index] == s2count[index]:
                match += 1
            elif s1count[index] + 1 == s2count[index]:
                match -= 1
            
            index = ord(s2[l])-ord('a')
            s2count[index] -= 1
            if s1count[index] == s2count[index]:
                match +=1
            elif s1count[index]-1 == s2count[index]:
                match -= 1
            l += 1
            # print(match)
        return match == 26        
            

        