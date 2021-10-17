class Queue:
    
    def __init__(self,data=[]):
        self.items=data
    
    def isEmpty(self):
        return self.items==[]
    
    def add(self,data):
        self.items.append(data)
    
    def remove(self):
        if self.items:
            return self.items.pop(0)  
            
    def size(self):
        return len(self.items)

    def prQueue(self):
        return self.items
