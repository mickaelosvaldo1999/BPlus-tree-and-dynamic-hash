from bPlusTree import *

tree = bPlusTree(128)

for i in range(1,100,2):
    tree.insert(i)
    tree.print()

while True:
    tree.insert(int(input("Digite um inteiro: ")))
    tree.print()
