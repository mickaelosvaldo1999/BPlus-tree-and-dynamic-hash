from node import *
# O python geralmente armazena inteiros acima de 256 com 28 Bytes. Por isso vou considerar essa a medida padrão
class bPlusTree:
    def __init__(self,blockSize,default=28):
        self.blockSize = blockSize
        self.default = blockSize//default
        #Por motivos de implementação só podemos aceitar números pares de tamnho de árvore
        if self.default % 2 != 0:
            print("!!blockSize reduced by 1!!")
            self.default =- 1
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
                self.findNode(self.root,value).insert(value)
        else:
            print("FATAL ERROR: VALUE MUST BE AN INTEGER WITH 28 BYTES")
    

    def findNode(self,key,value):

        temp = key
        if temp.isLeaf():
            return temp
        else:
            #verificando se o ní de baixo não é folha
            if temp.getKeys()[0].isLeaf():
                print("---------------- FOLHA ---------------------")
                for i in temp.getValues():
                    if value < i or i == temp.getValues()[-1]:
                        if value > temp.getValues()[-1]:
                            #Capturando índice de árvore caso ocorra um split
                            nextPage = temp.keys.index(temp.getKeys()[-1])
                            #Verificnado se a chave não está cheia
                            if temp.getKeys()[-1].isFull():
                                print("Algum nó abaixo ta cheio")
                                mika = self.splitChild(temp.getKeys()[-1])
                                if temp.getKeys()[-1].isLeaf():
                                    mika[0].leaf = True
                                    mika[1].leaf = True

                                temp.keys[nextPage] = mika[0]
                                temp.keys.append(mika[1])
                                temp.insert(mika[2])
                                return self.findNode(temp,value)
                            return self.findNode(temp.keys[nextPage],value)
                        else:
                            #Capturando índice de árvore caso ocorra um split
                            nextPage = temp.keys.index(temp.getKeys()[temp.getValues().index(i)])
                            aux = temp.getKeys()[temp.getValues().index(i)]
                            #Verificnado se a chave não está cheia
                            if aux.isFull():
                                print("Algum nó abaixo ta cheio")
                                mika = self.splitChild(aux)
                                if aux.isLeaf():
                                    mika[0].leaf = True
                                    mika[1].leaf = True

                                temp.keys[nextPage] = mika[0]
                                temp.keys.append(mika[1])
                                temp.insert(mika[2])
                                return self.findNode(temp,value)
                            return self.findNode(temp.keys[nextPage],value)

            #Descendo
            for i in temp.getKeys():
                for j in i.getValues():        
                    if value < j or i == temp.getKeys()[-1]:
                        #Capturando índice de árvore caso ocorra um split
                        nextPage = temp.keys.index(i)
                        #Verificnado se a chave não está cheia
                        if i.isFull():
                            print("Algum nó abaixo ta cheio")
                            mika = self.splitChild(i)
                            if i.isLeaf():
                                mika[0].leaf = True
                                mika[1].leaf = True

                            temp.keys[nextPage] = mika[0]
                            temp.keys.append(mika[1])
                            temp.insert(mika[2])
                            return self.findNode(temp,value)
                        return self.findNode(temp.keys[nextPage],value)


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

