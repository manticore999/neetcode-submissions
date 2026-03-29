class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify_max(nums)
        x= 0
        while(k>0):
            k-= 1
            x = heapq.heappop_max(nums)
        return x