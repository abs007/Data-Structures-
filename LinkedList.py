class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
class List:
    def __init__(self,data=None):
        self.head= node(data)
        
    def display(self):
        lst=[]
        cr_node=self.head
        while cr_node!=None:
            lst.append(cr_node.data)
            cr_node=cr_node.next           
        return lst
    
    def append(self,data):
        new_node= node(data)
        self.tail.next=new_node
        self.tail=new_node
        new_node.next=None
    
    def appbeg(self,data):
        new_node= node(data)
        new_node.next= self.head
        self.head=new_node
    
    def add(self,node_data,new_data):
        new_node=node(new_data)
        curr_node=self.head
        while True:
            if curr_node==None:
                return 'Invalid choice'
            if curr_node.data==node_data:
                n=curr_node.next
                curr_node.next=new_node
                new_node.next=n
                return self.display()
            else:
                curr_node=curr_node.next
        
        
        
       ### Example test cases ###
        
    l1=List()
    l1.head=node('1')
    l1.tail=node('2')
    l1.head.next=l1.tail
    l1.display()
 >>>['1', '2']
 
    l1.append('3')
    l1.append('4')
    l1.display()
 >>>['1', '2', '3', '4']
 
    l1.appbeg('0')
    l1.display()
 >>>['0', '1', '2', '3', '4']

    l1.add('4','5')             ##This func doesn't need display() because 'return self.display() is already present in the while loop
 >>>['0', '1', '2', '3', '4', '5']
