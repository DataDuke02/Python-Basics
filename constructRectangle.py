class Solution:
    def constructRectangle(self, area: int):
        length = area
        width = 1

        while width * width <= area:
            if area % width == 0:
                length = area // width
            width += 1

        return [length, width - 1]
