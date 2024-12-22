class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        left = 0
        right = len(height)-1

        while left<right:
            area = (right-left)*min(height[left],height[right])

            if height[left]<height[right]:
                left+=1
            else:
                right-=1
            max_water = max(area,max_water)


        return max_water

        