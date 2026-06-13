class Twitter:

    def __init__(self):
        # Global decreasing timestamp so newer tweets have smaller values.
        # This lets us sort tweets by recency using a min‑heap.
        self.count = 0

        # Maps each user to their list of tweets.
        # Each tweet is stored as [timestamp, tweetId].
        # We only keep the last 10 tweets per user for efficiency.
        self.tweetMap = defaultdict(list)

        # Maps each user to the set of users they follow.
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Add the tweet with the current timestamp.
        self.tweetMap[userId].append([self.count, tweetId])

        # Keep only the 10 most recent tweets for this user.
        if len(self.tweetMap[userId]) > 10:
            self.tweetMap[userId].pop(0)

        # Decrease timestamp so newer tweets have smaller values.
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        # A user always follows themselves.
        self.followMap[userId].add(userId)

        # If the user follows many people (≥10), we use a max‑heap optimization
        # to avoid pushing too many tweets into the heap.
        if len(self.followMap[userId]) >= 10:
            maxHeap = []

            # For each followee, push their most recent tweet into the heap.
            for followeeId in self.followMap[userId]:
                if followeeId in self.tweetMap:
                    index = len(self.tweetMap[followeeId]) - 1
                    count, tweetId = self.tweetMap[followeeId][index]

                    # Push into max‑heap using negative timestamp.
                    heapq.heappush(maxHeap, [-count, tweetId, followeeId, index - 1])

                    # Keep heap size at most 10 (only need 10 newest tweets).
                    if len(maxHeap) > 10:
                        heapq.heappop(maxHeap)

            # Convert max‑heap into a min‑heap for final extraction.
            while maxHeap:
                count, tweetId, followeeId, index = heapq.heappop(maxHeap)
                heapq.heappush(minHeap, [-count, tweetId, followeeId, index])

        else:
            # If followee count is small, push all most‑recent tweets directly.
            for followeeId in self.followMap[userId]:
                if followeeId in self.tweetMap:
                    index = len(self.tweetMap[followeeId]) - 1
                    count, tweetId = self.tweetMap[followeeId][index]
                    heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        # Merge tweets from all followees using a k‑way merge.
        # Always pop the newest tweet (smallest timestamp).
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)

            # If this followee has older tweets, push the next one.
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        # Add followee to follower's follow set.
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Remove followee if present.
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
