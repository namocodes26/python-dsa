<<<<<<< HEAD
class Solution:
    def maxSubarraySum(self, arr):
       n = len(arr)
       total = 0
       maxi = arr[0]
       for i in range(0,n):
           total+=arr[i]
           maxi = max(total,maxi)
           
           if total < 0:
               total = 0
    
           
       return maxi
          
        
       
=======
class Solution:
    def maxSubarraySum(self, arr):
       n = len(arr)
       total = 0
       maxi = arr[0]
       for i in range(0,n):
           total+=arr[i]
           maxi = max(total,maxi)
           
           if total < 0:
               total = 0
    
           
       return maxi
          
        
       
>>>>>>> 352790690d7fae7c4590aad2592897a2993c5a6c
       