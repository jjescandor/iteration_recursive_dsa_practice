from data_structures.node import Node

class LinkedList:

  def __init__(self):
    self.head = None

  def __str__(self):
    shape = ""
    curr = self.head
    while curr:
      shape += f"{curr.value} -> "
      curr = curr.next
    return shape


  def add(self, value):
    node = Node(value)

    if self.head is None:
      self.head = node
      return

    current = self.head
    while current.next is not None:
      current = current.next

    current.next = node

  
