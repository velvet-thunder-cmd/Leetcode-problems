class Solution:
    def sortArrayByParity(self, nums):
        left = 0
        right = len(nums)-1
        while left < right:
            if nums[left] %2 != 0 and nums[right] % 2 == 0:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
                right -= 1
            elif nums[left] %2 == 0 and nums[right]%2 != 0:
                left += 1
                right -= 1
            elif nums[left]%2 == 0:
                left += 1
            else:
                right -= 1
        return nums
