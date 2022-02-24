class Solution(object):
    def missingNumber(self, nums):
        maxi=len(nums)
        while not maxi<0:
            if maxi not in nums:
                return maxi
            else:
                maxi-=1
