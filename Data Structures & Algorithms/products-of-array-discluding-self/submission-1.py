class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        n=len(nums)
        # for i in range(n):
        #     if n == 0:
        #         left.append(nums[i])
        #     else:
        #         left.append(left[i-1]*nums[i])
        mult = 1
        zeroCount=0
        oneZero=1
        for i in nums:
            if i == 0:
                zeroCount+=1
            if zeroCount >= 2:
                return [0]*n
            if zeroCount == 1 and i==0:
                continue
            mult *= i
        for i in nums:
            if zeroCount == 1:
                if i == 0:
                    left.append(mult)
                else:
                    left.append(0)
            else:
                left.append(int(mult/i))
        return left
            

        