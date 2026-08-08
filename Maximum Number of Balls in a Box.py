class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        boxes = {}

        for num in range(lowLimit, highLimit + 1):
            temp = num
            total = 0

            while temp > 0:
                total += temp % 10
                temp //= 10

            boxes[total] = boxes.get(total, 0) + 1

        return max(boxes.values())
