from collections import deque

# QUEUE 
# - 2 Methods (Enqueue, Dequeue)
class Queue:
    def __init__(self):
        self.queue = deque()

    def is_empty(self):
        return len(self.queue) == 0
    
    # 1) enqueue (add to REAR)
    def enqueue(self, item):
        self.queue.append(item)

    # 2) dequeue (remove from HEAD)    
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty, cannot dequeue.")
        return self.queue.popleft()
    
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

# DEQUE (Double-Ended Queue) 
# - 4 Methods (Enqueue, Enqueue Head, Dequeue, Dequeue Rear)

class Deque:
    def __init__(self):
        self.deque = deque()

    def is_empty(self):
        return len(self.deque) == 0
    
    # 1) enqueue (add to REAR)
    def enqueue(self, item):
        self.deque.append(item)

    # 2) enqueue head (add to FRONT)
    def enqueue_head(self, item):
        self.deque.appendleft(item)

    # 3) dequeue (remove from FRONT)
    def dequeue(self):
        if self.is_empty():
            raise Exception("De-que is empty, cannot dequeue (head)")
        return self.deque.popleft()
    
    # 4) dequeue rear (remove from REAR)
    def dequeue_rear(self):
        if self.is_empty():
            raise Exception("De-que is empty, cannot dequeue (rear)")
        return self.deque.pop()
    
    def head(self):
        if self.is_empty():
            raise Exception("De-que is empty")
        return self.deque[0]
    
    def tail(self):
        if self.is_empty():
            raise Exception("De-que is empty")
        return self.deque[-1]
    
    def size(self):
        return len(self.deque)
    
    def display(self):
        return list(self.deque)
    
# ---------- Example De-quenemerut:
order_deque = Deque()

order_deque.enqueue("table 1")
order_deque.enqueue("table 2")
print("Current De-que: ", order_deque.display())

order_deque.enqueue_head("table 7")
print("Updated De-que: ", order_deque.display())

order_deque.dequeue()
print("Updated De-queue: ", order_deque.display())

order_deque.dequeue_rear()
print("Updated De-que: ", order_deque.display())