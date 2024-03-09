class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def push(self, item):
        if not self.isFull():
            self.items.append(item)
        else:
            raise IndexError("Stack is full")

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")

    def isEmpty(self):
        return len(self.items) == 0

    def isFull(self):
        return len(self.items) == self.capacity

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def insert(self, item):
        if not self.isFull():
            self.items.insert(0, item)
        else:
            raise IndexError("Queue is full")

    def remove(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            raise IndexError("Queue is empty")

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            raise IndexError("Queue is empty")

    def isEmpty(self):
        return len(self.items) == 0

    def isFull(self):
        return len(self.items) == self.capacity

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


def FunnyString(input_string):
    stack = Stack(len(input_string))
    queue = Queue(len(input_string))
    result = []

    for char in input_string:
        stack.push(char)
        queue.insert(char)

    while not stack.isEmpty():
        result.append(stack.pop())

    result.append(' ')

    while not queue.isEmpty():
        result.append(queue.remove())

    # Combine characters into a string, split the words, reverse the characters within each word, and join them back
    words = ''.join(result).split()
    reversed_words = [''.join(word[::-1]) for word in words]
    reversed_phrase = ' '.join(reversed_words)

    return reversed_phrase
