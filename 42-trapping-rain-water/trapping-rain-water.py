class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right= len(height)-1
        res = 0
        MaxLeft = -1
        MaxRight = -1
        while left<right:
            
            if height[left]<=height[right]:
                MaxLeft = max(height[left],MaxLeft)
                res+= MaxLeft - height[left]
                left+=1
            if height[left]>height[right]:
                MaxRight = max(height[right],MaxRight)
                res+= MaxRight - height[right]
                right-=1

        return res



        