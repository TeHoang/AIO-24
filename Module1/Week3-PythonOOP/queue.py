class MyQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.store = []

    def is_empty(self):
        return len(self.store) == 0

    def is_full(self):
        return len(self.store) == self.capacity

    def dequeue(self):
        return self.store.pop()

    def enqueue(self, value):
        self.store = [value] + self.store

    def front(self):
        return self.store[-1]


queue1 = MyQueue(capacity=5)

queue1.enqueue(1)

queue1.enqueue(2)

print(queue1.is_full())
# False

print(queue1.front())
# 1

print(queue1.dequeue())
# 1

print(queue1.front())
# 2

print(queue1.dequeue())
# 2

print(queue1.is_empty())
# True
