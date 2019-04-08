# dictionary.py

import sys

'''
Implementation of a Dictionary as a Red/Black BST in python

--- NODE COLORING KEY ---
RED   -> FALSE
BLACK -> TRUE

--- RULES ---
I   - Every Node has a color, red or black
II  - Root of tree is always black
III - A red node cannot have a red parent or child
IV  - Every path from node to any child has the same
      number of black nodes
'''


class Node(object):

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.parent = self.left = self.right = None
        self.color = False

    def delete(self):
        if self.left:
            self.delete(self.left)
        if self.right:
            self.delete(self.right)
        del self

    def insert(self, node):
        '''
        inserts a node object
        into the dictionary by
        traversing through nodes
        till it finds an empty child
        '''
        if self.key < node.key:
            if node.left:
                return self.insert(node.left)
            else:
                node.left = self
                self.parent = node
        else:
            if node.right:
                return self.insert(node.right)
            else:
                node.right = self
                self.parent = node

    def search(self):
        pass

    def rotate(self):
        pass

    def left_left(self):
        pass

    def left_right(self):
        pass

    def right_right(self):
        pass

    def right_left(self):
        pass

    def show(self):
        '''
        recurses over nodes
        and prints all children
        until nodes are displayed
        '''
        if self.left:
            self.left.show()
        if self.right:
            self.right.show()
        sys.stdout.write(f'{self}, ')

    def __repr__(self):
        return '\'%s\': %s' % (self.key, self.value)


class Dictionary(object):

    def __init__(self):
        '''
        sets _root to None
        and size to 0
        -  -
        insert will set
        root for empty dictionary
        '''
        self._root = None
        self.size = 0

    def __len__(self):
        return self.size

    # TODO: __repr__

    def show(self):
        sys.stdout.write('{ ')
        self._root.show()
        sys.stdout.write(' }\n')

    def balance(self, node):
        if not node.parent:
            # node has no parent, its the root
            node.color = True
        elif not node.parent.parent:
            # parent is the root
            node.color = False

    def root(self, node):
        '''
        Finds the new root for the
        dictionary after rotations
        '''
        if node.parent is not None:
            return self.root(node.parent)

    def search(self):
        pass

    def insert(self, key, value):
        '''
        inserts a key value pair
        into the dictionary
        calls
         - Dictionary.balance()
           to balance tree
         - Dictionary..root()
           to find new root node
        '''
        node = Node(key, value)
        if not self._root:
            self._root = node
        else:
            node.insert(self._root)

        # self.balance(self._root)
        # self._root = self.root(self._root)
        self.size += 1

    def delete(self):
        pass


if __name__ == '__main__':
    from random import randint
    d = Dictionary()
    for i in range(10):
        d.insert(i, randint(0, 10))
        d.show()
