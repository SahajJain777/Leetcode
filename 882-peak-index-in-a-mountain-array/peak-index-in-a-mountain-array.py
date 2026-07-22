class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr)-1
        mid = 0

        while(left<right):
            mid = (left+right)//2
            if arr[mid] < arr[mid+1]:
                left = mid+1
            if arr[mid] > arr[mid+1]:
                right = mid
        
        return left