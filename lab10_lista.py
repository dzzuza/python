class Node:
 
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
 
    def __str__(self):
        return str(self.data)
 
class UnidirectionalList:
 
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
 
    def add(self, data):
        if not self.head:
            n = Node(data)
            self.head = n
        else:
            n = self.head
            while n.next != None:
                n = n.next
            new_node = Node(data)
            n.next = new_node;

   def FrontAdd(self, data):
     
    def printList(self):
        n = self.head
        while n:
            print (n)
            n = n.next
 
ll = UnidirectionalList()
ll.add(14)
ll.add("test")
ll.add(2.34)
ll.add(True)
 
ll.printList()
