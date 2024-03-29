class node:
    def __init__(self,size,leaf,pointerLeft=0,pointerRight=0):
        self.leaf = leaf
        self.size = size
        self.values = []
        self.keys = []
        self.pointerLeft = pointerLeft
        self.pointerRight = pointerRight
    
    def getValues(self):
        return self.values.copy()
    
    def getKeys(self):
        return self.keys.copy()
    
    def delKeys(self):
        #Deleta todas as chaves
        del self.keys[:]

    def insert(self,value):
            self.values.append(value)
            self.values.sort()
    
    def removeValue(self,value):
            self.values.remove(value)
            self.values.sort()
    
    def removeKey(self,key):
            self.keys.remove(key)
            self.keys.sort()
    
    
    def isFull(self):
        if len(self.values) >= self.size:
            return True
        else:
            return False
    
    def isEmpty(self):
        if len(self.values) <= self.size/2:
            return True
        else:
            return False
    
    def isLeaf(self):
        return self.leaf
    
    def appendChild(self,child):
        self.keys.append(child)
    
    def getKeys(self):
        return self.keys.copy()

    def __eq__(self, other):
        if self.values[0] == other.values[0]:
            return True
        else:
            return False
    
    def __lt__(self,other):
        if self.values[0] < other.values[0]:
            return True
        else:
            return False