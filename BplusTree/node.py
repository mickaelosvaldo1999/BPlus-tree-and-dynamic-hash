class node:
    def __init__(self,size,leaf,pointerLeft=0,pointerRight=0):
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
    
    def getKeys(self):
        return self.keys.copy()