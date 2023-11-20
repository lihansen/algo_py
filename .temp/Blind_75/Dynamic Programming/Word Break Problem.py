# https://leetcode.cn/problems/word-break/description/
# Problem: 139. Word Break



class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)

        dp = [False for i in range(len(s) + 1)]

        dp[0] = True

        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        print(word_set, dp)
        return dp[len(s)]