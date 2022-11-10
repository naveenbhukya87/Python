class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
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

    def atBegining(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def atEnd(self, data):
        temp = self.head
        node = Node(data)
        while temp.next:
            temp = temp.next
        temp.next = node

    def atPosition(self, data, pos):
        temp = self.head
        node = Node(data)
        for i in range(pos - 1):
            temp = temp.next
        node.next = temp.next
        temp.next = node

    def delAtBeginning(self):
        temp = self.head
        self.head = temp.next
        temp.next = None

    def delAtEnd(self):
        temp = self.head.next
        prev = self.head
        while temp.next is not None:
            temp = temp.next
            prev = prev.next
        prev.next = None

    def delAtPos(self, pos):
        temp = self.head.next
        prev = self.head
        for i in range(pos - 1):
            temp = temp.next
            prev = prev.next
        prev.next = temp.next
        temp.next = None

    def search(self, value):
        temp = self.head
        while temp:
            if temp.data == value:
                print(True)
                break
            temp = temp.next
        else:
            print(False)

    def reverse(self):
        temp = self.head
        prevNode = None
        nextNode = None
        while temp:
            nextNode = temp.next
            temp.next = prevNode
            prevNode = temp
            temp = nextNode
        self.head = prevNode
        temp = self.head
        while temp:
            print(temp.data, end=" --> ")
            temp = temp.next
        print("None", end="")

    def midddleNode(self):
        slow = self.head
        fast = self.head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        print(slow.data)

    def nth_from_end(self, pos):
        ref = self.head
        main = self.head
        count = 0
        while count < pos:
            ref = ref.next
            count = count + 1
        while ref != None:
            ref = ref.next
            main = main.next
        print(main.data)

    def remove_adjacent_duplicates(self):
        temp = self.head
        # dup = self.head
        while temp.next:
            if temp.data == temp.next.data:
                temp.next = temp.next.next
                # dup.next.next = None
            else:
                temp = temp.next
                # dup = dup.next


    def removeDuplicates(self):
        fix = self.head
        rep = None
        dup = []
        while fix:
            rep = fix
            while rep.next:
                if fix.data == rep.next.data:
                    dup.append(fix.data)
                    rep.next = rep.next.next
                else:
                    rep = rep.next
            fix = fix.next
        # self.display()
        # print("\n",dup)
        


ll = LinkedList()

n0 = Node(10)
ll.head = n0

n1 = Node(20)
n2 = Node(30)
n3 = Node(40)

ll.head.next = n1
n1.next = n2
n2.next = n3
ll.atBegining(1)
ll.atBegining(2)
ll.atBegining(3)
ll.atBegining(4)
ll.atBegining(5)
ll.atBegining(6)
ll.atBegining(6)
ll.atBegining(6)
ll.atBegining(6)
ll.atEnd(50)
ll.atPosition(35, 4)
ll.atPosition(35, 4)
ll.atPosition(35, 4)
ll.atPosition(30, 4)
ll.atPosition(10, 4)
ll.atPosition(1, 4)


# ll.delAtBeginning()
# ll.delAtEnd()
# ll.delAtPos(3)
# ll.search(35)

ll.display()
# print("\n")
# ll.midddleNode()
# print("\n")
# ll.reverse()
# print("\n")
# ll.midddleNode()
# print("\n")
# ll.reverse()
# print("\n")
# ll.midddleNode()
# print("\n")
# ll.nth_from_end(3)

print("\n")
print("\n")
ll.remove_adjacent_duplicates()
ll.display()
ll.removeDuplicates()
print("\n")
print("\n")
ll.display()
