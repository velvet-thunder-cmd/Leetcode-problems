class Solution:
    def duplicateZeros(arr) -> None:
        z = arr.count(0)
        l = len(arr)
        for i in range(l-1, -1, -1):
            if i + z < l:
                arr[i + z] = arr[i]
            if arr[i] == 0: 
                z -= 1
                if i + z < l:
                    arr[i + z] = 0