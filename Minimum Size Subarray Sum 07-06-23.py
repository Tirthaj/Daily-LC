class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Approach 1
        p1 = 0
        p2 = 1
        cursum = nums[p1]
        res = 10**5+1
        if cursum >= target: return 1
        while p2 < len(nums):
            cursum += nums[p2]
            if cursum >= target:
                res = min(res, (p2-p1+1))
                while cursum >= target and p1 < p2:
                    cursum -= nums[p1]
                    p1 += 1
                    if cursum >= target:
                        res = min(res, (p2-p1+1))
            p2 += 1
        return 0 if res == 10**5+1 else res
            


