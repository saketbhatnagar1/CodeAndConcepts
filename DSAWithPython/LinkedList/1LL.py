class Node: #create a new node
    def __init__(self,value):
        self.value = value
        self.next = None




class LinkedList: #Class for linke dlist 
    def __init__(self,value): # Create a Linked List
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    def append(self,value): #create a new node and add to tyhe end
        #Check if Node exists
        temp = self.head
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length+=1

    def pop(self): #next of next is None, next of next is to be removed, so we set the tail pointer to next
        #if non node:
        if self.length == 0:
            return None
        temp = self.head
        previous = self.head
        #if one node:

        while temp.next is not None:
            previous = temp
            temp = temp.next
        self.tail = previous
        self.tail.next = None
        self.length -=1 
        if self.length ==0:
            self.head = None
            self.tail = None
            return temp
    def prepend(self,value): #create a new node and add to the end
        new_node = Node(value)
        if self.length ==0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node 
        self.length+=1   
    def insert(): #create a new node and add to new 
        pass
    def print_list(self):
        temp = self.head
        while temp is not None:
