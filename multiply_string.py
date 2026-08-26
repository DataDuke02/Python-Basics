class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        result = [0] * (len(num1) + len(num2))

        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):

                product = int(num1[i]) * int(num2[j])

                position = i + j + 1
                carry_position = i + j

                total = product + result[position]

                result[position] = total % 10
                result[carry_position] += total // 10

        # Remove leading zeros
        while result[0] == 0:
            result.pop(0)

        return "".join(map(str, result))
