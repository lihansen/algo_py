from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need, window = Counter(t), dict()

        left, right = 0, 0
        valid = 0 # number of characters in the window that matches the characters in t

        start = 0
        n = float('inf') # length of the minimum window

        while right < len(s):
            ch = s[right] # ch is the character to be added to the window
            right += 1 # window moves forward to the right

            if ch in need: # if ch is in t
                window[ch] = window.get(ch, 0) + 1 # add ch to the window
                if window[ch] == need[ch]: #  If the required count is reached
                    valid += 1 # Increment the valid counter

            while valid == len(need):  # shrink the window
                if right - left < n:
                    start = left
                    n = right - left

                d = s[left]  # Character to be removed from the window
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1

        return "" if n == float('inf') else s[start: start + n]