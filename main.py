class Queue:
    def __init__(self,size):
        self.size = size
        self.queue = []

    def enqueue(self,item):
        if len(self.queue) <= self.size:
            self.queue.append(item)
        else:
            print("Queue is full")
    
    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        elif len(self.queue) == 0:
            print("No items in queue")
    
    def clear_queue(self):
        if len(self.queue) > 0:
            self.queue = []
        elif len(self.queue) == 0:
            print("Nothing to clear in queue")

    def head(self):
        return self.queue[0]
    
    def tail(self):
        return self.queue[-1]
    
    def length(self):
        return len(self.queue)
    
    def display(self):
        print(self.queue)

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


    

    



        