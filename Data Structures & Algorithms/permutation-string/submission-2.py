class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2:
            return False
        sor = tuple(sorted(s1))
        se = set()
        se.add(sor)
        for i in range(0,n2-n1+1, 1):
            a = tuple(sorted(s2[i:i+n1]))
            # print(a)
            if a in se:
                return True
        return False

            

        