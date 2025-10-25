class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

def precedence(char): # order of characters
    if char == '^':
        return 3
    elif char in '*/':
        return 2
    elif char in '+-':
        return 1
    return 0

def is_operand(char):
    return char.isalnum()  # Accepts a-z, A-Z, 0-9

# convert infix to postfix
def infix_to_postfix(expression, stack):
    postfix = []
    for char in expression:
        if char == ' ':
            continue
        if is_operand(char):
            postfix.append(char)
        elif char == '(':
            stack.push(char)
        elif char == ')':
            while not stack.is_empty() and stack.peek() != '(':
                postfix.append(stack.pop())
            stack.pop()  # Pop the '('
        else:
            while (not stack.is_empty()) and (precedence(char) <= precedence(stack.peek())):
                postfix.append(stack.pop())
            stack.push(char)

    while not stack.is_empty():
        postfix.append(stack.pop())

    return ' '.join(postfix)

infix_expression = input("Enter Infix Expression:")
stack = Stack()
postfix_expression = infix_to_postfix(infix_expression, stack)
print("Postfix Expression:", postfix_expression)