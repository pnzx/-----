class TreeNode:
    def __init__(self, newItem, left, right):
        self.item = newItem
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self) -> None:
        self.__root = None
    
    def search(self, x) -> TreeNode:
        return self.__searchItem(self.__root, x)
    
    def __searchItem(self, tNode:TreeNode, x) -> TreeNode:
        if (tNode == None):
            return None
        elif (x == tNode.item):
            return tNode
        elif (x < tNode.item):
            return self.__searchItem(tNode.left, x)
        else:
            return self.__searchItem(tNode.right, x)
    
    def insert(self, newItem):
        self.__root = self.__insertItem(self.__root, newItem)
    
    def __insertItem(self, tNode:TreeNode, newItem) -> TreeNode:
        if (tNode == None):
            tNode = TreeNode(newItem, None, None)
        elif (newItem == tNode.item):
            return None
        elif (newItem < tNode.item):
            tNode.left = self.__insertItem(tNode.left, newItem)
        else:
            tNode.right = self.__insertItem(tNode.right, newItem)
        return tNode
    
    def delete(self, x):
        self.__root = self.__deleteItem(self.__root, x)
    
    def __deleteItem(self, tNode:TreeNode, x) -> TreeNode:
        if (tNode == None):
            return None
        elif (x == tNode.item):
            tNode = self.__deleteNode(tNode)
        elif (x < tNode.item):
            tNode.left = self.__deleteItem(tNode.left, x)
        else:
            tNode.right = self.__deleteItem(tNode.right, x)
        return tNode
    
    def __deleteNode(self, tNode:TreeNode) -> TreeNode:
        # 3가지 case
        #   1. tNode가 리프노드
        #   2. tNode가 자식이 하나만 있음
        #   3. tNode가 자식이 둘 있음
        if tNode.left == None and tNode.right == None:
            return None
        elif tNode.left == None:
            return tNode.right
        elif tNode.right == None:
            return tNode.left
        else:
            (rtnItem, rtnNode) = self.__deleteMinItem(tNode.right)
            tNode.item = rtnItem
            tNode.right = rtnNode
            return tNode
        
    # Case 3에서 삭제할 노드를 직후원소 값들로 변경하고 서브트리를 수선
    def __deleteMinItem(self, tNode:TreeNode) -> tuple:
        if tNode.left == None:
            return (tNode.item, tNode.right)
        else:
            (rtnItem, rtnNode) = self.__deleteMinItem(tNode.left)
            tNode.left = rtnNode
            return (rtnItem, tNode)
        
    def isEmpty(self) -> bool:
        return self.__root == self.NIL
    
    def clear(self):
        self.__root = self.NIL
    
    #순회
    #전위 순회: Root -> 왼쪽 -> 오른쪽
    def pre_order_traverse(self):
        self.__pre_order_traverse(self.__root)
    
    def __pre_order_traverse(self, tNode:TreeNode):
        if (tNode != None):
            print(tNode.item, end='')
            self.__pre_order_traverse(tNode.left)
            self.__pre_order_traverse(tNode.right)

    # 중위순회: 왼쪽 -> Root -> 오른쪽
    def in_order_traverse(self):
        self.__in_order_traverse(self.__root)

    def __in_order_traverse(self, tNode:TreeNode):
        if (tNode != None):
            self.__in_order_traverse(tNode.left)
            print(tNode.item, end='')
            self.__in_order_traverse(tNode.right)
    
    # 후위순회: 왼쪽 -> 오른쪽 -> Root
    def post_order_traverse(self):
        self.__post_order_traverse(self.__root)
    
    def __post_order_traverse(self, tNode:TreeNode):
        if(tNode != None):
            self.__post_order_traverse(tNode.left)
            self.__post_order_traverse(tNode.right)
            print(tNode.item, end='')