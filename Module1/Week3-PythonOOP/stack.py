class MyStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.store = []

    def is_empty(self):
        return len(self.store) == 0

    def is_full(self):
        return len(self.store) == self.capacity

    def pop(self):
        return self.store.pop()

    def push(self, value):
        self.store.append(value)

    def top(self):
        return self.store[-1]


stack1 = MyStack(capacity=5)

stack1.push(1)

stack1.push(2)

print(stack1.is_full())
# False

print(stack1.top())
# 2

print(stack1.pop())
# 2

print(stack1.top())
# 1

print(stack1.pop())
# 1

print(stack1.is_empty())
# True
