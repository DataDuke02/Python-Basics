class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)        # add to top    O(1)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()        # remove from top O(1)

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]          # view top O(1)

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

# Test
s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.peek())   # 30
print(s.pop())    # 30
print(s.pop())    # 20
print(s.size())   # 1
