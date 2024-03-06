import pytest

from asd.chapter_two.simple_tree import SimpleTree, SimpleTreeNode


@pytest.fixture()
def simple_tree():
    trees = [SimpleTreeNode(index, None) for index in range(1, 11)]
    tree = SimpleTree(trees[0])
    tree.AddChild(trees[0], trees[1])
    tree.AddChild(trees[1], trees[2])
    tree.AddChild(trees[1], trees[3])
    tree.AddChild(trees[2], trees[4])
    tree.AddChild(trees[2], trees[5])
    tree.AddChild(trees[2], trees[6])
    tree.AddChild(trees[3], trees[7])
    tree.AddChild(trees[3], trees[8])
    tree.AddChild(trees[3], trees[9])
    return tree


def test_add_child(simple_tree):
    leaf = simple_tree.LeafCount()
    all_nodes = simple_tree.GetAllNodes()
    tree = simple_tree.Count()
    node_3 = simple_tree.FindNodesByValue(3)
    simple_tree.set_level_tree()
    print(leaf, tree)

