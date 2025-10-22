
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Solution 1
        # Time complexity: O(m*nlogn)
        # Space complexity: O(m∗n)
        # res = defaultdict(list)
        # for s in strs:
        #     sortedS = ''.join(sorted(s))
        #     res[sortedS].append(s)
        # return list(res.values())
        # Solution 2
        # Time complexity: O(m∗n)
        # Space complexity: O(m∗n)
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())