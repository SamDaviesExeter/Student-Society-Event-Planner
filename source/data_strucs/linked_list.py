

class linked_list():
    def __init__(self):
        #[[0,None]] #pos 0 = value # pos 1 = pointer 
        self.arr = []
        self.pointer = 0 


    def get_length(self):
        return len(self.arr)
    
    def insert(self,value,position):
        #transfverse array until you get to the position which [0][1] == copy the data update the pointer 
        ...
