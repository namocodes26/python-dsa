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
          
        
       
       