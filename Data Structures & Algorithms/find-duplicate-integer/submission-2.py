class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast :
                break 
        p = 0
        while True : 
            slow = nums[slow]
            p = nums[p]
            if p ==slow :
                break 
        return slow