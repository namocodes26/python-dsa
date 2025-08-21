from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        freq_map = {}
        n = len(nums)

        for i in range(0,n):
            freq_map[nums[i]]=0
        k = 0 
        for j in freq_map:
            nums[k] = j
            k+=1
        
        return k
        