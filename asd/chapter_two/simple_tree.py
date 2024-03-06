from typing import List, Any


class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.Children = []  # список дочерних узлов
        self.level = None

    def __str__(self):
        return f"Node {self.value}, lvl = {self.level}"


class SimpleTree:

    def __init__(self, root: SimpleTreeNode = None):
        self.Root = root  # корень, может быть None

    def AddChild(self, parent_node: SimpleTreeNode, new_child: SimpleTreeNode) -> None:
        if parent_node is None:
            self.Root = SimpleTreeNode(new_child, None)
            return
        parent_node.Children.append(new_child)
        new_child.Parent = parent_node

    def DeleteNode(self, node_to_delete: SimpleTreeNode) -> None:
        node_to_delete.Parent.Children.remove(node_to_delete)
        node_to_delete.Parent = None

    def GetAllNodes(self) -> List:
        result = []
        self._get_all_node(self.Root, result)
        return result

    def _get_all_node(self, node: SimpleTreeNode, result: list) -> None:
        result.append(node)
        for child in node.Children:
            self._get_all_node(child, result)

    def FindNodesByValue(self, val):
        node_with_value = []
        self._find_nodes_by_value(val, self.Root, node_with_value)
        return node_with_value

    def _find_nodes_by_value(self, val: Any, node: SimpleTreeNode, output_node: list) -> None:
        if node.NodeValue == val:
            output_node.append(node)
        for child in node.Children:
            self._find_nodes_by_value(val, child, output_node)

    def MoveNode(self, original_node: SimpleTreeNode, new_parent: SimpleTreeNode):
        self.DeleteNode(original_node)
        self.AddChild(new_parent, original_node)

    def Count(self):
        return len(self.GetAllNodes())

    def _get_count_tree(self, node: SimpleTreeNode, count) -> int:
        if len(node.Children) == 0:
            return 0
        if len(node.Parent) > 0 and len(node.Children) > 0:
            return 1
        return sum([self._get_count_tree(child, count) for child in node.Children])

    def LeafCount(self):
        return self._get_count_leaf(self.Root, 0)

    def _get_count_leaf(self, node: SimpleTreeNode, count) -> int:
        if len(node.Children) == 0:
            return 1
        return sum([self._get_count_leaf(child, count) for child in node.Children])

    def set_level_tree(self):
        self._set_level(self.Root)

    def _set_level(self, node: SimpleTreeNode):
        if not node.Parent:
            node.level = 1
        if not node.level:
            node.level = node.Parent.level + 1
        for child in node.Children:
            self._set_level(child)
