class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # nums = [0,1,2,2,3,0,4,2]
        k = len(nums) # k = 8
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                nums.pop(i)
                k -= 1
        return k