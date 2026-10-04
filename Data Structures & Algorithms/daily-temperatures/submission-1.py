class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0]*len(temperatures)
        stack = [] # [temp,index]

        for index, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackt, stacki = stack.pop()
                ans[stacki] =  index - stacki
            stack.append([t,index])
        return ans