from tkinter.messagebox import NO


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, end=" --> ")
                temp = temp.next
            print("None", end="")

    def insert_begining(self, data):
        node = Node(data)
        node.next = self.head
        self.head.prev = node
        self.head = node

    def insert_end(self, data):
        node = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = node
        node.prev = temp

    def insert_pos(self, data, pos):
        node = Node(data)
        temp = self.head
        for i in range(pos - 1):
            temp = temp.next
        node.next = temp.next
        temp.next.prev = node
        temp.next = node
        node.prev = temp

    def del_begin(self):
        temp = self.head
        self.head = self.head.next
        temp.next = None
        temp.prev = None
        self.head.prev = None

    def del_end(self):
        temp = self.head.next
        prev = self.head
        while temp.next != None:
            temp = temp.next
            prev = prev.next
        prev.next = None
        temp.next = None
        temp.prev = None

    def del_pos(self, pos):
        temp = self.head.next
        prev = self.head
        for i in range(pos - 1):
            temp = temp.next
            prev = prev.next
        prev.next = temp.next
        temp.next.prev = prev
        temp.next = None
        temp.prev = None

    def search(self, value):
        temp = self.head
        while temp:
            if temp.data == value:
                print(True)
                break
            temp = temp.next
        else:
            print(False)

    def reverseNodes(self):
        tempNode = self.head
        while tempNode.next:
            tempNode = tempNode.next
        while tempNode:
            print(tempNode.data, end=" --> ")
            tempNode = tempNode.prev
        print("None", end="")

    def middleNode(self):
        slow = self.head
        fast = self.head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        print(slow.data)
    
    def nth_from_end(self,pos):
        ref = self.head
        main = self.head
        count = 0
        while count < pos:
            ref =ref.next
            count = count + 1
        while ref != None:
            ref = ref.next
            main = main.next
        print(main.data)
    
    def delete_duplicate(self):
        rep = None
        fix = self.head
        while fix:
            rep = fix
            while rep.next:
                if fix.data == rep.next.data:
                    rep.next = rep.next.next
                else:
                    rep = rep.next
            fix = fix.next
        


dll = DoubleLinkedList()

n1 = Node(10)


dll.head = n1
n2 = Node(20)
dll.head.next = n2
n2.prev = dll.head

n3 = Node(30)
n2.next = n3
n3.prev = n2
# dll.display()
# print("\n ===================================")

dll.insert_begining(5)
dll.insert_begining(6)
dll.insert_end(40)
dll.insert_pos(25, 3)
dll.insert_pos(35, 5)
dll.insert_pos(25, 3)
dll.insert_pos(35, 5)
dll.insert_pos(25, 3)
dll.insert_pos(35, 5)
# dll.del_begin()
# dll.del_end()
# dll.del_pos(2)
# dll.search(30)

dll.display()
print("\n =================Before Mid Node==================")
# dll.middleNode()
dll.reverseNodes()
# # dll.search(30)
# print("\n ==================Mid Node=================")
# dll.middleNode()
# dll.nth_from_end(2)
dll.delete_duplicate()
print("\n ==================After del dup=================")
dll.display()

