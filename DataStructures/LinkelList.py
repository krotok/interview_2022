class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,value):
        if not self.head:
            self.head = Node(value)
            return

        cur = self.head
        while cur.next:
            cur = cur.next

        cur.next = Node(value)

    def to_list(self):
       cur_list = []
       cur = self.head
       while cur:
            cur_list.append(cur.value)
            cur = cur.next
       return cur_list

ll = LinkedList()
ll.append(5)
ll.append(6)
print(ll.to_list())