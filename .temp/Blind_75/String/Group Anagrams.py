# https://leetcode.cn/problems/group-anagrams/submissions/
# Problem: 49. Group Anagrams


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()

        for word in strs:
            sword = tuple(sorted(word))
            d[sword] = d.get(sword, []) + [word]

        return list(d.values())