class Solution:
    def moveZeroes(nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        lastnz=0
        for cur in range(len(nums)):
            if nums[cur]!=0:
                nums[lastnz],nums[cur]=nums[cur],nums[lastnz]
                lastnz+=1