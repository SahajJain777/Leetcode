class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height)-1
        maxarea = 0

        while left<right:
            area = (right - left) * min(height[left],height[right])
            maxarea = max(area,maxarea)
            
            if height[left]< height[right]:
                left +=1
            else:
                right -=1
        
        return maxarea