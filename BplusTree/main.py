from bPlusTree import *

tree = bPlusTree(128)
while True:
    tree.insert(int(input("Digite um inteiro: ")))
    tree.print()
