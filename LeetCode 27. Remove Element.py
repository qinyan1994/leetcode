class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        s=0
        for i in nums:
            if i!=val:
                nums[s]=i
                s+=1
        return s