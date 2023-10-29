from leetcode import *

# greedy

class Solution:
    def partitionLabels(s: str) -> List[int]:
        start = end = 0
        n = len(s)
        res = []

        last_occ = [0] * 26

        for i in range(n):
            ch = s[i]
            last_occ[ord(ch) - ord("a")] = i

        
        for i in range(n):
            ch = s[i]
            end = max(end , last_occ[ord(ch) - ord("a")])

            if end == i:
                res.append(end - start + 1)
                start = i + 1

        return res
    

print(Solution.partitionLabels("ababcbacadefegdehijhklij"))
