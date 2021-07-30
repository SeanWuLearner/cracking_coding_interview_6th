
class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList():

    def __init__(self, datas):
        self.head = self._build(datas)

    def _build(self, datas):
        head = None
        prev = None
        for d in datas:
            node = Node(d)
            if head == None:
                head = node
            if prev != None:
                prev.next = node
            prev = node
        return head

    def __str__(self):
        node = self.head
        s = ""
        while node != None:
            s += str(node.data)
            if node.next != None:
                s += ' -> '
            node = node.next
        return s

    def __eq__(self, x):
        print(f'{self} compare {x}')
        return self.__str__() == x.__str__()

    def find(self, n):
        node = self.head
        while node != None:
            if node.data == n:
                return node
            node = node.next
        return None
