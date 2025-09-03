from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
    
        for i in range(n):
            if i != 0 and nums[i] == nums[i-1]:
                continue 
            j = i+1
            k = n-1


            while j < k :
                temp = nums[i] + nums[j] + nums[k]
                if temp < 0 :
                    j+=1
                elif temp > 0 :
                    k-=1
                
                else :
                    arr = [nums[i],nums[j],nums[k]]
                    ans.append(arr)
                    j+=1
                    k-=1
                
                    while j < k and nums[j] == nums [j-1]:
                        j+=1
                
                    while j <k and nums[k] == nums[k+1]:
                        k-=1
        
        return ans 
        




        