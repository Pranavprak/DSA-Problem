class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        # Solution 1
        # T - O(nlogn)
        # S - O(n)
        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
        # Solution 2
        # T - O(n)
        # S - O(n)
        freq = [ [] for i in range(len(nums)+1)]
        for num, counts in count.items():
            freq[counts].append(num)
        print(freq)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


        