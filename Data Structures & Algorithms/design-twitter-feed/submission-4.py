class Twitter:

    def __init__(self):
        self.followers = defaultdict(set) # we have the user as the key , and the people that he follows

        self.posts = defaultdict(list) # key : userid , value : posts of that user 
        self.count = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:

        self.posts[userId].append((self.count,tweetId))
        self.count+=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        people = [userId] + list(self.followers[userId])
        posts = []
        for follower in people : 
            posts+= self.posts[follower]
        res = []
        k = 10
        heapq.heapify_max(posts)
        while k>0 and posts:
            count, tweetid= heapq.heappop_max(posts)
            res.append(tweetid)
            k-=1
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
