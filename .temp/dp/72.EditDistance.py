# You have the following three operations permitted on a word:
#
# Insert a character
# Delete a character
# Replace a character

# example:
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation:
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')


def minDistance(word1: str, word2: str) -> int:
    l1 = len(word1)
    l2 = len(word2)

    # one of the string is empty, so return another word length
    if l1 * l2 == 0:
        return l1 + l2

    # dp[*][0] or dp[0][*] represents one of the strings is empty
    dp = [[0 for i in range(l2 + 1)] for j in range(l1 + 1)]

    for i in range(l1 + 1):
        dp[i][0] = i

    for j in range(l2 + 1):
        dp[0][j] = j

    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(
                    dp[i - 1][j],
                    dp[i][j - 1],
                    dp[i - 1][j - 1], # replace
                ) + 1

    return dp[l1][l2]


res = minDistance("horse", "ros")
print(res)
