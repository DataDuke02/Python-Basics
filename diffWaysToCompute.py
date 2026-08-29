class Solution:
    def diffWaysToCompute(self, expression: str):
        result = []

        for i in range(len(expression)):
            if expression[i] in "+-*":
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i + 1:])

                for a in left:
                    for b in right:
                        if expression[i] == "+":
                            result.append(a + b)
                        elif expression[i] == "-":
                            result.append(a - b)
                        else:
                            result.append(a * b)

        # If there is no operator, the expression is just a number
        if not result:
            result.append(int(expression))

        return result

  
