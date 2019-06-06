class Solution:
    """
    @param A: a list of integers
    @return an integer
    """
    def removeDuplicates(self, A):
        # write your code here
        k=0
        for i in range(1,len(A)):
            if A[i] != A[k]:
                k+=1
                A[k] = A[i]
        
        del A[k+1:len(A)]
        return len(A)
        
                    