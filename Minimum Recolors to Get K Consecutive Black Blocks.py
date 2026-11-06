class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        white = blocks[:k].count('W')
        min_recolors = white

        for i in range(k, len(blocks)):
            if blocks[i] == 'W':
                white += 1

            if blocks[i - k] == 'W':
                white -= 1

            min_recolors = min(min_recolors, white)

        return min_recolors
