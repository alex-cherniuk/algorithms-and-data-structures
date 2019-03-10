class Stack:
    def __init__(self, size=25):
        self.container = []
        self.container_size = size
    
    def push(self, value):
        if len(self.container) >= self.container_size:
            raise IndexError(f"Can't push {value}. Stack is overflow")
        self.container.append(value)
        
    def pop(self):
        try:
            last_value = self.container[-1]
        except IndexError:
            raise IndexError("Can't pop last value. Stack is empty")
        else:
            del self.container[-1]
            return last_value
    
    def __len__(self):
        return len(self.container)

    def __str__(self):
        def wrapper(arg):
            return '[ ' + arg + ' ]'
        return "Size %2i, Stack: %s" %(self.__len__(), \
                                       wrapper(" | ".join([str(elem) for elem in self.container])))
    

if __name__ == '__main__':
    stack = Stack(size=5)
    print(stack)
    
    for i in range(6):
        try:
            stack.push(i)
            print(stack)
        except IndexError as error:
            print(error)
        
    for i in range(6):
        try:
            stack.pop()
            print(stack)
        except IndexError as error:
            print(error)
            
# Size  0, Stack: [  ]
# Size  1, Stack: [ 0 ]
# Size  2, Stack: [ 0 | 1 ]
# Size  3, Stack: [ 0 | 1 | 2 ]
# Size  4, Stack: [ 0 | 1 | 2 | 3 ]
# Size  5, Stack: [ 0 | 1 | 2 | 3 | 4 ]
# Can't push 5. Stack is overflow
# Size  4, Stack: [ 0 | 1 | 2 | 3 ]
# Size  3, Stack: [ 0 | 1 | 2 ]
# Size  2, Stack: [ 0 | 1 ]
# Size  1, Stack: [ 0 ]
# Size  0, Stack: [  ]
# Can't pop last value. Stack is empty
