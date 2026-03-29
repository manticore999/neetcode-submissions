class Twitter:

    def __init__(self):
        self.followers = defaultdict(set)
        self.posts = defaultdict(list)
        self.order = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append([self.order,tweetId])
        self.order+=1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        posts = []
        res = []
        self.followers[userId].add(userId)
        maxheap = []
        heapq.heapify_max(maxheap)
        
        for follower in self.followers[userId]:
            if follower in self.posts :
                i = len(self.posts[follower])-1
                order , tid = self.posts[follower][i]
                heapq.heappush_max(maxheap,[order,tid,follower,i-1])
            if len(maxheap)> 10 :
                heapq.heappop_max(maxheap)
        res = []
        while maxheap and len(res)<10:
            order , tid , follower , i = heapq.heappop_max(maxheap)
            res.append(tid)
            if i >= 0:
                order , tid = self.posts[follower][i]
                heapq.heappush_max(maxheap,[order,tid,follower,i-1])
        return res
 
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers and followeeId in self.followers[followerId] : 
            self.followers[followerId].remove(followeeId)
        
