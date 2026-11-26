class Twitter:

    def __init__(self):
        self.users = {}
        self.usersPost = {}
        self.time = 0
        self.allPosts = []
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.users.setdefault(userId,set())
        heapq.heappush(self.allPosts,(-self.time,userId,tweetId))
        # print(self.allPosts)
        self.time+=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        arr = []
        res = []
        i = 0;
        while self.allPosts and i<10:
            x = heapq.heappop(self.allPosts)
            if userId in self.users and (x[1] in self.users[userId] or x[1] == userId):
                res.append(x[2])
                i+=1
            arr.append(x)
        for i in arr:
            heapq.heappush(self.allPosts,i)
        return res

        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId!=followeeId:
            self.users.setdefault(followerId,set()).add(followeeId)




    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users:
            self.users[followerId].discard(followeeId)
        
