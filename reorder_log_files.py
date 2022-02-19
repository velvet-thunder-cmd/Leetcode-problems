class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        res1,res2=[],[]
        for i in logs:
            if (i.split()[1]).isdigit():
                res2.append(i)
            else:
                res1.append(i.split())
        res1.sort(key=lambda x:x[0])
        res1.sort(key=lambda x:x[1:])
        for i in range(len(res1)):
            res1[i]=(" ".join(res1[i]))
        res1.extend(res2)
        return res1
