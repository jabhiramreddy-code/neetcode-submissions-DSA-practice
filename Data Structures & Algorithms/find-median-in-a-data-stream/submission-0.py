class MedianFinder:

    def __init__(self):
        self.arr = []
        

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        

    def findMedian(self) -> float:
        n = len(self.arr)
        if n == 1:
            return self.arr[0]
        self.arr.sort()
        if n % 2==0:
            mid = n//2
            mid1 = mid-1
            return (self.arr[mid] + self.arr[mid1])/2
        else:
            return self.arr[n//2]
        
        