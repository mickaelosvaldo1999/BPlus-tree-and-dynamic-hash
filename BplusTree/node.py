class node:
    def __init__(self,size,leaf,pointerLeft=0,PointerRight=0):
        self.leaf = leaf
        self.size = size
        self.values = []
        self.keys = []
    
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
    
    def isFull(self):
        if len(self.values) >= self.size:
            return True
        else:
            return False
    
    def isLeaf(self):
        return self.leaf
    
    def appendChild(self,child):
        self.keys.append(child)
    
    def verify(self):
        if self.isLeaf():
            if len(self.values) < self.size/2:
                return False
            else:
                return True
        elif self.root:
            True
        else:
            if len(self.keys) == len(self.values) + 1:
                return True
            else:
                return False
    
    def getKeys(self):
        return self.keys.copy()