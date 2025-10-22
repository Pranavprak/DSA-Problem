class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Brute Force
        # T - O(n^2)
        # S - O(1)
        result = []
        for index,num in enumerate(nums):
            product = 1
            for i in range(0,len(nums)):
                if i != index:
                    product *=nums[i]
            result.append(product)
        return result
    
        # Optimal Approach
        # T - O(n)
        # S - O(n)
        prefix = []
        suffix = [1] * len(nums)
        prefix.append(1)
        product = 1
        for i in range(len(nums)-1):
            product*=nums[i]
            prefix.append(product)
        product=1
        for i in range(len(nums)-2,-1,-1):
            product*=nums[i+1]
            suffix[i]=product
        result= [1] * len(nums)
        for i in range(len(nums)):
            result[i] = prefix[i] * suffix[i]
        return result
    
        # Space Optimized Approach
        # T - O(n)
        # S - O(1)
        result = [1] * len(nums)
        product = 1
        for i in range(len(nums)-1):
            product*=nums[i]
            result[i+1]*=product
        product=1
        for i in range(len(nums)-2,-1,-1):
            product*=nums[i+1]
            result[i]*=product
        return result


        