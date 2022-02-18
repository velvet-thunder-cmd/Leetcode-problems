class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash={}
        for i,value in enumerate(nums):
            if value in hash:
                return [hash[value],i]   
            hash[target-value] = i
        return []
