

class queue():
    #FIFO structure
    def __init__(self):
        self.queue = []
        self.length = 0

    def get_length(self):
        return self.length
    
    def is_empty(self):
        return self.get_length() == 0
    
    def push(self,value):
        self.queue.append(value)
        self.length += 1

    def pop(self):
        if self.get_length() == 0:
            return None
        temp = self.queue.pop(0)# ensuring first element is removed 
        self.length -= 1
        return temp
    
    def peak(self):
        if self.get_length() == 0:
            return None
        return self.queue[0]
