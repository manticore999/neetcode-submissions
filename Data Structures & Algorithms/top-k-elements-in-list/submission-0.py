class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        res = []
        for i in nums : 
            count[i] =count.get(i,0) + 1

        for i,c in count.items():
            freq[c].append(i)

        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k :
                    return res






        