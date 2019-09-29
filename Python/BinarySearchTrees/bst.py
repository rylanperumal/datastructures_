import matplotlib.pyplot as plt
import networkx as nx


class Node:

    def __init__(self, key):
        self.parent = None
        self.left = None
        self.right = None
        self.key = key
