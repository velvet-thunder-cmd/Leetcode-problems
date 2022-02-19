class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x,y = 0,0
        xd,yd = 0,1
        for i in instructions:
            if i=='G':
                x,y=x+xd,y+yd
            elif i=="L":
                xd,yd=-1*yd,xd
            else:
                xd,yd=yd,-1*xd
        return (x,y)==(0,0) or (xd,yd)!=(0,1)
