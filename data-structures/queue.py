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