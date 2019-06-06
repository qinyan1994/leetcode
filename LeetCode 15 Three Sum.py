class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums)<3:
            return []
        if len(nums)==3:
            if nums[0]+nums[1]+nums[2]==0:
                return [nums[0],nums[1],nums[2]]
        l=[]
        for i,j in enumerate(nums):
            if i==len(nums)-2:
                return l
            for k in nums[i+1:]:
                if 0-(j+k) in nums[k+1:]:
                    n=[j,k,-j-k]
                    n.sort()
                    if n not in l:
                        l.append(n)
        return l