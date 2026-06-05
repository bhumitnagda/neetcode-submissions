class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s= list(sorted(s))
        # t = list(sorted(t))
        if sorted(s) == sorted(t):
            return True
        else: return False