class Student:
    def __init__(self, number, name):
        self.grade = number  # this will serve as the object's key
        self.name = name

    def __lt__(self, kq):
        # FIXME: Write this function
        if self.grade < kq.grade:
            return True
        else:
            return False

    def __gt__(self, kq):
        # FIXME: Write this function
        if self.grade > kq.grade:
            return True
        else:
            return False

    def __eq__(self, kq):
        # FIXME: Write this function
        if self.grade == kq.grade:
            return True
        else:
            return False

    def __str__(self):
        # FIXME: Write this function
        if self.grade is not None:
            return str(self.grade)


class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


# when this is a primitive, this serves as the node's key

class BST:
    def __init__(self, start_tree=None) -> None:
        """ Initialize empty tree """
        self.root = None  # populate tree with initial nodes (if provided)
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self):
        """Traverses the tree using "in-order" traversal
        and returns content of tree nodes as a text string"""
        values = [str(_) for _ in self.in_order_traversal()]
        return "TREE in order { " + ", ".join(values) + " }"

    def add(self, val):
        """
        Creates and adds a new node to the BSTree.
        If the BSTree is empty, the new node should added as the root.
        Args:
            val: Item to be stored in the new node
        """
        # FIXME: Write this function
        if self.root is None:
            self.root = TreeNode(val)
        else:
            newNode = TreeNode(val)
            cur = self.root
            while cur is not None:
                P = cur
                if val < cur.val:
                    if cur.left is None:
                        cur.left = newNode
                        break
                    else:
                        cur = cur.left
                else:
                    if cur.right is None:
                        cur.right = newNode
                        break
                cur = cur.right

    def in_order_traversal(self, cur_node=None, visited=None) -> []:
        """
        Perform in-order traversal of the tree and return a list of visited nodes
        """
        if visited is None:
            # first call to the function -> create container to store list of visited nodes             #
            # and initiate recursive calls starting with the root node
            visited = []
            self.in_order_traversal(self.root, visited)
            # not a first call to the function
            # base case - reached the end of current subtree -> backtrack
            if cur_node is None:
                return visited
                # recursive case -> sequence of steps for in-order traversal:
                # visit left subtree, store current node value, visit right subtree
            self.in_order_traversal(cur_node.left, visited)
            visited.append(cur_node.val)
            self.in_order_traversal(cur_node.right, visited)
            return visited

    def pre_order_traversal(self, cur_node=None, visited=None) -> []:
        """         Perform pre-order traversal of the tree and return a list of visited nodes
        Returns:             A list of nodes in the specified ordering
        """
        # FIXME: Write this function
        if visited is None:
            # first call to the function -> create container to store list of visited nodes
            # and initiate recursive calls starting with the root node
            visited = []
            self.in_order_traversal(self.root, visited)
            # not a first call to the function
            # base case - reached the end of current subtree -> backtrack
            if cur_node is None:
                return visited
                # recursive case -> sequence of steps for in-order traversal:
                # visit left subtree, store current node value, visit right subtree
            self.in_order_traversal(cur_node.left, visited)
            visited.append(cur_node.val)
            self.in_order_traversal(cur_node.right, visited)
            return visited

    def post_order_traversal(self, cur_node=None, visited=None) -> []:
        """         Perform post-order traversal of the tree and return a list of visited nodes
        Returns:             A list of nodes in the specified ordering         """
        # FIXME: Write this function
        if visited is None:
            # first call to the function -> create container to store list of visited nodes
            # and initiate recursive calls starting with the root node
            visited = []
            self.in_order_traversal(self.root, visited)
            # not a first call to the function
            # base case - reached the end of current subtree -> backtrack
            if cur_node is None:
                return visited
                # recursive case -> sequence of steps for in-order traversal:
                # visit left subtree, store current node value, visit right subtree
            self.in_order_traversal(cur_node.left, visited)
            visited.append(cur_node.val)
            self.in_order_traversal(cur_node.right, visited)
            return visited

    def contains(self, kq):
        """         Searches BSTree to determine if the query key (kq) is in the BSTree.
        Args:             kq: query key
        Returns:          True if kq is in the tree, otherwise False         """
        in_order = self.in_order_traversal()
        for i in in_order:
            if kq == i:
                return True
            return False

    def left_child(self, node):
        """         Returns the left-most child in a subtree.
        Args:             node: the root node of the subtree
        Returns:             The left-most node of the given subtree
        """
        # FIXME: Write this function
        cur = node
        while cur.left is not None:
            cur = cur.left
            return cur

    def get_first(self):
        """
        Gets the val of the root node in the BSTree.
        Returns: val of the root node, return None if BSTree is empty
        """
        # FIXME: Write this function
        return self.root.val


s = Student(1, "Shweta")
t = BST()
BST.add(t, s)
