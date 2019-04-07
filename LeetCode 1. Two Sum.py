class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i,j in enumerate(nums):
            k=target-j
            if k in d:
                return [d[k],i]
            else:
                d[j]=i