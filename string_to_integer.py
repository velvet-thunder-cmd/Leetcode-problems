class Solution:
    def myAtoi(self, s: str) -> int:
        MIN_INT= -2**31
        MAX_INT= 2**31 -1
        i=0
        res=0
        neg=1
        while i<len(s) and s[i]==' ':
            i+=1
        if i<len(s) and s[i]=='-':
            i+=1
            neg=-1
        elif i<len(s) and s[i] == '+':
            i+=1
        checker=set('0123456789')
        while i<len(s) and s[i] in checker:
            res=res*10+int(s[i])
            i+=1
        res=res*neg
        if res<0:
            return max(MIN_INT, res)
        return min(MAX_INT,res)
