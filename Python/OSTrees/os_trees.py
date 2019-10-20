from tqdm import tqdm
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import seaborn as sns
import pandas as pd
import sys
import random
import time


class Node:
    def __init__(self, key):
        # nil node
        # self.nil = Node(0)
        # self.nil.color = False
        # self.nil.left = None
        # self.nil.right = None
        # self.nil.size = 0

        self.parent = None
        self.left = None
        self.right = None
        self.key = key
        self.color = True # boolean (True: red or False: black), new node must be red   
        self.size = 1


class OrderStatisticTree:
    # structure inherited from RedBlackTree Class
    def __init__(self):
        self.nil = Node(0)
        self.nil.color = False
        self.nil.left = None
        self.nil.right = None
        self.nil.size = 0
        self.root = self.nil

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
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
        y.size = x.size
        x.size = x.left.size + x.right.size + 1


    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y
        y.size = x.size
        x.size = x.left.size + x.right.size + 1

    def tree_insert(self, key):
        z = Node(key)
        z.left = self.nil
        z.right = self.nil
        y = None
        x = self.root
        while x != self.nil:
            y = x
            y.size += 1
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

        # if the new node is root node, then we just return
        if z.parent == None:
            z.color = False
            return
        # if parent's parent is None then we just return
        if z.parent.parent == None:
            return

        self.insert_fixup(z)
        return z

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
            if z == self.root:
                break
        self.root.color = False

    def tree_delete(self, key):
        z = self.nil
        curr_node = self.root
        while curr_node != self.nil:
            if curr_node.key == key:
                z = curr_node
            if curr_node.key <= key:
                curr_node = curr_node.right
            else:
                curr_node = curr_node.left
        if z == self.nil:
            print("Node does not exist in tree")
            return

        curr_node = z
        while curr_node != None:
            curr_node.size -= 1
            curr_node = curr_node.parent

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
                temp = x.parent
                while(temp != y):
                    temp.size -= 1
                    temp = temp.parent
                y.size = y.left.size + 1

            self.tree_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
            y.size = y.left.size + y.right.size + 1
        if y_original_color == False:
            self.delete_fixup(x)

    def tree_transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
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

                # if w.right != self.nil and w.left != self.nil:
                
                if w.right.color == False:# and w.left.color == False:
                    w.color = True
                    x = x.parent
                else:
                    if w.left.color == False:
                        w.right.color = False
                        w.color = True
                        self.left_rotate(w)
                        w = x.parent.left

                    w.color = x.parent.color
                    x.parent.color = False
                    w.right.color = False
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = False

    def tree_os_select(self, x, i):
        # initial call ost.tree_select(ost.root, i), i=5
        r = x.left.size + 1
        if i == r:
            return x
        elif i < r:
            return self.tree_os_select(x.left, i)
        else:
            return self.tree_os_select(x.right, i-r)

    def tree_os_rank(self, x):
        r = x.left.size + 1
        y = x
        while y != self.root:
            if y == y.parent.right:
                r = r + y.parent.left.size + 1
            y = y.parent
        return r

    def tree_print(self, node, indent, last):
        if node != self.nil:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "    "
            else:
                sys.stdout.write("L----")
                indent += "|    "

            color = "RED" if node.color == True else "BLACK"
            print(str(node.key) + "(" + color + "  " + str(node.size) + ")")
            self.tree_print(node.left, indent, False)
            self.tree_print(node.right, indent, True)

    def tree_draw(self, node, G, color_map):
        if node == self.root:
            G.add_node(str(node.key))
            color_map.append('black')
            # return
        else:
            if node != self.nil:
                G.add_node(str(node.key))
                if node.color == False:
                    color_map.append('black')
                else:
                    color_map.append('red')
                G.add_edge(str(node.parent.key), str(node.key))
        if node.left != self.nil:
            self.tree_draw(node.left, G, color_map)
        if node.right != self.nil:
            self.tree_draw(node.right, G, color_map)



#######################################################################################################################
# Visualization Functions
#######################################################################################################################
def hierarchy_pos(G, root=None, width=1., vert_gap = 0.2, vert_loc = 0, xcenter = 0.5):

    '''
    From Joel's answer at https://stackoverflow.com/a/29597209/2966723.  
    Licensed under Creative Commons Attribution-Share Alike 

    If the graph is a tree this will return the positions to plot this in a 
    hierarchical layout.

    G: the graph (must be a tree)

    root: the root node of current branch 
    - if the tree is directed and this is not given, 
      the root will be found and used
    - if the tree is directed and this is given, then 
      the positions will be just for the descendants of this node.
    - if the tree is undirected and not given, 
      then a random choice will be used.

    width: horizontal space allocated for this branch - avoids overlap with other branches

    vert_gap: gap between levels of hierarchy

    vert_loc: vertical location of root

    xcenter: horizontal location of root
    '''
    if not nx.is_tree(G):
        raise TypeError('cannot use hierarchy_pos on a graph that is not a tree')

    if root is None:
        if isinstance(G, nx.DiGraph):
            root = next(iter(nx.topological_sort(G)))  #allows back compatibility with nx version 1.11
        else:
            root = random.choice(list(G.nodes))

    def _hierarchy_pos(G, root, width=1., vert_gap = 0.2, vert_loc = 0, xcenter = 0.5, pos = None, parent = None):
        '''
        see hierarchy_pos docstring for most arguments

        pos: a dict saying where all nodes go if they have been assigned
        parent: parent of this branch. - only affects it if non-directed

        '''

        if pos is None:
            pos = {root:(xcenter,vert_loc)}
        else:
            pos[root] = (xcenter, vert_loc)
        children = list(G.neighbors(root))
        if not isinstance(G, nx.DiGraph) and parent is not None:
            children.remove(parent)  
        if len(children)!=0:
            dx = width/len(children) 
            nextx = xcenter - width/2 - dx/2
            for child in children:
                nextx += dx
                pos = _hierarchy_pos(G,child, width = dx, vert_gap = vert_gap, 
                                    vert_loc = vert_loc-vert_gap, xcenter=nextx,
                                    pos=pos, parent = root)
        return pos


    return _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter)

def display_tree(T, figname=""):
    G = nx.Graph()
    color_map = []
    T.tree_draw(T.root, G, color_map)
    pos = hierarchy_pos(G, str(T.root.key))
    nx.draw(G, pos=pos, node_color=color_map)
    nx.draw_networkx_labels(G, pos=pos, font_color='w')
    plt.show()


if __name__ == "__main__":

    start = int(input('Start: '))
    end = int(input('End: '))
    step = int(input('Step: '))
    n = np.arange(start, end, step)
    avg_times = int(input('Averages: '))

    insert_time = []
    delete_time = []
    select_time = []
    rank_time = []
    for i in tqdm(n):
        avg_insert = 0
        avg_delete = 0
        avg_select = 0
        avg_rank = 0
        # building the tree
        ost = OrderStatisticTree()
        rand_array = random.sample(range(1, i+1), i)
        nodes = []
        for k in rand_array:
			temp_node = ost.tree_insert(k)
			nodes.append(temp_node)
		random_insert = list(range(i+1, i*10))
        # these numbers should not be in the tree
        random_insert = list(set(random_insert) - set(rand_array))
        np.random.shuffle(random_insert)
        for j in range(avg_times):
			k = np.random.choice(random_insert)
			# random_insert = np.delete(random_insert, k)
			start_insert = time.time_ns()
			node = ost.tree_insert(k)
			end_insert = time.time_ns()
            
			nodes.append(node)

            start_select = time.time_ns()
            ost.tree_os_select(ost.root, np.random.choice(np.arange(1, i)))
            end_select = time.time_ns()
        
            start_rank = time.time_ns()
            ost.tree_os_rank(node)
            end_rank = time.time_ns()

            start_delete = time.time_ns()
            ost.tree_delete(k)
            end_delete = time.time_ns()

            rb_insert = end_insert - start_insert
            rb_delete = end_delete - start_delete
            os_select = end_select - start_select
            os_rank = end_rank - start_rank
            
            avg_insert += rb_insert
            avg_delete += rb_delete
            avg_select += os_select
            avg_rank += os_rank
        
        insert_time.append(avg_insert/avg_times)
        delete_time.append(avg_delete/avg_times)
        select_time.append(avg_select/avg_times)
        rank_time.append(avg_rank/avg_times)



    insert_df = pd.DataFrame({'input': n, 'time': insert_time})
    delete_df = pd.DataFrame({'input': n, 'time': delete_time})
    select_df = pd.DataFrame({'input': n, 'time': select_time})
    rank_df = pd.DataFrame({'input': n, 'time': rank_time})

    insert_df.to_csv('insert.csv', header=True, index=False)
    delete_df.to_csv('delete.csv', header=True, index=False)
    select_df.to_csv('select.csv', header=True, index=False)
    rank_df.to_csv('rank.csv', header=True, index=False)


    #print(insert_time)
    #x = np.linspace(1, len(n), len(n))
    #print(x)
    #print(delete_time)
    #print(select_time)
    #print(rank_time)

   


    # ost.tree_print(ost.root, "", True)
    # display_tree(ost)
    # ost.tree_delete(34)
    # # ost.tree_delete(25)
    # ost.tree_print(ost.root, "", True)
    # display_tree(ost)

