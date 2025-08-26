<<<<<<< HEAD
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        lis =[]
        dic = {}

        for i in range(n):
            if nums[i] in dic:
                dic[nums[i]]+=1
            else:
                dic[nums[i]]=1
        
        for key,value in dic.items():
            if value > n//3:
                lis.append(key)
        
        lis.sort()
=======
from typing import list
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        lis =[]
        dic = {}

        for i in range(n):
            if nums[i] in dic:
                dic[nums[i]]+=1
            else:
                dic[nums[i]]=1
        
        for key,value in dic.items():
            if value > n//3:
                lis.append(key)
        
        lis.sort()
>>>>>>> 352790690d7fae7c4590aad2592897a2993c5a6c
        return lis