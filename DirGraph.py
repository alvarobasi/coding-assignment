class TreeNode(object):
    """
    The TreeNode object stores a new node in the directed graph. It contains information of its label name,
    its parent, a list of child TreeNode objects and its right sibling for preordered tree traversal algorithm.

    Arguments:
        name: name of the label stored within the node.

    Attributes:
        __name: Stores the node label.
        __parent: Stores the parent TreeNode object.
        __children: Stores a list() of its children TreeNode objects.
        __right_sibling: Stores the TreeNode object of its right sibling (node with
        the same parent located immediately on the next possition in the parent's children list())
    """
    def __init__(self, name):
        self.__name = name
        self.__parent = None
        self.__children = []
        self.__right_sibling = None

    def add_child(self, child_node):
        """
        Appends a new TreeNode object in the children list() and stores this new object in the right_sibling attribute
        of the previous child (if existing).

        Arguments:
            child_node: TreeNode object with the new label to be added to the graph stored in the name attribute.
        """
        child_node.set_parent(self)
        
        if self.has_children():
            self.get_children_list()[-1].set_right_sibling(child_node)

        self.get_children_list().append(child_node)

    def has_children(self):
        """
        Returns a boolean to show whether or not the children list() attribute is empty, that is, whether or not this
        node has children or if it is just a leaf in the tree graph.
        """
        return len(self.__children) > 0
    
    def is_root(self):
        """
        Returns a boolean showing whether or not the node object is the root of the tree, that is, whether or not it
        has a parent stored in the parent attribute.
        """  
        return not self.__parent

    def left_most_child(self):
        """
        Returns the child located most on the left of the children list() if it is not empty, or None if it is empty.
        """
        if self.has_children():
            return self.__children[0]
        
        return None

    def get_right_sibling(self):
        """
        Returns the right sibling object of the node.
        """  
        return self.__right_sibling

    def set_right_sibling(self, right_sibling):
        """
        Sets the right sibling object of the node.
        """
        self.__right_sibling = right_sibling

    def get_name(self):
        """
        Returns the label stored in the node.
        """
        return self.__name

    def get_parent(self):
        """
        Returns the node parent.
        """
        return self.__parent

    def set_parent(self, parent):
        """
        Sets the node parent.
        """
        self.__parent = parent

    def get_children_list(self):
        """
        Returns the children list().
        """
        return self.__children

    def get_level(self):
        """
        Returns the degree level of the node inside the tree graph.

        :returns level: int() storing the node level.
        """
        level = 0
        p = self.get_parent()
        while p:
            level += 1
            p = p.get_parent()
        return level

    def print(self):
        """
        Prints the tree graph starting from the self node.
        """
        indents = ' ' * self.get_level() * 3
        prefix = indents + "|__" if self.get_parent() else ""
        print(prefix + self.get_name())
        if self.has_children():
            for child in self.get_children_list():
                child.print()
