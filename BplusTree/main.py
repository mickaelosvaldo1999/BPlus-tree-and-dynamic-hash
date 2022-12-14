from bPlusTree import *

tree = bPlusTree(128)
""""
while True:
    tree.insert(int(input("Digite um inteiro: ")))
    tree.print()
"""
for i in range(1,100):
    tree.insert(i)
    tree.print()
