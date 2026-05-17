from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, data):
        self.queue.append(data)         # add to rear   O(1)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.popleft()     # remove from front O(1)

    def front(self):
        if self.is_empty():
            return None
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


# Test
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.front())    # 10
print(q.dequeue())  # 10
print(q.dequeue())  # 20
print(q.size())     # 1
