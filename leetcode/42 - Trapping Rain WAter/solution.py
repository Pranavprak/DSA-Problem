class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = height[0]
        maxR = height[len(height)-1]
        l=0
        R=len(height)-1
        count = 0
        while l<R:
            if (maxL<=maxR):
                l+=1
                diff = maxL - height[l]
                if(diff > 0 ):
                    count+=diff
                maxL=max(height[l],maxL)
            else:
                R-=1
                diff= maxR - height[R]
                if(diff > 0):
                    count+=diff
                maxR = max(height[R],maxR)
        return count

        