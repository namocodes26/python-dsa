from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        nonzero = 0
        for i in range(n):
            if nums[i] != 0:
                nums[i],nums[nonzero]=nums[nonzero],nums[i]
                nonzero+=1


        