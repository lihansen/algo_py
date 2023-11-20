# https://leetcode.cn/problems/palindromic-substrings/description/

# Problem: 647. Palindromic Substrings

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        res = 0

        for center in range(n):
            left = center
            right = center

            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1

                res += 1

            left = center
            right = center + 1

            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1

                res += 1

        return res

# manacher's algorithm