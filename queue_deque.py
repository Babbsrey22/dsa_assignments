from collections import deque

class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0
    
    # 1) enqueue (FROM THE REAR) ---- QUEUE
    def enqueue(self, item):
        self.queue.append(item)

    # 2) dequeue (FROM THE FRONT) ---- QUEUE    
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty, cannot dequeue.")
        return self.queue.pop(0)
    
    def head(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.queue[0] # shows 'none' lagi huhu
    
    def tail(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.queue[-1]
    
    def size(self):
        return len(self.queue)
    
    def display(self):
        return list(self.queue)
    
    def __str__(self):
        return f"Queue({list(self.queue)})"

# ----- Example Queuenemerut toooo:
grocery_list = Queue()

grocery_list.enqueue("eggs")
grocery_list.enqueue("kamatis")
grocery_list.enqueue("milk")
grocery_list.enqueue("milk pero bear brand na powder")
grocery_list.enqueue("bawang")

print("Initial queue: ", grocery_list.display())

print(f"Removed {grocery_list.dequeue()}.") # remove eggs
print("Updated queue: ", grocery_list.display())

grocery_list.enqueue('SILIIII')
print(f"Added {grocery_list.tail()}")
print("Updated queue: ", grocery_list.display())