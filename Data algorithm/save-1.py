# coding:utf-8


class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.l_child = None
        self.r_child = None


class Tree(object):
    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]

        """将二叉树上的每一个节点当成一个树来进行添加,采用广度遍历(队列)进行添加:根 左->右"""
        while queue:
            cur_node = queue.pop(0)
            if cur_node.l_child is None:  # 当树根节点的左子树为空,则直接将节点挂载到当前左子树
                cur_node.l_child = node
                return
            else:
                queue.append(cur_node.l_child)  # 使用广度遍历,添加左子节点

            if cur_node.r_child is None:
                cur_node.r_child = node
                return  # 添加完,需要直接返回,否则会进行无限添加
            else:
                queue.append(cur_node.r_child)

    def deeply_travel(self):
        """广度遍历:从上往下,每一层从左往右遍历(队列实现)"""
        if self.root is None:
            return
        queue = [self.root]

        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem, end=" ")
            if cur_node.l_child is not None:
                queue.append(cur_node.l_child)  # 使用广度遍历,读取左子节点

            if cur_node.r_child is not None:  # 同理
                queue.append(cur_node.r_child)

    """深度遍历：根的遍历顺序,左->右"""
    # 先序:根 左右
    # 中序:左 根 右
    # 后序:左右 根
    def pre_order(self, node):
        """前序遍历"""
        if node is None:
            return

        print(node.elem, end=" ")  # 打印当前节点元素
        self.pre_order(node.l_child)  # 递归查找树的左节点
        self.pre_order(node.r_child)

    def in_order(self, node):
        """中序遍历"""
        if node is None:
            return

        self.in_order(node.l_child)
        print(node.elem, end=" ")
        self.in_order(node.r_child)

    def post_order(self, node):
        """后序遍历"""
        if node is None:
            return

        self.post_order(node.l_child)
        self.post_order(node.r_child)
        print(node.elem, end=" ")


if __name__ == "__main__":
    tree = Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)

    tree.deeply_travel()
    print(" ")
    tree.pre_order(tree.root)  # 将已添加树上的节点进行遍历
    print(" ")
    tree.in_order(tree.root)
    print(" ")
    tree.post_order(tree.root)
    print(" ")
