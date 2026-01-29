

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
