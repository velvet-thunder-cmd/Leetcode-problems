def findMaxConsecutiveOnes(nums) -> int:
        maxcount = 0
        count = 0
        for i in nums:
            if i:
                count+=1
                continue 
            maxcount = max(maxcount, count)
            count = 0 
        return max(maxcount, count)
