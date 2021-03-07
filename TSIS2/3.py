class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        totl = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    totl+=1
        return(totl)
