import matplotlib as plt
import networkx as nx
import sys


class Node:
    def __init(self, key):
        self.parent = None
        self.left = None
        self.right = None
        self.key = key
        self.color = True  # boolean (red or black), new node must be red


class NilNode:
    def __init__(self):
        self.color = False  # true for red false for black


class RedBlackTree:
    def __init__(self, root):
        self.root = root
        nil = NilNode()
        self.root.parent = nil
        self.nil = nil

    def tree_search(self, x, k):
        # initial call rbt.tree_seach(rbt.root, k)
        if x == self.nil or k == x.key:
            return x
        if k < x.key:
            return self.tree_search(x.left, k)
        else:
            return self.tree_search(x.right, k)

    def tree_min(self, x):
        while x.left != self.nil:
            x = x.left
        return x

    def tree_max(self, x):
        while x.right != self.nil:
            x = x.right
        return x

    def tree_successor(self, x):
        if x.right != self.nil:
            return self.tree_min(x.right)
        y = x.parent
        while y != self.nil and x == y.right:
            x = y
            y = y.parent
        return y

    def tree_predecessor(self, x):
        if x.left != self.nil:
            return self.tree_max(x.left)
        y = x.parent
        while y != self.nil and x == y.left:
            x = y
            y = y.parent
        return y

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
            y.left = x
            x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
            y.right = x
            x.parent = y

    def tree_insert(self, key):
        z = Node(key)
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == self.nil:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = self.nil
        z.right = self.nil
        z.color = True  # red
        self.insert_fixup(z)

    def insert_fixup(self, z):
        while z.parent.color == True:
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == True:
                    z.parent.color = False
                    y.color = False
                    z.parent.parent.color = True
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.color = False
                    z.parent.parent.color = True
                    self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == True:
                    z.parent.color = False
                    y.color = False
                    z.parent.parent.color = True
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)

                    z.parent.color = False
                    z.parent.parent.color = True
                    self.left_rotate(z.parent.parent)
        self.root.color = False

    def tree_delete(self, z):
        y = z
        y_original_color = y.color
        if z.left == self.nil:
            x = z.right
            self.tree_transplant(z, z.right)
        elif z.right == self.nil:
            x = z.left
            self.tree_transplant(z, z.left)
        else:
            y = self.tree_min(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.tree_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.tree_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == False:
            self.delete_fixup(x)

    def tree_transplant(self, u, v):
        if u.parent == self.nil:
            self.root = v
        elif u == u.parent:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def delete_fixup(self, x):
        while x != self.root and x.color == False:
            if x == x.parent.left:
                w = x.parent.right
                if w.color == True:
                    w.color = False
                    x.parent.color = True
                    self.left_rotate(x.parent)
                    w = x.parent.right

                if w.left.color == False and w.right.color == False:
                    w.color = True
                    x = x.parent
                else:
                    if w.right.color == False:
                        w.left.color = False
                        w.color = True
                        self.right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = False
                    w.right.color = False
                    self.left_rotate(x.parent)
                    x = self.root

            else:
                w = x.parent.left
                if w.color == True:
                    w.color = False
                    x.parent.color = True
                    self.right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == False and w.left.color == False:
                    w.color = True
                    x = x.parent
                else:
                    if w.left.color == False:
                        w.right.color = False
                        w.color = True
                        self.left_rotate(w)
                        w = x.parent
                    w.color = x.parent.color
                    x.parent.color = False
                    w.right.color = False
                    self.right_rotate(x.parent)
                    x = self.root
            x.color = False


if __name__ == "__main__":
    print("hello")
