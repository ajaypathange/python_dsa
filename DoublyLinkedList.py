class _Node:
    __slots__ = '_element','_next','_prev'
    
    def __init__(self,element, next, prev):
        self._element = element
        self._next = next
        self._prev = prev 
        
class DoublyLL:
    def __init__(self):
        self._head = None 
        self._tail = None 
        self._size = 0
        
    def __len__(self):
        return self._size
        
    def isempty(self):
        return self._size == 0
        
    def addlast(self,e):
        newest = _Node(e,None,None)
        if self.isempty():
            self._head = newest
            self._tail = newest
        else:
            self._tail._next = newest
            newest._prev = self._tail
        self._tail = newest
        self._size += 1
        
    def addany(self,e,position):
        newest = _Node(e,None,None)
        p = self._head
        i = 1
        while i < position - 1:
            p = p._next
            i = i+1 
        newest._next = p._next
        p._next = newest
        newest._prev = p 
        self._size += 1
        
        
    def addfirst(self,e):
        newest = _Node(e,None,None)
        if self.isempty():
            self._head = newest
            self._tail = newest
            
        else:
            newest._next = self._head
            self._head._prev = newest
            self._head = newest
            
        self._size += 1
        
    def removefirst(self):
        if self.isempty():
            print("Empty")
            return
        e = self._head._element
        self._head = self._head._next
        self._prev = None
        self._size -=1 
        return e 
        
    def removelast(self):
        if self.isempty():
            print("Empty")
            return
        e = self._tail._element
        self._tail = self._tail._prev
        self._tail._next = None
        self._size -= 1 
        return e 
            
            
    def removeany(self, position):
        p = self._head
        i = 1  
        while i < position:
            p = p._next
            i = i+1 
        
        e = p._next._element
        p._next = p._next._next
        p._next._prev = p 
        self._size -= 1 
        return e 
        
    def display(self):
        p = self._head
        while p :
            print(p._element, end = '-->')
            p = p._next
            
D = DoublyLL()
D.addlast(7)
D.addlast(4)
D.addlast(15)
D.addlast(20)
D.addlast(4)
D.display()
print()
print("Size : ", len(D))


D.addfirst(34)
D.display()
print()
print("Size : ", len(D))

D.addany(95,3)
D.display()
print()
print("Size : ", len(D))

D.removefirst()
D.display()
print()
print("Size : ", len(D))

D.removelast()
D.display()
print()
print("Size : ", len(D))

D.removeany(3)
D.display()
print()
print("Size : ", len(D))

        
        
