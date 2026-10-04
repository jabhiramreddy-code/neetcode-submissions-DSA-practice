class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = [] #pair [position, time]
        for i in range(len(position)):
            time.append([position[i],(target - position[i])/speed[i]]);
        time.sort()
        ans = 0
        i = len(speed)-1
        stack = []
        while i >= 0:
            if not stack:
                stack.append(time[i][1])
                i-=1
            while i>=0 and stack[-1] >= time[i][1]:
                i-=1
            if i>=0:
                stack.append(time[i][1])
            i-=1
        return len(stack)