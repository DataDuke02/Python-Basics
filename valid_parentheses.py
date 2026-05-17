def valid_parentheses(s):
    stack = []
    mapping = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in s:
        if char in mapping:              # closing bracket
            if not stack:
                return False
            top = stack.pop()
            if mapping[char] != top:     # mismatch
                return False
        else:
            stack.append(char)           # opening bracket

    return len(stack) == 0              # stack must be empty at end

print(valid_parentheses("()[]{}"))   # True
print(valid_parentheses("([)]"))     # False
print(valid_parentheses("{[]}"))     # True
print(valid_parentheses("("))        # False
print(valid_parentheses(""))         # True
