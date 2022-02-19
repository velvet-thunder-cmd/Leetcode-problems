class Solution:
    def reverse(self, x: int) -> int:
        r=0
        t=0
        MIN_INT=-2**31
        MAX_INT=2**31 -1
        while x:
            r=int(math.fmod(x,10))
            x=int(x/10)
            
            if (t>MAX_INT//10 or (t==MAX_INT//10 and r>=MAX_INT%10)):
                return 0
            elif (t<MIN_INT//10 or (t==MIN_INT//10 and r<=MIN_INT%10)):
                return 0
            t = t*10+r
        return t 
