class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:

        sorted_score = sorted(score, reverse=True)
        ans = []

        for i in score:
            rank = sorted_score.index(i)

            if rank == 0:
                ans.append("Gold Medal")
            elif rank == 1:
                ans.append("Silver Medal")
            elif rank == 2:
                ans.append("Bronze Medal")
            else:
                ans.append(str(rank + 1))

        return ans