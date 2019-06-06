class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        
        if needle=='':
            return 0
        if haystack=='':
            return -1
        for i,j in enumerate(haystack):
            if j==needle[0] and haystack[i:i+len(needle)]==needle:
                return i
                break
            if i==len(haystack)-1:
                return -1
        """
        return haystack.find(needle)