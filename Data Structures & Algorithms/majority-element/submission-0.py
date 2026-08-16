class Solution:
    def majorityElement(self, nums: List[int]) -> int:
      major = len(nums) // 2
      start = {}
      for item in nums:
        if item in start:
            start[item] += 1
        else:
            start[item] = 1
        for key,val in start.items():
            if val > major:
                return key