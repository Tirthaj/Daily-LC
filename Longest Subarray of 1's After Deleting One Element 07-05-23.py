class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # My approach
        # More optimal than given solution!
        # Time O(n) # Space O(1)
        left = 0
        right = 0
        res = 0
        flag = False
        for i in nums:
            if i == 0:
                flag = True
                res = max(res, (left+right))
                print(res)
                left = right
                right = 0
            else:
                right += 1
        res = max(res, (left+right))
        if not flag: return res-1
        return res

        # APproach 2 Sliding Window
        # Time O(2n) # Space O(1)
        # left = 0
        # right = 0
        # count = 0
        # res = 0
        # while right < len(nums):
        #     if nums[right] == 0:
        #         count += 1
        #         if count > 1:
        #             while count != 1:
        #                 if nums[left] == 0: 
        #                     count -= 1
        #                 left += 1
        #     right+=1
        #     res = max(res, (right-1-left+1-1))
        # # print(left, right)
        # return res
                    
