class Solution(object):
    def minimumRecolors(self, blocks, k):
        white = 0

        for i in range(k):
            if blocks[i] == 'W':
                white += 1

        ans = white

        left = 0
        for right in range(k, len(blocks)):
            if blocks[left] == 'W':
                white -= 1
            left += 1

            if blocks[right] == 'W':
                white += 1

            ans = min(ans, white)

        return ans  

        