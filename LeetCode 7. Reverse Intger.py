class Solution:
    def reverse(self, x: int) -> int:
        if x==0:
            return 0
        x=str(x)
        x=x[::-1]
        for i,j in enumerate(x):
            if j!='0':
                s=x[i:]
                if s[-1]=='-':
                    ans=eval(s[-1]+s[:-1])
                    break
                else:
                    ans=eval(s)
                    break
        if ans>=-2**31 and ans<=2**31-1:
            return ans
        else:
            return 0