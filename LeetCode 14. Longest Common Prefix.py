class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        #def qianzhui(strs):
        if not strs:
            return ''
        length,index=len(strs[0]),0
        for i,j in enumerate(strs):
            if len(j)<=length:
                length=len(j)
                index=i
        ans=''
        for i,j in enumerate(strs[index]):
            for k in strs:
                if k[i]!=j:
                    return ans
            else:
                ans+=j
        return ans