class Solution:
    def checkStraightLine(self, coordinates):
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]

        for i in range(2, len(coordinates)):
            x3, y3 = coordinates[i]

            if (y2 - y1) * (x3 - x1) != (y3 - y1) * (x2 - x1):
                return False

        return True

  Input:
coordinates = [[1,2],[2,3],[3,4],[4,5]]

Output:
True
