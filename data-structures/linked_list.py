class LinkedListNode:
    def __init__(self, data):
        self.data = data      # contains the data
        self.next = None      # contains the reference to the next node
        self.previous = None  # contains the reference to the previous node


class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert(self, value):
        node = LinkedListNode(value)
        if self.head:
            node.previous = self.head
            self.head.next = node
        self.head = node
           
    def remove(self, value):
        current_node = self.head
        found = False
        while current_node is not None and not found:
            if current_node.data == value:
                found = True
                if current_node.previous:
                    if current_node.next:
                        # We are in the middle of the list
                        current_node.previous.next = current_node.next
                        current_node.next.previous = current_node.previous
                    else:
                        # We are in the head
                        current_node.previous.next = None
                        self.head = current_node.previous
                else:
                    if current_node.next:
                        # We are in the tail
                        current_node.next.previous = None 
                    else:
                        # It is a list with only one node. Just remove head.
                        self.head = None
            else:
                current_node = current_node.previous
        if not found:
            print(f"Value {value} is not in the list")   
            
    def __get_values(self):
        values = []
        if self.head:
            node = self.head
            while True:
                values.append(node.data)
                if node.previous:
                    node = node.previous
                else:
                    break
        return values
    
    def __str__(self):            
        return " -> ".join([str(elem) for elem in self.__get_values()])
    

if __name__ == '__main__':
    linked_list = LinkedList()
    for i in range(5):
        linked_list.insert(i)
        print(linked_list)
    linked_list.insert(4)
    print(linked_list)
    linked_list.remove(4)
    print(linked_list)
    linked_list.remove(4)
    print(linked_list)
    linked_list.remove(4)
    linked_list.remove(0)
    print(linked_list)
    

# 0
# 1 -> 0
# 2 -> 1 -> 0
# 3 -> 2 -> 1 -> 0
# 4 -> 3 -> 2 -> 1 -> 0
# 4 -> 4 -> 3 -> 2 -> 1 -> 0
# 4 -> 3 -> 2 -> 1 -> 0
# 3 -> 2 -> 1 -> 0
# Value 4 is not in the list
# 3 -> 2 -> 1
