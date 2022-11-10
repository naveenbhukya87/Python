class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None
    
    def display(self):
        temp = self.head
        while temp:
            print(temp.data,end = " ==> ")
            temp = temp.next
        print("None")
    
    def insert_at_begin(self,data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def insert_at_end(self,data):
        node = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = node
    
    def insert_at_position(self,data,pos):
        node = Node(data)
        temp = self.head
        for i in range(pos-1):
            temp = temp.next
        node.next = temp.next
        temp.next = node
    
    def del_at_begin(self):
        temp = self.head
        self.head = temp.next
        del(temp)
    
    def del_at_end(self):
        pass




n1 = Node(10)
n2 = Node(20)
ll = SingleLinkedList()
ll.head = n1
n1.next = n2
ll.insert_at_begin(5)
ll.insert_at_end(30)
ll.insert_at_position(25,3)
ll.insert_at_position(15,2)
ll.del_at_begin()

ll.display()