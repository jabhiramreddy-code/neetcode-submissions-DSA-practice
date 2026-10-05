class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        m = max(piles);
        i,j = 1,m
        res = m
        while i<=j:
            m = ((i +j)//2)
            ma=0
            for p in piles:
                ma += math.ceil(p/m);
            if ma <= h:
                res = min(res, m)
                j = m-1
            elif ma > h:
                i = m+1
        return res
        