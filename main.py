try:
    from data_structures.node import Node
    from data_structures.linked_list import LinkedList
    from data_structures.stack import Stack
    from data_structures.queue import Queue
    from data_structures.binary_tree import BinaryTree
    from data_structures.binary_search_tree import BinarySearchTree
except:
    from .data_structures.node import Node
    from .data_structures.linked_list import LinkedList
    from .data_structures.stack import Stack
    from .data_structures.queue import Queue
    from .data_structures.binary_tree import BinaryTree
    from .data_structures.binary_search_tree import BinarySearchTree


# Iterate a linked list iteratively and return the largest value
# input_linked_list (7)->(2)->(13)->(9)->(3)
def iterate_linkedlist_iteratively(input_linked_list):
    curr = input_linked_list.head
    max = curr.value
    while curr:
        if curr.value > max:
            max = curr.value
        curr = curr.next
    return max


# ##################### NEW #####################################
# Write a test to cover this
# Iterate through a linked list iteratively and return the smallest value
# input_linked_list (7)->(2)->(13)->(9)->(3)
def iterate_linkedlist_iteratively_small(input_linked_list):
    curr = input_linked_list.head
    min = curr.value
    while curr:
        if curr.value < min:
            min = curr.value
        curr = curr.next
    return min


# ##################### NEW #####################################
# Write a test to cover this
# Iterate through a linked list iteratively and remove duplicate values
# input_linked_list (7)->(2)->(13)->(2)->(9)->(3)->(9)

def iterate_linkedlist_iteratively_duplicates(input_linked_list1):
    curr = input_linked_list1.head
    prev = None
    unique = []
    while curr:
        if curr.value in unique:
            prev.next = curr.next
        else:
            unique.append(curr.value)
            prev = curr
        curr = curr.next
    return input_linked_list1


# ##################### NEW #####################################
# Write a test to cover this
# Iterate through a linked list, and return the value furthest removed from zero
# input_linked_list (7)->(2)->(13)->(-9)->(3)->(-21)

def iterate_linkedlist_furthest_from_zero(input_linked_list):
    curr = input_linked_list.head
    max = curr.value
    min = curr.value
    while curr:
        if curr.value > max:
            max = curr.value
        if curr.value < min:
            min = curr.value
        curr = curr.next
    return max if max > abs(min) else min


# Iterate a linked list recursively and return the largest value
# input_linked_list (7)->(2)->(13)->(9)->(3)
def iterate_linkedlist_recursively(input_node, largest=0):
    if input_node:
        if input_node.value > largest:
            largest = input_node.value
        return iterate_linkedlist_recursively(input_node.next, largest)
    else:
        return largest


# ##################### NEW #####################################
# Write a test to cover this
# Iterate through a linked list recursively and return the largest value
# input_linked_list (7)->(2)->(13)->(9)->(3)
def iterate_linkedlist_recursively_smallest(input_node, smallest=0):
    if input_node:
        if input_node.value < smallest:
            smallest = input_node.value
        return iterate_linkedlist_recursively_smallest(input_node.next, smallest)
    return smallest


# Iterate a stack iteratively and return the largest value
# input_stack (7)->(2)->(13)->(9)->(3)
def iterate_stack_iteratively(input_stack):
    max = input_stack.top.value
    while not input_stack.is_empty():
        if input_stack.top.value > max:
            max = input_stack.top.value
        input_stack.pop()
    return max


# Iterate a stack recursively and return the largest value
# input_stack (7)->(2)->(13)->(9)->(3)
def iterate_stack_recursively(input_stack, largest=0):
    if not input_stack.is_empty():
        if input_stack.top.value > largest:
            largest = input_stack.top.value
        input_stack.pop()
        return iterate_stack_recursively(input_stack, largest)
    return largest


# Iterate a queue iteratively and return the largest value
# input_queue (7)->(2)->(13)->(9)->(3)
def iterate_queue_iteratively(input_queue):
    max=input_queue.front.value
    while not input_queue.is_empty():
        if input_queue.front.value > max:
            max = input_queue.front.value
        input_queue.dequeue()
    return max


# Iterate a queue recursively and return the largest value
# input_queue (7)->(2)->(13)->(9)->(3)
def iterate_queue_recursively(input_queue, largest=0):
    if input_queue.is_empty():
        return largest
    else:
        if input_queue.front.value > largest:
            largest = input_queue.front.value
        input_queue.dequeue()
        return iterate_queue_recursively(input_queue, largest)


# Perform a Pre-Order, In-Order, and Post-Order traversal of a binary tree.
#                       4
#                     /   \
#                   7      18
#                 /   \   /   \
#                3     1 5     11
#
# Pre-Order Traveral
# expected [4, 7, 3, 1, 18, 5, 11]
def pre_order_traversal(input_node, values=[]):
    if not input_node:
        return
    values.append(input_node.value)
    pre_order_traversal(input_node.left, values)
    pre_order_traversal(input_node.right, values)
    return values


# In-Order Traveral
# expected [3, 7, 1, 4, 5, 18, 11]
def in_order_traversal(input_node, values=[]):
    if not input_node:
        return
    in_order_traversal(input_node.left, values)
    values.append(input_node.value)
    in_order_traversal(input_node.right, values)
    return values


# Post-Order Traveral
# expected [3, 1, 7, 5, 11, 18, 4]
def post_order_traversal(input_node, values=[]):
    if not input_node:
        return
    post_order_traversal(input_node.left, values)
    post_order_traversal(input_node.right, values)
    values.append(input_node.value)
    return values


# Level Order, or Breadth First, Traversal
# expected [4, 7, 18, 3, 1, 5, 11]
def level_order_traversal(input_tree):
    current, queue, visited = input_tree.root, Queue(), []
    queue.enqueue(input_tree.root)
    while not queue.is_empty():
        current = queue.dequeue()
        if not current:
            return visited
        visited.append(current.value)
        if current.left:
            queue.enqueue(current.left)
        if current.right:
            queue.enqueue(current.right)
    return visited

# ##################### NEW #####################################
# Write a test to cover this
# Binary Search Tree for contains
#                       7
#                     /   \
#                  -3      13
#                 /   \   /   \
#               -21     5 9    17
#
# Given a bst, return value the furthest removed from zero
def bst_furthest_from_zero(input_tree): 
    values = in_order_traversal(input_tree.root,[])
    left, right = values[0], values[-1]
    return left if abs(right) > left else right


# Binary Search Tree for contains
#                       7
#                     /   \
#                   3      13
#                 /   \   /   \
#                1     5 9     17
#
# Given a value return true or false if it's contained within the binary search tree
def bst_contains(input_tree, value):
    def traverse(node, value):
        if not node:
            return False
        if node.value == value:
            return True
        if value > node.value:
            return traverse(node.right, value)
        if value < node.value:
            return traverse(node.right, value)
    return traverse(input_tree.root, value)



# -----------------------------------------------------
# -----------------------------------------------------
# ----------------- TEST RUNNER STUFF -----------------
# -----------------------------------------------------
# -----------------------------------------------------


def run_tests():
    # Linked List Tests
    input_linked_list = make_linked_list()
    input_linked_list_2 = make_linked_list_2()
    input_linked_list_3 = make_linked_list_3()
    print("LinkedList Largest Value: {}".format(iterate_linkedlist_iteratively(input_linked_list)))
    print("LinkedList Smallest Value: {}".format(iterate_linkedlist_iteratively_small(input_linked_list)))
    print("LinkedList Remove Duplicate Value: {}".format(iterate_linkedlist_iteratively_duplicates(input_linked_list_2)))
    print("Furthest from zero: {}".format(iterate_linkedlist_furthest_from_zero(input_linked_list_3)))
    print("LinkedList Recursively Largest: {}".format(iterate_linkedlist_recursively(input_linked_list.head)))
    print("LinkedList Recursively Smallest: {}".format(iterate_linkedlist_recursively_smallest(input_linked_list_3.head)))
    # Stack Tests
    input_stack = make_stack()
    print("Stack Iteratively: {}".format(iterate_stack_iteratively(input_stack)))
    input_stack_2 = make_stack_2()
    print("Stack Recursively: {}".format(iterate_stack_recursively(input_stack_2)))
    # Queue Tests
    input_queue = make_queue()
    print("Queue Iteratively: {}".format(iterate_queue_iteratively(input_queue)))
    input_queue = make_queue2()
    print("Queue Recursively: {}".format(iterate_queue_recursively(input_queue)))

    # BinaryTree Order Traversal Tests
    input_binary_tree = make_binary_tree()
    print("Pre-Order Traversal: \n{}".format(pre_order_traversal(input_binary_tree.root)))
    print("In-Order Traversal: \n{}".format(in_order_traversal(input_binary_tree.root)))
    print("Post-Order Traversal: \n{}".format(post_order_traversal(input_binary_tree.root)))
    print("Level-Order Traversal: \n{}".format(level_order_traversal(input_binary_tree)))


    # Binary Search Tree Contains and Depth Search Tests
    input_binary_search_tree = make_binary_search_tree()
    input_binary_search_tree2 = make_binary_search_tree_2()
    print("Binary Search Tree furthest from zero: {}".format(bst_furthest_from_zero(input_binary_search_tree2)))
    print("Binary Search Tree Contains 13: {}".format(bst_contains(input_binary_search_tree, 13)))
    print("Binary Search Tree Contains 11: {}".format(bst_contains(input_binary_search_tree, 11)))


# helper methods to instatiate the datastructures
def make_linked_list():
    input_linked_list = LinkedList()
    input_linked_list.add(7)
    input_linked_list.add(2)
    input_linked_list.add(13)
    input_linked_list.add(9)
    input_linked_list.add(3)
    return input_linked_list

def make_linked_list_2():
    input_linked_list1 = LinkedList()
    input_linked_list1.add(7)
    input_linked_list1.add(2)
    input_linked_list1.add(7)
    input_linked_list1.add(2)
    input_linked_list1.add(13)
    input_linked_list1.add(9)
    input_linked_list1.add(3)
    input_linked_list1.add(13)
    input_linked_list1.add(9)
    input_linked_list1.add(3)
    return input_linked_list1

def make_linked_list_3():
    input_linked_list1 = LinkedList()
    input_linked_list1.add(-7)
    input_linked_list1.add(2)
    input_linked_list1.add(7)
    input_linked_list1.add(2)
    input_linked_list1.add(-14)
    input_linked_list1.add(9)
    input_linked_list1.add(3)
    input_linked_list1.add(13)
    input_linked_list1.add(9)
    input_linked_list1.add(3)
    return input_linked_list1


def make_stack():
    input_stack = Stack()
    input_stack.push(7)
    input_stack.push(2)
    input_stack.push(13)
    input_stack.push(9)
    input_stack.push(3)
    return input_stack

def make_stack_2():
    input_stack = Stack()
    input_stack.push(7)
    input_stack.push(2)
    input_stack.push(14)
    input_stack.push(9)
    input_stack.push(3)
    return input_stack


def make_queue():
    input_queue = Queue()
    input_queue.enqueue(7)
    input_queue.enqueue(2)
    input_queue.enqueue(13)
    input_queue.enqueue(9)
    input_queue.enqueue(3)
    return input_queue

def make_queue2():
    input_queue = Queue()
    input_queue.enqueue(7)
    input_queue.enqueue(2)
    input_queue.enqueue(14)
    input_queue.enqueue(9)
    input_queue.enqueue(3)
    return input_queue


def make_binary_tree():
    input_binary_tree = BinaryTree()
    node_a = Node(4)
    node_b = Node(7)
    node_c = Node(18)
    node_d = Node(3)
    node_e = Node(1)
    node_f = Node(5)
    node_g = Node(11)
    node_a.left = node_b
    node_a.right = node_c
    node_b.left = node_d
    node_b.right = node_e
    node_c.left = node_f
    node_c.right = node_g
    input_binary_tree.root = node_a
    return input_binary_tree


def make_binary_search_tree():
    input_binary_search_tree = BinarySearchTree()
    input_binary_search_tree.add(7, None)
    root = input_binary_search_tree.root
    input_binary_search_tree.add(3, root)
    input_binary_search_tree.add(1, root)
    input_binary_search_tree.add(5, root)
    input_binary_search_tree.add(13, root)
    input_binary_search_tree.add(9, root)
    input_binary_search_tree.add(17, root)
    return input_binary_search_tree

def make_binary_search_tree_2():
    input_binary_search_tree = BinarySearchTree()
    input_binary_search_tree.add(7, None)
    root = input_binary_search_tree.root
    input_binary_search_tree.add(-3, root)
    input_binary_search_tree.add(13, root)
    input_binary_search_tree.add(-21, root)
    input_binary_search_tree.add(5, root)
    input_binary_search_tree.add(9, root)
    input_binary_search_tree.add(17, root)
    return input_binary_search_tree


run_tests()
