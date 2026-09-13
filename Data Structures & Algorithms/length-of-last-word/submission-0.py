class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        last_space = -1
        for i in range(len(s)):
            if s[i] == " ":
                last_space = i
        return len(s[last_space+1:]) if last_space!=-1 else len(s)
        