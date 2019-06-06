class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        if 0<=x and x<10:
            return True
        start=0
        s=str(x)
        end=len(s)-1
        
        while start<end:
            if s[start]!=s[end]:
                return False
            start+=1
            end-=1
        return True