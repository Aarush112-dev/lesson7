class Stack():
    def __init__(self,max):
        self.max = max
        self.stack = []

    def add(self,n):
        if len(self.stack) >= self.max:
            print("Stack is full")
        else:
            self.stack.append(n)

    def pop(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:    
            return self.stack.pop(0)

    def top(self):
        return self.stack[-1]
    
    def rear(self):
        return self.stack[0]
    
    def size(self):
        return len(self.stack)
    
    def clear(self):
        self.stack = []
    
    def display(self):
        print(self.stack)

class Queue:
    def __init__(self,size):
        self.size = size
        self.queue = Stack(size)
        self.queue2 = Stack(size)

    def enqueue(self,item):
        if self.queue.size() >= self.size:
            print("Queue is full")
        else:
            self.queue.add(item)
    
    def dequeue(self):
        self.queue.pop()
    
    def clear_queue(self):
        if self.queue.size() > 0:
            self.queue.clear()
        elif self.queue.size() == 0:
            print("Nothing to clear in queue")

    def head(self):
        self.queue.rear()
    
    def tail(self):
        self.queue.top()
    
    def length(self):
        self.queue.size()
    
    def display(self):
        self.queue.display()

queue = Queue(14)
queue.enqueue(10)
queue.enqueue(5)
queue.enqueue(17)
queue.enqueue(21)
queue.enqueue(53)
queue.enqueue(47)
queue.dequeue()
queue.clear_queue()
queue.enqueue(17)
queue.enqueue(21)
queue.enqueue(53)
print(queue.head())
print(queue.tail())
print(queue.length())
queue.display()
