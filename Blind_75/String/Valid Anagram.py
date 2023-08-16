# https://leetcode.cn/problems/valid-anagram/description/

# Problem: 242. Valid Anagram
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        c1 = collections.Counter(s)
        c2 = collections.Counter(t)

        if len(c1) != len(c2):
            return False

        for k in c1.keys():
            if c1[k] != c2.get(k):
                return False

        return True