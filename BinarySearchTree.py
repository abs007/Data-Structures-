class node:
    def __init__(self,data=None):
        self.data=data
        self.left=None
        self.right=None
        
class bst:
    def __init__(self,data=None):
        self.root=node(data)
        
    def insert(self,data):
        if self.root:
            self._insert(data,self.root)
        else:
            self.root=node(data)
    
    def _insert(self,data,curr_node):
        if curr_node is None:
            curr_node=node(data)
            return curr_node
        
        if data<curr_node.data:
            curr_node.left=self._insert(data,curr_node.left)
        elif data>curr_node.data:
            curr_node.right=self._insert(data,curr_node.right)
        else:
            print( 'Value already exists')
            return None
        
        return curr_node 
            
    def print_tree(self):
        if self.root:
            self._print_tree(self.root)
        else:
            return 'Empty Tree'
    
    def _print_tree(self, curr_node):
        if curr_node:
            self._print_tree(curr_node.left)
            print (str(curr_node.data))
            self._print_tree(curr_node.right)
    
    def height(self):
        if self.root:
            return self._height(self.root,0)
        
        return 0
    
    def _height(self,curr_node,height):
        if curr_node==None:
            return height
        left_height= self._height(curr_node.left,height+1)
        right_height= self._height(curr_node.right,height+1)
        return max(left_height,right_height)
    
    def search(self,value):
        if self.root:
            return self._search(self.root,value)
        else:
            return False
    
    def _search(self,curr_node,value):
        if value==curr_node.data:
            return True
        elif value<curr_node.data and curr_node.left:
            return self._search(curr_node.left,value)
        elif value>curr_node.data and curr_ndoe.right:
            return self._search(curr_node.right,value)
        return False
    
    def levelOrder(self):
        if self.root:
            self._levelOrder()
        else:
            return []
    
    def _levelOrder(self):
        lst=[]
        from collections import deque
        q1 = deque()
        q1.append(self.root)
        
        while q1:
            
            for i in range(len(q1)):
                curr_node= q1.popleft()
                
                lst.append(curr_node.data)
                if curr_node.left: 
                    q1.append(curr_node.left)
                if curr_node.right:
                    q1.append(curr_node.right)
        print(lst)
        
        
        
        
        
        #
