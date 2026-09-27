class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # merge sort
        if len(nums) <= 1:
            return nums

        # dividing array nums into 2 halfs
        mid = len(nums) // 2
        left_half = nums[:mid]
        right_half = nums[mid:]

        # recursion
        self.sortArray(left_half)
        self.sortArray(right_half)

        i = 0
        j = 0
        k = 0

        # conquer
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                nums[k] = left_half[i]
                i += 1
                k += 1
            else:
                nums[k] = right_half[j]
                j += 1
                k += 1

        while i < len(left_half):
            nums[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            nums[k] = right_half[j]
            j += 1
            k += 1
        return nums



