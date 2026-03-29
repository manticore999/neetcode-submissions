class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [ (position[i],speed[i]) for i in range(len(speed))]
        pair.sort(reverse=True)
        st = []
        for p,s in pair : 
            st.append((target-p)/s)
            if len(st)>=2 and st[-1]<=st[-2]:
                st.pop()
        return len(st)
                    
                     


        