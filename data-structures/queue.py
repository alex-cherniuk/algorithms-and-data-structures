class Queue:
    def __init__(self, size=25):
        self.container = []
        self.container_size = size
        
    def enqueue(self, value):
        if self.container_size:
            if len(self.container) >= self.container_size:
                raise IndexError(f"Can't enqueue {value}. Queue is overflow")
        self.container.append(value)
        
    def dequeue(self):
        try:
            first_value = self.container[0]
        except IndexError as error:
            raise IndexError("Can't dequeue first value. Queue is empty")
        else:
            del self.container[0]
            return first_value

    def __len__(self):
        return len(self.container)

    def __str__(self):
        def wrapper(arg):
            return '[ ' + arg + ' ]'
        return wrapper(" | ".join([str(elem) for elem in self.container]))
    
    
if __name__ == '__main__':
    queue = Queue(size=5)
    print("Size %2i, Queue: %s" %(len(queue), queue))
    
    for i in range(6):
        try:
            queue.enqueue(i)
            print("Size %2i, Queue: %s" %(len(queue), queue))
        except IndexError as error:
            print(error)
        
    for i in range(6):
        try:
            queue.dequeue()
            print("Size %2i, Queue: %s" %(len(queue), queue))
        except IndexError as error:
            print(error)
        
# Size  0, Queue: [  ]
# Size  1, Queue: [ 0 ]
# Size  2, Queue: [ 0 | 1 ]
# Size  3, Queue: [ 0 | 1 | 2 ]
# Size  4, Queue: [ 0 | 1 | 2 | 3 ]
# Size  5, Queue: [ 0 | 1 | 2 | 3 | 4 ]
# Can't enqueue 5. Queue is overflow
# Size  4, Queue: [ 1 | 2 | 3 | 4 ]
# Size  3, Queue: [ 2 | 3 | 4 ]
# Size  2, Queue: [ 3 | 4 ]
# Size  1, Queue: [ 4 ]
# Size  0, Queue: [  ]
# Can't dequeue first value. Queue is empty
