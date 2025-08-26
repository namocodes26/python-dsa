class Solution:
    def getMinDiff(self, arr, k):
        n = len(arr)
        arr.sort()
        
        ans = arr[-1] - arr[0]   # initial difference
        
        for i in range(n-1):
            high = max(arr[-1] - k, arr[i] + k)
            low = min(arr[0] + k, arr[i+1] - k)
            
            if low < 0:   # skip if negative
                continue
                
            ans = min(ans, high - low)
        
        return ans
