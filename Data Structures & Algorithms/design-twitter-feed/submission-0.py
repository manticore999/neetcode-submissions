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

        for i in self.followers[userId]:
            if i in self.posts :
                posts+= self.posts[i]
        
            if userId not in self.followers[userId] : 
                posts+= self.posts[userId]

        heapq.heapify_max(posts)
        i=0
        res = []
        while posts and i<10:
            res.append(heapq.heappop_max(posts)[1])
            i+=1
        return res
        
 
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers and followeeId in self.followers[followerId] : 
            self.followers[followerId].remove(followeeId)
        
