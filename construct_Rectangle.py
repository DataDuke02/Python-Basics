class Solution:
    def constructRectangle(self, area: int):
        for w in range(area, 0, -1):
            if area % w == 0:
                l = area // w
                if l >= w:
                    return [l, w]
