class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for a in asteroids:
            while stack and a<0 and stack[-1]>0:
                dif=a+stack[-1]
                if dif<0:
                    stack.pop()
                elif dif>0:
                    a=0
                else:
                    a=0
                    stack.pop()
            if a:
                stack.append(a)
        return stack
