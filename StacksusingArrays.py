class StackArray:
    
    def __init__(self):
        self._data = []
        
    def __len__(self):
        return len(self._data)
    
    def isempty(self):
        return len(self._data) == 0
        
    def push(self, e):
        self._data.append(e)
    
    def pop(self):
        if self.isempty():
            print("Empty")
            return
        else:
            return self._data.pop()
            
    def top(self):
        if self.isempty():
            print("Empty")
            return
        return self._data[-1]
        
S = StackArray()
S.push(3)
S.push(4)
S.push(7)
print(S._data)
print("Size ",len(S._data))
print(S.pop())
print(S._data)
print(S.top())
print(S._data)
