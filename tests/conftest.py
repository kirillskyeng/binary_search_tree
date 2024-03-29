import pytest

from src.binary_search_tree import BinarySearchTree


@pytest.fixture
def bst_root():
    """Создаем BST с одним узлом в вершине."""
    bst = BinarySearchTree()
    bst.insert({'id': 40})
    return bst


@pytest.fixture
def bst_full():
    """Создаем BST с полными тремя уровнями."""
    bst = BinarySearchTree()
    bst.insert({'id': 40})
    bst.insert({'id': 30})
    bst.insert({'id': 50})
    bst.insert({'id': 25})
    bst.insert({'id': 35})
    bst.insert({'id': 45})
    bst.insert({'id': 60})
    return bst
