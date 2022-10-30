class Node:
    def __init__(self, value=None, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def pushBack(self, newNodeElement):
        if self.tail == self.head is None:
            self.tail = self.head = newNodeElement

            return

        if self.head is self.tail:
            self.head.next = newNodeElement
            self.tail = newNodeElement
            self.tail.prev = self.head

            return

        currTail = self.tail
        self.tail.next = newNodeElement
        self.tail = newNodeElement
        self.tail.prev = currTail

    def popFront(self):
        if self.tail == self.head is None:
            return

        if self.tail is self.head:
            self.tail = self.head = None
            return

        self.head = self.head.next

    def popEnd(self):
        if self.tail == self.head is None:
            return

        if self.tail is self.head:
            self.tail = self.head = None
            return

        if self.head.next is self.tail:
            self.head.next = None
            self.tail = self.head
            return

        self.tail = self.tail.prev
        self.tail.next = None

    def displayList(self):
        if self.head == self.tail is None:
            return

        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

        print(f"head {self.head.value}", f"tail {self.tail.value}")

    def reverseLinkedList(self):
        # a -> b -> c -> None
        # b -> a -> None
        curr = self.head
        currPrev = None
        while curr is not None:
            currPrev = curr.prev
            curr.prev = curr.next
            curr.next = currPrev
            curr = curr.prev

        if currPrev is not None:
            self.head = currPrev.prev


node1 = Node(5)
node2 = Node(15)
node3 = Node(25)

list = LinkedList()

list.pushBack(node1)
list.pushBack(node2)
list.pushBack(node3)

list.reverseLinkedList()

list.displayList()
