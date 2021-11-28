class Solution:
    def checkIfExist(arr) -> bool:
        for i in arr:
            if i == 0 :
                if arr.count(0)%2 == 0:
                    return True
                else:
                    continue
            if i*2 in arr:
                return 1
        else:
            return 0