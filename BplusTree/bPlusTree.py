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
                self.insertNonFull(self.root,value).insert(value)
        else:
            print("FATAL ERROR: VALUE MUST BE AN INTEGER WITH 28 BYTES")
    
    def remove(self,value):
        self.__remove(self.root,value).removeValue(value)
    
    def __remove(self,key,value):
        temp = key
        #prevents empty root
        if self.root.getValues() == []:
            self.root = self.root.getKeys()[0]
            return self.__remove(self.root,value)

        #end of recursion
        if temp.isLeaf():
            return temp
        else:
            #Cheking leaf nodes to fix operations issues on structure
            if True:
                #Detalied analisis on leaf elements
                for i in temp.getValues():
                    #possible value found
                    if value < i or i == temp.getValues()[-1]:
                        #Picking key indexes
                        nextPage = temp.keys.index(temp.getKeys()[temp.getValues().index(i)])
                        #special case in last node
                        if i == temp.getValues()[-1] and value >= i:
                            nextPage += 1

                        if temp.getKeys()[nextPage].isEmpty():
                            #If this element is the first one
                            if i == temp.getValues()[0] and value < i:
                                #remover if
                                if i == temp.getValues()[0]:
                                    #Cheking if the right neightbor is empty
                                    if temp.getKeys()[1].isEmpty():
                                        #making forced merge
                                        temp.removeValue(i)
                                        self.print()
                                        temp.keys[nextPage] = self.mergeChild(temp.getKeys()[nextPage],temp.getKeys()[nextPage+1])
                                        temp.removeKey(temp.getKeys()[nextPage+1])

                                        return self.__remove(temp,value)
                                        
                                    #stealing the first key to miss the merge
                                    else:

                                        temp.keys[0].insert(temp.getKeys()[1].getValues()[0])
                                        temp.keys[1].removeValue(temp.getKeys()[1].getValues()[0])
                                        temp.insert(temp.getKeys()[1].getValues()[0])
                                        temp.removeValue(i)
                                        return self.__remove(temp,value)
                                    
                                
                            #if this element is the last one
                            elif i == temp.getValues()[-1] and value >= i:
                                if temp.getKeys()[-2].isEmpty():
                                    #making forced merge
                                    temp.removeValue(i)
                                    temp.keys[nextPage] = self.mergeChild(temp.getKeys()[nextPage],temp.getKeys()[nextPage-1])
                                    temp.removeKey(temp.getKeys()[nextPage-1])

                                    return self.__remove(temp,value)
                                        
                                #stealing the first key to miss the merge
                                else:
                                    temp.keys[-1].insert(temp.getKeys()[-2].getValues()[-1])
                                    temp.insert(temp.getKeys()[-2].getValues()[-1])
                                    temp.keys[-2].removeValue(temp.getKeys()[-2].getValues()[-1])
                                    temp.removeValue(i)
                                    return self.__remove(temp,value)

                            #removing elements in the middle of structure
                            else:
                                #testing if can miss the merge
                                if not temp.getKeys()[nextPage + 1].isEmpty():

                                    temp.keys[nextPage].insert(temp.getKeys()[nextPage + 1].getValues()[0])
                                    temp.keys[nextPage + 1].removeValue(temp.getKeys()[nextPage + 1].getValues()[0])
                                    temp.insert(temp.getKeys()[nextPage + 1].getValues()[0])
                                    temp.removeValue(i)
                                    return self.__remove(temp,value)

                                elif not temp.getKeys()[nextPage - 1].isEmpty():
                                    temp.keys[nextPage].insert(temp.getKeys()[nextPage - 1].getValues()[-1])
                                    temp.insert(temp.getKeys()[nextPage - 1].getValues()[-1])
                                    temp.keys[nextPage - 1].removeValue(temp.getKeys()[nextPage - 1].getValues()[-1])
                                    temp.removeValue(i)
                                    return self.__remove(temp,value)

                                
                                #Forced merge
                                else:
                                    #making forced merge
                                    temp.removeValue(i)
                                    temp.keys[nextPage] = self.mergeChild(temp.getKeys()[nextPage],temp.getKeys()[nextPage+1])
                                    temp.removeKey(temp.getKeys()[nextPage+1])

                                    return self.__remove(temp,value)
                        
                        else:
                            return self.__remove(temp.keys[nextPage],value)
                        

            #Log de erro
            print("Algo deu errado")
            print(temp.getValues())
            print(temp.getKeys())
            print("------------------")


    def mergeChild(self,keyA,keyB):
        if not keyA.isEmpty() or not keyB.isEmpty():
            print("ERROR ON MERGING TWO NODES")
            quit(513)
        #definindo a maior chave
        #KeyB é sempre a maior chave
        if keyB < keyA:
            aux = keyB
            keyB = keyA
            keyA = aux

        keyA.values += keyB.values
        keyA.keys += keyB.keys
        return keyA

    def search(self,value):
        return self.__search(self.root,value)
    
    def __search(self,key,value):
        temp = key
        if temp.isLeaf():
            if value in temp.getValues():
                print("Encontrou!!")
                return True
            else:
                print("Não encontrado")
                print(key.getValues())
                return False
        else:
            #verificando se o ní de baixo não é folha
            if temp.getKeys()[0].isLeaf():
                for i in temp.getValues():
                    if value < i or i == temp.getValues()[-1]:
                        
                        if value >= temp.getValues()[-1]:
                            #retornando a folha
                            nextPage = temp.keys.index(temp.getKeys()[-1])
                            
                        else:
                            #retornando a folha
                            nextPage = temp.keys.index(temp.getKeys()[temp.getValues().index(i)])
                            
                        return self.__search(temp.keys[nextPage],value)
            #Descendo
            else:
                for i in temp.getKeys():
                    for j in i.getValues():        
                        if value < j or i == temp.getKeys()[-1]:
                            #Capturando índice de árvore caso ocorra um split
                            nextPage = temp.keys.index(i)
                            return self.__search(temp.keys[nextPage],value)

            #Log de erro
            print("Algo deu errado")
            print(temp.getValues())
            print(temp.getKeys())
            print("------------------")


    def insertNonFull(self,key,value):
        temp = key
        if temp.isLeaf():
            return temp
        else:
            #verificando se o nó de baixo não é folha
            if temp.getKeys()[0].isLeaf():
                for i in temp.getValues():
                    if value < i or i == temp.getValues()[-1]:
                        if value >= temp.getValues()[-1]:
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
                                return self.insertNonFull(temp,value)
                            return self.insertNonFull(temp.keys[nextPage],value)
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
                                return self.insertNonFull(temp,value)
                            return self.insertNonFull(temp.keys[nextPage],value)

            #Descendo
            else:
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
                                return self.insertNonFull(temp,value)
                            return self.insertNonFull(temp.keys[nextPage],value)

            #Log de erro
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

