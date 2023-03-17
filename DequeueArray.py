class Dequeue:
    def __init__(self):
        self._data = []
        
    def __len__(self):
        return len(self._data)
        
    def isempty(self):
        return len(self._data) == 0
        
    def addfirst(self,e):
        self._data.insert(0,e)
        
    def addlast(self,e):
        self._data.append(e)
        
    def removefirst(self):
        if self.isempty():
            print("empty")
            return
        return self._data.pop(0)
        
    def removelast(self):
        if self.isempty():
            print("empty")
            return
        return self._data.pop()
        
    def first(self):
        if self.isempty():
            print("empty")
            return
        return self._data[0]
        
    def last(self):
        if self.isempty():
            print("empty")
            return
        return self._data[-1]
        
D = Dequeue()
D.addfirst(5)
D.addfirst(3)
D.addlast(7)
D.addlast(12)
print(D._data)

D.removefirst()
print(D._data)

D.removelast()
print(D._data)
        