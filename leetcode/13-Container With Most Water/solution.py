class Solution:
    def maxArea(self, height: List[int]) -> int:
        volume = 0
        l= 0
        r= len(height) - 1
        while l<r:
            diff = r-l
            product = min(height[l],height[r])*diff
            volume = max(product,volume)
            if(height[l]>height[r]):
                r-=1
            else:
                l+=1
        return volume
        