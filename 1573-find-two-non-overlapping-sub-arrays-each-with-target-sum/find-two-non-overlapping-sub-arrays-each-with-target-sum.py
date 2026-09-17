class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        prefix = 0
        ans = 1000000

        freq = {0: 0}
        best = [1000000] * (n + 1)

        for i in range(n):
            prefix += arr[i]

            if prefix - target in freq:
                start = freq[prefix - target]
                length = i + 1 - start

                if best[start] != 1000000:
                    ans = min(ans, best[start] + length)

                best[i + 1] = min(best[i], length)
            else:
                best[i + 1] = best[i]

            freq[prefix] = i + 1

        if ans == 1000000:
            return -1

        return ans