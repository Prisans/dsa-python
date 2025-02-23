class SinglyNode:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        return str(self.val)

# Traversing Linked List

def display(head):
    curr = head
    element = []
    while curr:
        element.append(str(curr.val))
        curr = curr.next
    print('->'.join(element))

# Searching Linked List

def search(head, val):
    curr = head
    while curr:
        if val==curr.val:
            print("found")
        curr = curr.next
       
    

Head = SinglyNode(1)
A = SinglyNode(3)
B = SinglyNode(5)
C = SinglyNode(8)

Head.next = A
A.next = B
B.next = C
# print(Head)

# curr = Head

# while curr:
#     print(curr)
#     curr = curr.next

# display(Head)
# search(Head,5)


# Doubly Linked list

class DoublyNode:
    def __init__(self,val,next=None,prev=None):
        self.val = val
        self.next = next
        self.prev = prev
    
    def __str__(self):
        return str(self.val)

def traverse(head):
    curr=head
    element = []
    while curr:
        element.append(str(curr.val))
        curr = curr.next
    print("<->".join(element))

Head = Tail = DoublyNode(1)
print(Tail)
print(Head)

A = DoublyNode(2)
B = DoublyNode(5)
C = DoublyNode(7)

Head.next = A
A.next=B
A.prev=Head
B.next=C
B.prev=A
C.prev=B

traverse(Head)


# Do insertion and deletion practise 
