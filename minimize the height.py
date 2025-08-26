<<<<<<< HEAD
class Solution:
    def getMinDiff(self, arr, k):
        n = len(arr)
        arr.sort()
        
        ans = arr[n-1]-arr[0]
        
        for i in range(n-1):
            high = max(arr[n-1]-k,arr[i]+k)
            low = min(arr[0]+k,arr[i+1]-k)
            
            if low<0:
                continue
            
            ans = min(ans,high-low)
        
=======
class Solution:
    def getMinDiff(self, arr, k):
        n = len(arr)
        arr.sort()
        
        ans = arr[n-1]-arr[0]
        
        for i in range(n-1):
            high = max(arr[n-1]-k,arr[i]+k)
            low = min(arr[0]+k,arr[i+1]-k)
            
            if low<0:
                continue
            
            ans = min(ans,high-low)
        
>>>>>>> 352790690d7fae7c4590aad2592897a2993c5a6c
        return ans