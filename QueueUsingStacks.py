class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []   # for enqueue
        self.stack2 = []   # for dequeue

    def enqueue(self, data):
        self.stack1.append(data)      # always push to stack1

    def dequeue(self):
        if not self.stack2:           # stack2 empty — refill
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            return None
        return self.stack2.pop()

    def front(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            return None
        return self.stack2[-1]

# Test
q = QueueUsingStacks()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())   # 1
print(q.dequeue())   # 2
q.enqueue(4)
print(q.dequeue())   # 3
print(q.dequeue())   # 4
