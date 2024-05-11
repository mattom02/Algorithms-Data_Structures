from typing import Union

class Node:
    def __init__(self, key: int, value: str) -> None:
        self._key = key
        self._value = value
        self._left = None
        self._right = None

class BinaryTree:
    def __init__(self) -> None:
        self.__root = None

    def search(self, key: int) -> Union[str, None]:
        if self.__root is None:
            return None
        else:
            return self.__search(key, self.__root)
        
    def __search(self, key: int, node: Node) -> Union[str, None]:
        if key == node._key:
            return node._value
        elif key < node._key:
            return self.__search(key, node._left)
        elif key > node._key:
            return self.__search(key, node._right)
        return None

    def insert(self, key: int, value: str) -> None:
        self.__root = self.__insert(key, value, self.__root)
        
    def __insert(self, key: int, value: str, node: Node) -> Union[str, None, Node]:
        if node is None:
            return Node(key, value)
        elif node._key is key:
            node._value = value
            return node
        elif key < node._key:
            node._left = self.__insert(key, value, node._left)
            return node
        elif key > node._key:
            node._right = self.__insert(key, value, node._right)
            return node

    def delete(self, key: int) -> None:
        self.__root = self.__delete(key, self.__root)
        
    def __delete(self, key: int, node: Node) -> Union[Node, None]:
        if key < node._key:
            node._left = self.__delete(key, node._left)
            return node
        elif key > node._key:
            node._right = self.__delete(key, node._right)
            return node
        elif key == node._key:
            if node._right is None and node._left is None:
                return None
            elif node._right is None:
                return node._left
            elif node._left is None:
                return node._right
            else:
                current = node._right
                while current._left is not None:
                    current = current._left
                temp = Node(current._key, current._value)
                temp._left = node._left
                temp._right = self.__delete(current._key, node._right)
                return temp
        
    def print(self) -> None:
        if self.__root is None:
            return None
        else:
            self.__print(self.__root)

    def __print(self, node: Node) -> None:
        if node._left is not None:
            self.__print(node._left)
        print(f"{node._key} {node._value}", end = ",")
        if node._right is not None:
            self.__print(node._right)

    def height(self) -> int:
        return self.__height(self.__root)

    def __height(self, node: Node) -> int:
        if node is None:
            return 0
        else:
            leftHeight = self.__height(node._left)
            rightHeight = self.__height(node._right)

            if rightHeight > leftHeight:
                return rightHeight + 1
            else:
                return leftHeight + 1

    def print_tree(self) -> None:
        print("==============")
        self.__print_tree(self.__root, 0)
        print("==============")

    def __print_tree(self, node: Node, lvl: int) -> None:
        if node != None:
            self.__print_tree(node._right, lvl + 5)
            print()
            print(lvl * " ", node._key, node._value)
            self.__print_tree(node._left, lvl + 5)
