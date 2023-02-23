class Solution: 
    def select(self, arr, i):
        # code here 
        n=len(arr)
        selectionSort(self,arr,n)
            
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(n-1):
            m=i
            for j in range(i+1,n):
                if arr[j]<arr[m]:
                    m=j
            if m!=i:
                arr[i],arr[m]=arr[m],arr[i]
                
