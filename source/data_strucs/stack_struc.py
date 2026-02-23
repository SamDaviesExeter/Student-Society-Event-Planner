

class stack():
    #LIFO structure
    def __init__(self):
        self.stack = []
        self.length = 0

    def get_length(self):
        return self.length

    def is_empty(self):
        return self.get_length() == 0

    def push(self,value):
        self.stack.append(value)
        self.length += 1

    def pop(self):
        if self.get_length() == 0:
            return None
        temp = self.stack.pop(-1)# ensuring last element
        self.length -= 1
        return temp
    
    def peak(self):
        if self.get_length() == 0:
            return None
        return self.stack[-1]
    
    def insert_array(self,arr):
        for x in range(len(arr)):
            self.push(arr[x])

    def reverse_stack(self):
        if self.get_length() == 0:
            return None
        
        tmp = []
        for x in range(self.get_length()):
            tmp.append(self.pop()) #using stack methods to reverse 
        
        for x in range(len(tmp)-1, -1, -1): # someone wanted stack to return to original un reversed state
            self.push(tmp[x])
        return tmp
        
