# https://leetcode.cn/problems/longest-palindrome/description/
# Problem: 409. Longest Palindrome

from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)

        count = 0
        odd = 0
        for c in counter.values():
            if c %2 == 0:
                count += c
            else:
                count += c-1
                odd = 1
        return count+ odd