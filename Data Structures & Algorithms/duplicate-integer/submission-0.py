class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        start = {}
        for s in nums:
            if s in start:
                start[s] +=1
            else:
                start[s] = 1

        for k,v in start.items():
            if v > 1:
                return True
        
        return False