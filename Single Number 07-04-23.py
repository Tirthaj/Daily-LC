class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Approach 1
        hmap = {}
        for i in nums:
            if i not in hmap: hmap[i] = 0
            hmap[i] += 1
        for key,val in hmap.items():
            if val != 3:
                return key
