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
if fruta == 1:
    print(tree.root)
print(tree.root.left)
print(tree.root.right.left)
