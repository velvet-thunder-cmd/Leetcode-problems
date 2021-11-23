from math import floor, log10
class Solution:
    def findNumbers(nums) -> int:
        return sum(floor(log10(num)) % 2 for num in nums)




        