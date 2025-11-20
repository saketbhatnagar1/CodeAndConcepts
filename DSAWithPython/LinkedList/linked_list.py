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
        return True   
    def insert(self,index): #create a new node and add to new 
        pass
    def pop_first(self):
        if self.length ==0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp        
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value,"->")
            temp = temp.next
    def get(self,index):
        temp = self.head
        if index<0 or index>= self.length:
            return None
        for _ in range(index):
            temp = temp.next
        return temp
    def set_value(self,index,value):
        if self.length == 0:
            return None
        temp = self.get(index)
        if temp:
            temp.value = value 
            return True
        return False
    def insert(self,index,value):
        if index<0 or index>self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value=value)
        temp = self.get(index=index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length+=1
        return True
    def remove(self,index):
        if index == 0:
            return self.pop_first()
        if index == self.length:
            return self.pop()
        previous = self.get(index-1)
        temp = previous.next
        previous.next = temp.next
        temp.next = None
        self.length -=1
        return temp
    def reverse(self):
        if self.length <= 1:
            return
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None 
        for _ in range(self.length): #a->b->c->d to reverse after = b 
            after = temp.next       #a->b->c->d->None after = b,temp = a, before = None (new variable with none value)
            temp.next = before  # None(before)<-a b->c->d
            before = temp   # a<-b before = a 
            temp = after #temp = c
            
    def doubly():
        pass
    
