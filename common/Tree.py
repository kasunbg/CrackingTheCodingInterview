class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
        self.parent = None

    # Walk the tree inOrder and append the elements into an array
    @staticmethod
    def InOrderArray(node, inArr):
        if not node:
            return
        if node.left:
            Node.InOrderArray(node.left, inArr)
        inArr.append(node.data)
        if node.right:
            Node.InOrderArray(node.right, inArr)

    @staticmethod
    def Depth(node):
        if not node:
            return 0
        return max(Node.Depth(node.left), Node.Depth(node.right)) + 1

    @staticmethod
    def _PreOrderArrayToTree(preArr, current, parent):
        if preArr[current] == None:
            return None, current + 1
        node = Node(preArr[current])
        node.parent = parent
        node.left, current = Node._PreOrderArrayToTree(preArr, current+1, node)
        node.right, current = Node._PreOrderArrayToTree(preArr, current, node)
        return node, current

    @staticmethod
    def PreOrderArrayToTree(preArr):
        root, _ = Node._PreOrderArrayToTree(preArr, 0, None)
        return root
