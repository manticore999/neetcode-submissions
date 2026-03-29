class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2!=0:
            return False

        target = sum(nums)/2
        s = set()
        s.add(nums[0])
        s.add(0)
        for i in range (1,len(nums)):
            if target in s:
                return True
            temp = []
            for n in s:
                if n+nums[i] in s or n+nums[i] >target:
                    continue
                temp.append(n+nums[i])
            s.update(temp)
        return False
        
            