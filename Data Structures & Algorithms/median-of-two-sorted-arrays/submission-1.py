class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a,b = nums1,nums2
        if len(a)>len(b):
            a,b = b,a
        total = len(a) + len(b)
        h = total // 2 
        l,r = 0 ,len(a)-1
        while 1 : 
            i = (l+r) //2
            j = h -i-2
            aleft = a[i] if i>=0 else float("-inf")
            aright = a[i+1] if i+1 <len(a) else float("inf")
            bright = bright = b[j+1] if j+1 <len(b) else float("inf")
            bleft = b[j] if j>=0 else float("-inf")
            if aleft <= bright and bleft <= aright:
                if total% 2:
                    return min(aright,bright)
                return (max(aleft,bleft)+min(aright,bright))/2
            elif bright < aleft :
                r = i-1
            else : 
                l = i+1 


