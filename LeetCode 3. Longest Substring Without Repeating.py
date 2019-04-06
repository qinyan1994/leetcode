class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        stack=[]
        ans=0
        for i in s:
            if i not in stack:
                stack.append(i)
            else:
                if len(stack)>=ans:
                    ans=len(stack)
                    stack.append(i)
                    del stack[:stack.index(i)+1]
                else:
                    stack.append(i)
                    del stack[:stack.index(i)+1]
        return max(ans,len(stack))