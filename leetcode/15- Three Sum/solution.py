class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        numSort = sorted(nums)
        res = []
    
        for i,n in enumerate(numSort):
            if(n>0):
                break
            if(numSort[i-1] == n and i!=0):
                continue
            l = i+1
            r = len(numSort) - 1
            while l < r:          
                if numSort[i] + numSort[l] + numSort[r] == 0 :
                    res.append([numSort[i],numSort[l],numSort[r]])
                    l= l+1
                    while numSort[l-1] == numSort[l] and l<r:
                        l+=1
                elif numSort[i] + numSort[l] + numSort[r] < 0 :
                    l+=1
                else:
                    r-=1
        return res

        