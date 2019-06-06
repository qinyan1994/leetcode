class Solution:
    def isValid(self, s: str) -> bool:
        dic={'(':')','[':']','{':'}'}
        stack=[]
        for i in s:
            if i in dic:
                stack.append(i)
            else:
                if not stack or i!=dic[stack.pop()]:
                    return False
        return stack==[]