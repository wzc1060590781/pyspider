class Node():
    def __init__(self, value, left=None, right=None, father=None):
        self.value = value
        self.left = left
        self.right = right
        self.father = father


class Tree():
    def insert(self, root, node, father=None):
        if root == None:
            node.father = father
            root = node
        elif node.value > root.value:
            root.right = self.insert(root.right, node, root)
        elif node.value < root.value:
            root.left = self.insert(root.left, node, root)
        return root

    # def is_balanced(self):

    def pre_order(self, root):
        if root == None:
            return
        self.pre_order(root.left)
        print(root.value)
        self.pre_order(root.right)

    def query(self, root, value):
        if root == None:
            return -1
        elif value > root.value:
            return self.query(root.right, value)
        elif value < root.value:
            return self.query(root.left, value)
        else:
            return root

    def get_depth(self, root):
        if root == None:
            return 0
        nright = self.get_depth(root.right)
        nleft = self.get_depth(root.left)
        return max(nleft, nright) + 1

    def is_balanced(self, root):
        if root == None:
            return True
        nleft = self.get_depth(root.left)
        nright = self.get_depth(root.right)
        if abs(nleft - nright) > 1:
            return False
        else:
            return self.is_balanced(root.left) and self.is_balanced(root.right)

    def find_min(self, root):
        if root == None:
            return
        elif root.left:
            return self.find_min(root.left)
        else:
            return root

    def delete_node(self, root, value):
        # temp = root
        if self.query(root, value) == -1:
            return
        if root == None:
            return
        if value > root.value:
            root.right = self.delete_node(root.right, value)
        elif value < root.value:
            root.left = self.delete_node(root.left, value)
        else:
            if root.left and root.right:
                min_root = self.find_min(root.right)
                root.value = min_root.value
                root.right = self.delete_node(root.right, min_root.value)
            elif root.right == None and root.left == None:
                # 左右子树都为空
                root = None
            elif root.right == None:
                root = root.left
            elif root.left == None:
                root = root.right
        return root

    def insert_into_balanced_tree(self, root, node):
        self.insert(root, node)
        self.rotation(root)

    def rotation(self,root):
        # 判断根节点对应的树是否平衡
        if self.is_balanced_tree(root):
            return
        else:
            # 如果根节点的左子树和右子树中有一个不平衡，则对其子节点进行旋转
            if self.is_balanced_tree(root.left) and self.is_balanced_tree(root.right):
                if self.get_depth(root.right) - self.get_depth(root.left) > 1:
                # 右右，需要进行左旋
                    if self.get_depth(root.right.right) > self.get_depth(root.right.left):
                        self.left_rotation(root)
                    # 右左
                    else:
                        # 先将root节点的右节点进行右旋，再将root节点进行左旋
                        self.right_rotation(root.right)
                        self.left_rotation(root)
                # 树偏左
                elif self.get_depth(root.left) - self.get_depth(root.right) > 1:
                    # 左左，直接右旋
                    if self.get_depth(root.left.right) < self.get_depth(root.left.right):
                        self.right_rotation(root)
                    else:
                        self.left_rotation(root.left)
                        self.right_rotation(root)
                else:
                    self.rotation(root.left)
                    self.rotation(root.right)
            else:
                if self.is_balanced_tree(root.right):
                    root = root.left
                else:
                    root = root.right
                self.rotation(root)
            # 如果根节点左右子树均平衡，则对根节点进行旋转



    def left_rotation(self, root):
        # if root.father == None:
        #     root.right.left = root
        father = root.father
        new_root = root.right
        new_root.father = father
        if father:
            if father.left == root:
                father.left = new_root

            else:
                father.right = new_root

        else:
            root.right.father = None
        root.right = new_root.left
        new_root.left = root

    def right_rotation(self, root):
        # if root.father == None:
        #     root.right.left = root
        father = root.father
        new_root = root.left
        new_root.father = father
        if father:
            if father.right == root:
                father.right = new_root

            else:
                father.left = new_root

        root.left = new_root.right
        new_root.right = root

    def is_balanced_tree(self, root):
        if root == None:
            return True
        n_left = self.get_depth(root.left)
        n_right = self.get_depth(root.right)
        if abs(n_left - n_right) <= 1:
            return self.is_balanced_tree(root.left) and self.is_balanced_tree(root.right)
        else:
            return False


if __name__ == '__main__':
    node1 = Node(10)
    tree = Tree()
    node2 = Node(5)
    node3 = Node(12)
    node4 = Node(16)
    node5 = Node(8)
    node6 = Node(7)
    node7 = Node(9)
    node8 = Node(11)
    node9 = Node(4)
    node10 = Node(5)
    node11 = Node(9.5)
    # node12 = Node(3)
    tree.insert_into_balanced_tree(node1, node2)
    tree.insert_into_balanced_tree(node1, node3)
    tree.insert_into_balanced_tree(node1, node4)
    tree.insert_into_balanced_tree(node1, node5)
    tree.insert_into_balanced_tree(node1, node6)
    # print(tree.get_depth(node1))
    tree.insert_into_balanced_tree(node1, node7)
    tree.insert_into_balanced_tree(node1, node8)
    tree.insert_into_balanced_tree(node1, node9)
    # tree.insert_into_balanced_tree(node1, node10)
    tree.insert_into_balanced_tree(node1, node11)
    # tree.insert_into_balanced_tree(node1, node12)
    # print(node6.father.value)
    print(tree.is_balanced_tree(node1))
    # print(node11.father.value)
    # print(node11.father.father.father.value)
    # print(node5.father.value)
    # print(tree.query(node1, 19))
    # print(tree.is_balanced(node1))
    # print(tree.delete_node(node1, 5).value)
    # tree.pre_order(node1)
    # print(tree.is_balanced_tree(node1))
    print(node11.father.father.value)
    # print(tree.find_min(node1).value)
    # print(tree.query(node1,12).left.value)
    # print(node2.father.value)
