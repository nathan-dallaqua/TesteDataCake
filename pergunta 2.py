
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.roght = None

    def __str__(self):
        return str(self.data)


class BinaryTree:
    def __init__(self, data):
        node = Node(data)
        self.root = node


if __name__ == '__main__':
    tree = BinaryTree('Maçã')
    tree.root.left = Node('Morango')
    tree.root.left.left = Node('Goiaba')
    tree.root.left.right = Node('Limão')
    tree.root.right = Node('Pera')
    tree.root.right.left = Node('Abacaxi')
    tree.root.right.left.left = Node('Laranja')
    tree.root.right.left.left.left = Node('Banana')
    tree.root.right.left.left.right = Node('Cebola')
  
fruta=int(input('''Temos uma árvore binária onde possui as frutas:
1 - Maçã
2 - Morango
3 - Goiaba
4 - Limão
5 - Pera
6 - Abacaxi
7 - Laranja
8 - Banana
9 - Cebola
Informe o número da fruta que deseja e elá será buscada nesta árvore:
'''))


if fruta == 2:
  print(tree.root, '=>', tree.root.left)
  
elif fruta == 3:
  print(tree.root,'=>', tree.root.left, '=>', tree.root.left.left)

elif fruta == 4:
  print(tree.root,'=>', tree.root.left, '=>', tree.root.left.right)

elif fruta == 5:
  print(tree.root,'=>', tree.root.right)

elif fruta == 6:
  print(tree.root,'=>', tree.root.right,'=>', tree.root.right.left)

elif fruta == 7:
  print (tree.root,'=>', tree.root.right,'=>', tree.root.right.left, '=>', tree.root.right.left.left)

elif fruta == 8:
  print (tree.root,'=>', tree.root.right,'=>', tree.root.right.left, '=>', tree.root.right.left.left,'=>',tree.root.right.left.left.left )

elif fruta == 9:
  print (tree.root,'=>', tree.root.right,'=>', tree.root.right.left, '=>', tree.root.right.left.left,'=>',tree.root.right.left.left.right)
