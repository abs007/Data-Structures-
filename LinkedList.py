class node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
               
class List:
    def __init__(self,data=None):
        self.head = node(data)
        
    def display(self):
        lst = []
        cr_node = self.head
        while cr_node != None:
            lst.append(cr_node.data)
            cr_node = cr_node.next           
        return lst
    
    def append(self,data):
        new_node = node(data)
        cr_node = self.head
        
        while cr_node.next:
            cr_node = cr_node.next
        
        cr_node.next = new_node
        new_node.next = None
    
    def appbeg(self,data):
        new_node = node(data)
        new_node.next = self.head
        self.head = new_node
    
    def addafter(self,node_data,new_data):
        new_node = node(new_data)
        curr_node = self.head
        while True:
            if curr_node == None:
                return 'Invalid choice'
            if curr_node.data == node_data:
                n = curr_node.next
                curr_node.next = new_node
                new_node.next = n
                return self.display()
            else:
                curr_node = curr_node.next
        
        
        
       ### Example test cases ###
        
    l1=List()
    l1.head = node(5)
    l1.addafter(5,6)        
 >>>[5, 6]                          ##This func doesn't need display() because 'return self.display() is already present in the while loop
 
    l1.append(7)
    l1.display()
 >>>[5, 6, 7]
 
    l1.appbeg(4)
    l1.display()
 >>>[4, 5, 6, 7]
