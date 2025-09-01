from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left,right = 0,len(nums)-1
        result = [0]*len(nums)
        pos = len(nums)-1

        while left<=right:
            if abs(nums[left])>abs(nums[right]):
                result[pos]  = nums[left]**2
                left+=1
            else:
                result[pos] = nums[right]**2
                right-=1
            pos-=1

        return result            
        