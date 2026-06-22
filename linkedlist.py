class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def add_end(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = new
    def add_begin(self, data):
        obj=Node(data)
        if self.head is None:
            self.head = obj
            return
        obj.next = self.head
        self.head = obj
    def middle(self):
        slow=self.head
        fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        print(slow.data)
    def display(self):
        itr=self.head
        while itr:
            print(itr.data,end="-->")
            itr=itr.next
ll=LinkedList()
ll.add_end(50)
ll.add_end(150)
ll.add_end(250)
ll.add_end(350)
ll.add_end(450)
ll.add_end(550)
ll.add_end(650)
ll.add_begin(750)
ll.display()
print()
ll.middle() 