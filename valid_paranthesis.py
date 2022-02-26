class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        mapping = {")": "(", "}": "{", "]": "["}
        if len(s)==1:
            return False
        
        for i in s:
            if i in mapping and len(stack)!=0:
                if stack[len(stack)-1]==mapping[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
                
        if len(stack)==0:
            return True
        else:
            return False
