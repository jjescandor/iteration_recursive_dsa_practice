from data_structures.node import Node
from data_structures.linked_list import LinkedList
from data_structures.stack import Stack
from data_structures.queue import Queue
from data_structures.binary_tree import BinaryTree
from data_structures.binary_search_tree import BinarySearchTree


# Iterate a linked list iteratively and return the largest value
# input_linked_list (7)->(2)->(13)->(9)->(3)
def iterate_linkedlist_iteratively(input_linked_list):
    # code here, change return the largest value
    return 0


# ##################### NEW #####################################
# Write a test to cover this
# Iterate through a linked list iteratively and return the smallest value
# input_linked_list (7)->(2)->(13)->(9)->(3)
def iterate_linkedlist_iteratively_small(input_linked_list):
    # code here, change return the smallest value
    return 0


# ##################### NEW #####################################
# Write a test to cover this
# Iterate through a linked list iteratively and remove duplicate values
# input_linked_list (7)->(2)->(13)->(2)->(9)->(3)->(9)

def iterate_linkedlist_iteratively_duplicates(input_linked_list):
    # code here, remove duplicate values
    return 0


# ##################### NEW #####################################
# Write a test to cover this
# Iterate through a linked list, and return the value furthest removed from zero
# input_linked_list (7)->(2)->(13)->(-9)->(3)->(-21)

def iterate_linkedlist_furthest_from_zero(input_linked_list):
    # code here, remove duplicate values
    return 0


# Iterate a linked list recursively and return the largest value
# input_linked_list (7)->(2)->(13)->(9)->(3)
def iterate_linkedlist_recursively(input_node, largest=0):
    # code here, change return the largest value
    return 0


# ##################### NEW #####################################
# Write a test to cover this
# Iterate through a linked list recursively and return the largest value
# input_linked_list (7)->(2)->(13)->(9)->(3)
def iterate_linkedlist_recursively_smallest(input_node, largest=0):
    # code here, change return the largest value
    return 0


# Iterate a stack iteratively and return the largest value
# input_stack (7)->(2)->(13)->(9)->(3)
def iterate_stack_iteratively(input_stack):
    # code here, change return the largest number
    return 0


# Iterate a stack recursively and return the largest value
# input_stack (7)->(2)->(13)->(9)->(3)
def iterate_stack_recursively(input_stack, largest=0):
    # code here, change return the largest number
    return 0


# Iterate a queue iteratively and return the largest value
# input_queue (7)->(2)->(13)->(9)->(3)
def iterate_queue_iteratively(input_queue):
    # code here, change return the largest number
    return 0


# Iterate a queue recursively and return the largest value
# input_queue (7)->(2)->(13)->(9)->(3)
def iterate_queue_recursively(input_queue, largest=0):
    # code here, change return the largest number
    return 0


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
    # code here, return a list of pre-ordered values
    return values


# In-Order Traveral
# expected [3, 7, 1, 4, 5, 18, 11]
def in_order_traversal(input_node, values=[]):
    # code here, return a list of in-order values
    return values


# Post-Order Traveral
# expected [3, 1, 7, 5, 11, 18, 4]
def post_order_traversal(input_node, values=[]):
    # code here, return a list of post-ordered values
    return values


# Level Order, or Breadth First, Traversal
# expected [4, 7, 18, 3, 1, 5, 11]
def level_order_traversal(input_tree):
    # code here, return a list of values
    return []


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
def bst_contains(input_tree):
    # code here, return value the furthest remove from zero
    return None


# Binary Search Tree for contains
#                       7
#                     /   \
#                   3      13
#                 /   \   /   \
#                1     5 9     17
#
# Given a value return true or false if it's contained within the binary search tree
def bst_contains(input_tree, value):
    # code here, return true or false
    return None


# -----------------------------------------------------
# -----------------------------------------------------
# ----------------- TEST RUNNER STUFF -----------------
# -----------------------------------------------------
# -----------------------------------------------------


def run_tests():
    # Linked List Tests
    input_linked_list = make_linked_list()
    print("LinkedList Iteratively: {}".format(iterate_linkedlist_iteratively(input_linked_list)))
    print("LinkedList Recursively: {}".format(iterate_linkedlist_recursively(input_linked_list.head)))

    # Stack Tests
    input_stack = make_stack()
    print("Stack Iteratively: {}".format(iterate_stack_iteratively(input_stack)))
    input_stack = make_stack()
    print("Stack Recursively: {}".format(iterate_stack_recursively(input_stack)))

    # Queue Tests
    input_queue = make_queue()
    print("Queue Iteratively: {}".format(iterate_queue_iteratively(input_queue)))
    input_queue = make_queue()
    print("Queue Recursively: {}".format(iterate_queue_recursively(input_queue)))

    # BinaryTree Order Traversal Tests
    input_binary_tree = make_binary_tree()
    print("Pre-Order Traversal: \n{}".format(pre_order_traversal(input_binary_tree.root)))
    print("In-Order Traversal: \n{}".format(in_order_traversal(input_binary_tree.root)))
    print("Post-Order Traversal: \n{}".format(post_order_traversal(input_binary_tree.root)))
    print("Level-Order Traversal: \n{}".format(level_order_traversal(input_binary_tree)))

    # Binary Search Tree Contains and Depth Search Tests
    input_binary_search_tree = make_binary_search_tree()
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


def make_stack():
    input_stack = Stack()
    input_stack.push(7)
    input_stack.push(2)
    input_stack.push(13)
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


run_tests()
