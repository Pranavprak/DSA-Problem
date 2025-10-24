class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s=s.lower()
        # cleaned = "".join([c for c in s if c.isalnum()])
        # for i in range(len(cleaned)):
        #     if cleaned[i] != cleaned[-(i+1)]:
        #         return False
        # return True
        s=s.lower()
        l,r = 0, len(s)-1
        while l<r:
            if not s[l].isalnum():
                l+=1
                continue
            if not s[r].isalnum():
                r-=1
                continue
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        return True
        