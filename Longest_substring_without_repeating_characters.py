class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        longest=0
        hash={}
        for r,c in enumerate(s):
            if c in hash:
                l=max(l,hash[c]+1)
            hash[c]=r
            longest=max(longest,r-l+1)
        return longest
