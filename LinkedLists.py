class _Node:
    __slots__ = '_element','_nexts'
    
    def __init__(self,element,nexts):
        self._element = element
        self._nexts = nexts
        
class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None 
        self._size = 0
    
    def __len__(self):
        return self._size
        
    def isempty(self):
        return self._size == 0
        
    def addlast(self,e):
        newest = _Node(e,None)
        
        if self.isempty():
            self._head = newest
        else:
            self._tail._nexts = newest
          
        self._tail = newest
        self._size += 1
        
        
    def search(self,key):
        p = self._head
        index = 0
        while p:
            if p._element == key:
                return index
            else:
                p = p._nexts
                index +=1
                
        return -1
        
    def addfirst(self,e):
        newest = _Node(e,None)
        if self.isempty():
            self._head = newest
            self._tail = newest
            
        else:
            newest._nexts = self._head
            self._head = newest
        self._size +=1
        
    def addany(self,e,position):
        newest = _Node(e,None)
        p = self._head
        i = 1
        while i < position - 1:
            p = p._nexts
            i = i + 1 
            
        newest._nexts = p._nexts
        p._nexts = newest
        self._size +=1 
        
    def removefirst(self):
        if self.isempty():
            print("Empty List")
            return
        e = self._head._element
        self._head = self._head._nexts
        self._size -=1 
        if self.isempty():
            self._tail = None
        return e 
        
    def removelast(self):
        if self.isempty():
            print("Empty List")
            return
        p = self._head
        i = 1 
        while i < len(self) - 1:
            p = p._nexts
            i = i + 1 
        self._tail._nexts = None
        self._size -=1
        
    def removeany(self,position):
        p = self._head
        i = 1 
        while i < position-1:
            p = p._nexts
            i = i+1 
            
        e = p._nexts._element
        p._nexts = p._nexts._nexts
        self._size -= 1
        
        return e
        
    def display(self):
        p = self._head
        while p:
            print(p._element,end="-->")
            p = p._nexts
        print()
            
L = LinkedList()
L.addlast(7)
L.addlast(4)
L.addlast(12)
L.addlast(8)
L.addlast(3)
L.display()
print("-------------------------------------")
print("Size of the list is : ",len(L))
print("-------------------------------------")
i = L.search(3)
print("Searched Element index is : ",i)
print("-------------------------------------")
L.addfirst(20)
L.display()
print("-------------------------------------")
L.addany(40,7)
L.display()
print("-------------------------------------")
L.removefirst()
L.display()
print("-------------------------------------")
L.removelast()
L.display()
print("-------------------------------------")
L.removeany(3)
L.display()

            
        
        