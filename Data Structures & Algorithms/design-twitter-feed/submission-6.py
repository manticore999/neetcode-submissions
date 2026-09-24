class Twitter:

    def __init__(self):
        self.followers = defaultdict(set) # we have the user as the key , and the people that he follows

        self.posts = defaultdict(list) # key : userid , value : posts of that user 
        self.count = 0
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.count,tweetId))
        self.count+=1
    
    def getNewsFeed(self, userId: int) -> List[int]:
        maxheap = []
        
        self.followers[userId].add(userId)
        for followee in list(self.followers[userId]) :
            if followee in self.posts :  
                last = len(self.posts[followee])-1
                count , postid = self.posts[followee][last]
                maxheap.append((count,postid,followee,last-1))
            heapq.heapify_max(maxheap)
            res = []

        while maxheap and len(res)< 10 : 
            count , postid,followee, index = heapq.heappop_max(maxheap)
            res.append(postid)
            if index >= 0 : 
                count , postid = self.posts[followee][index]
                heapq.heappush_max(maxheap,(count,postid,followee,index-1))
        return res 
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
