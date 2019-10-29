class TreeNode:
    def __init__(self, key, data, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right

    def get_key(self):  # return key of node
        return self.key

    def get_data(self):  # return data of node
        return self.data


class BinarySearchTree:

    def __init__(self):  # Returns empty BST
        self.root = None

    def is_empty(self):  # returns True if tree is empty, else False
        if self.root is None:
            return True

        else:
            return False

    def search(self, key):  # returns True if key is in a node of the tree, else False
        return self.search_helper(key, self.root)

    def search_helper(self, key, node):
        if node is None:            # check if tree is empty
            return False

        if node.key == key:         # return true if node is found
            return True

        elif node.key > key:            # search left tree if key is less than node key
            return self.search_helper(key, node.left)

        else:
            return self.search_helper(key, node.right)          # search right tree if key is greater than node key

    def insert(self, key, data=None):  # inserts new node w/ key and data
        # If an item with the given key is already in the BST, 
        # the data in the tree will be replaced with the new data
        # Example creation of node: temp = TreeNode(key, data)
        new_tree_node = TreeNode(key, data)         # create new node for tree

        if self.root is None:       # check if item is first into tree
            self.root = new_tree_node

        else:
            self.insert_helper(new_tree_node, self.root)         # call insert helper to find where node goes

    def insert_helper(self, node, root):
        if node.key == root.key:        # check if key already exists in list
            root.data = node.data

        elif node.key < root.key:         # check if new node key is less than root key
            if root.left is None:           # check if there is node left of node
                root.left = node
            else:
                self.insert_helper(node, root.left)         # if there is node left of root recall insert helper

        else:           # else new node key is greater than root key
            if root.right is None:          # check if there is a node right of root
                root.right = node
            else:
                self.insert_helper(node, root.right)            # if there is node left of root recall insert helper

    def find_min(self):  # returns a tuple with min key and data in the BST
        # returns None if the tree is empty
        return self.find_min_helper(self.root)

    def find_min_helper(self, node):
        if node.left is None:
            return node.key, node.data

        return self.find_min_helper(node.left)

    def find_max(self):  # returns a tuple with max key and data in the BST
        # returns None if the tree is empty
        return self.find_max_helper(self.root)

    def find_max_helper(self, node):
        if node.right is None:
            return node.key, node.data

        return self.find_max_helper(node.right)

    def tree_height(self):  # return the height of the tree
        # returns None if tree is empty
        height = self.tree_height_helper(self.root)
        if height == 0:         # if tree is empty return none
            return None

        return height - 1           # root doesn't count as part of height so height - 1

    def tree_height_helper(self, node, height=0):
        if node is None:            # check if tree is empty
            return 0

        else:
            max_left = self.tree_height_helper(node.left, height + 1)           # find height of left sub-tree
            max_right = self.tree_height_helper(node.right, height + 1)         # find height of right sub-tree

            if max_left > max_right:            # check if left or right tree is taller
                max_depth = max_left + 1
            else:
                max_depth = max_right + 1

        return max_depth

    def inorder_list(self):  # return Python list of BST keys representing in-order traversal of BST
        return self.inorder_helper(self.root)

    def inorder_helper(self, node, python_list=None):
        if python_list is None:         # creates empty python list
            python_list = []

        if node is None:            # checks if tree is empty
            return []

        if node.left is not None:
            self.inorder_helper(node.left, python_list)         # process left sub-tree
        python_list.append(node.key)            # process root

        if node.right is not None:
            self.inorder_helper(node.right, python_list)            # process right sub-tree

        return python_list

    def preorder_list(self):  # return Python list of BST keys representing pre-order traversal of BST
        return self.pre_order_helper(self.root)

    def pre_order_helper(self, node, python_list=None):
        if python_list is None:         # creates empty python list
            python_list = []

        if node is not None:
            python_list.append(node.key)            # append root first
            self.pre_order_helper(node.left, python_list)           # append left tree second
            self.pre_order_helper(node.right, python_list)          # append right tree last

        return python_list
        
    def delete(self, key): # deletes node containing key
        # Will need to consider all cases
        # This is the most difficult method - save it for last, so that
        # if you cannot get it to work, you can still get credit for 
        # the other methods
        # Returns True if the item was deleted, False otherwise

        if self.delete_helper(self.root, key) is not None:
            return True
        else:
            return False

    def delete_helper(self, node, key):
        if node is None:
            return None

        if node.key == key:

            # node is least in tree
            if node.left is None:
                temp = node.right
                node = None
                return temp

            # node is far right
            elif node.right is None:
                temp = node.left
                node = None
                return temp

            # node is root of tree
            elif (node.right is not None) and (node.left is not None):
                temp = node.right
                node = None
                return temp

            temp = self.find_min_for_delete(node.right)
            node.key = temp.key
            node.right = self.delete_helper(node.right, temp.key)

        elif node.key > key:
            node.left = self.delete_helper(node.left, key)

        elif node.key < key:
            node.right = self.delete_helper(node.right, key)

        return node

    def find_min_for_delete(self, node):
        if node.left is None:
            return node
        return self.find_min_helper(node.left)
