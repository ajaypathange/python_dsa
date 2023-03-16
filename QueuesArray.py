class QueuesArray:
    
    def __init__(self):
        self._data = []
    
    def __len__(self):
        return len(self._data)
        
    def isempty(self):
        return len(self._data) == 0
        
    def enqueue(self,e):
        self._data.append(e)
        
    def dequeue(self):
        if self.isempty():
            print("Empty")
            return
        else:
            return self._data.pop(0)
            
    def first(self):
        if self.isempty():
            print("Empty")
            return
        return self._data[0]
        
Q = QueuesArray()
Q.enqueue(5)
Q.enqueue(3)
Q.enqueue(6)
print(Q._data)
print("Size : ",len(Q))
Q.dequeue()
print(Q._data)
print("Size : ",len(Q))
Q.first()
print(Q.first())
print(Q._data)
print("Size : ",len(Q))
        