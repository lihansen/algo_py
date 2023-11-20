# https://leetcode.cn/problems/combination-sum/description/
# Problem: 39. Combination Sum


def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    res = []
    self.helper(candidates, target, res, [], 0)
    return res


def helper(self, candidates, target, res, combins, start):
    # if target < 0:
    #     return
    if target == 0:
        res.append(combins[::])
    else:
        for i in range(start,
                       len(candidates)):  # make sure do not use the previous elems in the candidates, reduce duplicates
            cand = candidates[i]
            combins.append(cand)
            if target - cand >= 0:
                self.helper(candidates, target - cand, res, combins, i)
            combins.pop()
