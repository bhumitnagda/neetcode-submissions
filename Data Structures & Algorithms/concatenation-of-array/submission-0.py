class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums * 2:
            res.append(i)
        return res