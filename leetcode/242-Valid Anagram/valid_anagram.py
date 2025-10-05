class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # Solution 1
        #Time O(nlogn)
        # Space O(n)
        first = ''.join(sorted(s))
        second = ''.join(sorted(t))
        if(first == second):
            return True
        else:
            return False
        #Solution 2
        # Time O(n)
        # Space O(1)
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT

        