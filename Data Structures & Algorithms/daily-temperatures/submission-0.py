class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans   = [0]*len(temperatures)
        n = len(temperatures)
        for i in range (n-1, -1, -1):
            if not stack:
                stack.append(i);
            else:
                while stack:
                    if temperatures[stack[(len(stack)-1)]] <= temperatures[i]:
                        stack.pop()
                    else:
                        ans[i] = stack[len(stack)-1]-i;
                        break
                stack.append(i);
            # print(ans,stack,i)
        return ans;