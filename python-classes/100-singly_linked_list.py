#!/usr/bin/python3
"""Module that defines a node of a singly linked list"""

class Node:
    """class to define the node of a singly linked list"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """data getter"""
        return self.__data

    @data.setter
    def data(self, value):
        """data setter with validatiom"""
        if not isinstance(value, int):
            return TypeError("data must be an integer")
        self.__data = value
    
    @property
    def next_node(self):
        """Getter for next_node"""
        return self.__next_node

    @next_node.setter
    def def next_node(self, value):
        """Setter for next_node with validation"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """Class to define a singly linked list"""

    def __init__(self):
        """Initializes an empty linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new node in sorted (increasing) order"""
        new_node = Node(value)

        #If list is empty or new node should be at the beggining
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        #Find the appropriate position to insert
        current = self.__head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        #Insert the new node
        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """Print the entire list, one node per line"""
        result = []
        current = self.__head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)

        

