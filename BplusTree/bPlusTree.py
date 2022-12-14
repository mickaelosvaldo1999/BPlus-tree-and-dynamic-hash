from node import *
# O python geralmente armazena inteiros acima de 256 com 28 Bytes. Por isso vou considerar essa a medida padrão
class bPlusTree:
    def __init__(self,blockSize,default=28):
        self.blockSize = blockSize
        self.default = blockSize//default
        #Por motivos de implementação só podemos aceitar números pares de tamnho de árvore
        if self.default % 2 != 0:
            print("!!blockSize reduced by 1!!")
            self.default - 1
        #Cria a raiz
        self.root = node(self.default,True)
        
    def insert(self,value):
        #Verifica se o valor é inteiro e se tem o tamanho adequado
        if type(value) is int and value.__sizeof__() <= 28:

            #Verifica se a árvore ainda está na raiz
            if self.root.isFull():
                #Dividindo Raiz cheia
                print("Cheio")
                temp = self.splitChild(self.root)
                if self.root.isLeaf():
                    temp[0].leaf = True
                    temp[1].leaf = True

                self.root.delKeys()
                self.root.appendChild(temp[0])
                
                self.root.appendChild(temp[1])
                self.root.values = [temp[2]]

                self.root.leaf = False
                self.insert(value)
                #Caso normal de inserção
            else:
                self.findNode(self.root,value).values.append(value)
        else:
            print("FATAL ERROR: VALUE MUST BE AN INTEGER WITH 28 BYTES")
    

    def findNode(self,key,value):
        aux = 0
        temp = key
        if temp.isLeaf():
            return temp
        else:
            #Descendo
            for i in temp.getKeys():
                for j in i.getValues():
                    if value == j:
                        if i.isLeaf():
                            return self.findNode(i,value)
                        else:
                            True
                            aux = temp.getkeys().find(i)
                            if aux < len(temp.getkeys() - 1):
                                return self.findNode(aux+1,value)
                            else:
                                 return self.findNode(temp.getkeys()[-1],value)       
                    elif value < j:
                        #Verificnado se a chave não está cheia
                        if i.isFull():
                            print("Algum nó abaixo ta cheio")
                            mika = self.splitChild(i)
                            if i.getKeys() == []:
                                mika[0].leaf = True
                                mika[1].leaf = True

                            temp.keys[temp.keys.index(i)] = mika[0]
                            temp.keys.append(mika[1])
                            temp.values.append(mika[2])
                        return self.findNode(i,value)
                        
                    elif i == temp.getKeys()[-1]:
                        #Verificnado se a chave não está cheia
                        if i.isFull():
                            print("Algum nó abaixo ta cheio")
                            mika = self.splitChild(i)
                            if i.getKeys() == []:
                                mika[0].leaf = True
                                mika[1].leaf = True

                            temp.keys[temp.keys.index(i)] = mika[0]
                            temp.keys.append(mika[1])
                            temp.values.append(mika[2])
                        return self.findNode(temp.keys[-1],value)

            print("Algo deu errado")
            print(temp.getValues())
            print(temp.getKeys())
            print("------------------")
    
    def splitChild(self,page):
        temp = page.getValues()
        aux1 = node(self.default,False)
        aux1.values = temp[:self.default//2]
        aux2 = node(self.default,False)
        aux2.values = temp[self.default//2:]
        #TODO os : estão invertidos, provavelmente é algum problema de append nas keys
        aux1.keys = page.getKeys()[:self.default//2]
        aux2.keys = page.getKeys()[self.default//2:]
        #TERMINAR A INSERÇÃO DOS FILHOS
        return aux1,aux2,temp[self.default//2]
            
    def print(self):
        if self.root.isLeaf():
            print(self.root.getValues())
        else:
            level = [[self.root]]
            temp = []
            while True:
                aux = ""
                temp = level.copy()
                level.clear()
                for i in temp:
                    for j in i:
                        aux += str(j.getValues())
                        level.append(j.getKeys())
                print(aux)

                if level[0][0].isLeaf():
                    aux = ""
                    for i in level:
                        for j in i:
                            aux += str(j.getValues())
                    print(aux)
                    print("")
                    break

