class Solution:
    def removeElement(nums,val) -> int:
        if len(nums) == 0:
            return 0
        left = 0
        right = len(nums) - 1
        while (left < right):
            if nums[left] != val:
                left += 1
                continue
            if nums[right] == val:
                right -= 1
                continue
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        newLen = 0
        if nums[0] == val:
            return 0
        for i in range(len(nums)):
            if nums[i] != val:
                newLen = i
        return newLen + 1 





