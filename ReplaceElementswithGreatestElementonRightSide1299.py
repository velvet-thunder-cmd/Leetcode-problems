class Solution:
    def replaceElements(arr):
        curMax = -1
        for i in range(len(arr)-1, -1, -1):
            arr[i], curMax = curMax, max(arr[i], curMax)
        return arr
