class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def print_list(self):
            current_node = self.head
            while current_node:
                print(current_node.data, end=" -> ")
                current_node = current_node.next
            print("X") # Indicates the end of the list

    # ---------- Basic Functions (PPT):
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node    
        else:
            self.tail = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            else:
                current_node = current_node.next
        return False
    
    # ------- Linked List Assignment:

    # a. remove_beginning()
    def remove_beginning(self):
        if self.head is None:
            return ("List is empty.")
        
        removed_head = self.head.data
        self.head = self.head.next
        print(f"\nREMOVED BEGINNING '{removed_head}':")

    # b. remove_at_end()
    def remove_at_end(self):
        if self.tail is None:
            return("List is empty.")
        
        current_node = self.head
        while current_node.next.next:
            current_node = current_node.next

        removed_tail = current_node.next.data
        current_node.next = None
        self.tail = current_node
        print(f"\nREMOVED END '{removed_tail}':")

    def remove_at(self, data):
        if self.head is None:
            return("List is empty.")
        
        # if head is removed
        if self.head.data == data:
            removed = self.head.data
            self.head = self.head.next
            if not self.head:
                self.tail = None
            print(f"\nREMOVED '{removed}':")
            return
        
        current_node = self.head
        while current_node.next:
            if current_node.next.data == data:
                removed = current_node.next.data
                current_node.next = current_node.next.next
                if current_node.next is None:
                    self.tail = current_node
                print(f"\nREMOVED '{removed}':")
                return
            current_node = current_node.next
            
        print(f"\nREMOVED: '{data}' not in list.")

# ------------- Forming the List:
sushi_preparation = LinkedList()

sushi_preparation.insert_at_end("prepare")
sushi_preparation.insert_at_end("roll")
sushi_preparation.insert_at_beginning("assemble")

print("LINKED LIST:")
sushi_preparation.print_list()

# a. remove_beginning()
sushi_preparation.remove_beginning()
sushi_preparation.print_list()

# b. remove_at_end()
sushi_preparation.remove_at_end()
sushi_preparation.print_list()

# c. remove_at()
sushi_preparation.remove_at("wrapping")
sushi_preparation.remove_at("prepare")
sushi_preparation.print_list()