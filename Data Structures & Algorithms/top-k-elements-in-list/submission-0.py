class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        start = {}

        for item in nums:
            if item in start:
                start[item] += 1
            else:
                start[item] = 1 

        sorted_items = sorted(start.items(), key = lambda item:item[1], reverse = True)[:k]

        sorted_items = dict(sorted_items)

        arr = []

        for key,val in sorted_items.items():
            arr.append(key)
        
        return arr


