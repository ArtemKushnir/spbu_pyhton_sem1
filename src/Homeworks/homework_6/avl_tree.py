from dataclasses import dataclass
from typing import TypeVar, Generic, Optional, Callable, Iterable

Value = TypeVar("Value")
Key = TypeVar("Key")


@dataclass
class TreeNode(Generic[Value]):
    key: int
    value: Value
    height: int = 0
    left: Optional["TreeNode[Value]"] = None
    right: Optional["TreeNode[Value]"] = None


@dataclass
class Tree(Generic[Value]):
    root: Optional[TreeNode[Value]] = None
    size: int = 0


def _get_height(node: TreeNode[Value]) -> int:
    if node is None:
        return -1
    return node.height


def _get_balance_factor(node: TreeNode[Value]) -> int:
    if node is None:
        return 0
    return _get_height(node.left) - _get_height(node.right)


def _update_height(node: TreeNode[Value]) -> None:
    node.height = max(_get_height(node.left), _get_height(node.right)) + 1


def create_tree() -> Tree[Value]:
    return Tree()


def put(tree: Tree[Value], key: int, value: Value) -> None:
    new_tree_node = TreeNode(key, value)
    if tree.root is None:
        tree.root = new_tree_node
    else:

        def put_recursion(curr_node: TreeNode[Value]) -> TreeNode[Value]:
            if curr_node is None:
                return new_tree_node
            elif curr_node.key == key:
                curr_node.value = value
                return curr_node
            elif curr_node.key > key:
                curr_node.left = put_recursion(curr_node.left)
            else:
                curr_node.right = put_recursion(curr_node.right)
            _update_height(curr_node)
            balance_factor = _get_balance_factor(curr_node)
            if abs(balance_factor) > 1:
                curr_node = _balancing_tree(curr_node, balance_factor)
            return curr_node

        tree.root = put_recursion(tree.root)
    tree.size += 1


def _balancing_tree(curr_node: TreeNode[Value], balance_factor: int) -> TreeNode[Value]:
    if balance_factor > 1:
        left_balance_factor = _get_balance_factor(curr_node.left)
        if left_balance_factor >= 0:
            curr_node = _perform_small_right_turn(curr_node)
        else:
            curr_node.left = _perform_small_left_turn(curr_node.left)
            curr_node = _perform_small_right_turn(curr_node)
    if balance_factor < -1:
        right_balance_factor = _get_balance_factor(curr_node.right)
        if right_balance_factor <= 0:
            curr_node = _perform_small_left_turn(curr_node)
        else:
            curr_node.right = _perform_small_right_turn(curr_node.right)
            curr_node = _perform_small_left_turn(curr_node)
    return curr_node


def _perform_small_left_turn(curr_node: TreeNode[Value]) -> TreeNode[Value]:
    new_node = curr_node.right
    curr_node.right = new_node.left
    new_node.left = curr_node
    _update_height(curr_node)
    _update_height(new_node)
    return new_node


def _perform_small_right_turn(curr_node: TreeNode[Value]) -> TreeNode[Value]:
    new_node = curr_node.left
    curr_node.left = new_node.right
    new_node.right = curr_node
    _update_height(curr_node)
    _update_height(new_node)
    return new_node


def remove(tree: Tree[Value], key: int) -> Value:
    if not has_key(tree, key):
        raise ValueError(f"no such key {key}")

    def remove_recursion(
        curr_node: TreeNode[Value],
    ) -> tuple[Optional[TreeNode[Value]], Value]:
        if curr_node.key < key:
            new_right_child, value = remove_recursion(curr_node.right)
            curr_node.right = new_right_child
            _update_height(curr_node)
            balance_factor = _get_balance_factor(curr_node)
            if abs(balance_factor) > 1:
                curr_node = _balancing_tree(curr_node, balance_factor)
            return curr_node, value
        elif curr_node.key > key:
            new_left_child, value = remove_recursion(curr_node.left)
            curr_node.left = new_left_child
            _update_height(curr_node)
            balance_factor = _get_balance_factor(curr_node)
            if abs(balance_factor) > 1:
                curr_node = _balancing_tree(curr_node, balance_factor)
            return curr_node, value
        if curr_node.left is None and curr_node.right is None:
            return None, curr_node.value
        elif curr_node.left is None or curr_node.right is None:
            new_node = curr_node.left if curr_node.left is not None else curr_node.right
            return new_node, curr_node.value
        else:
            result = curr_node.value
            new_key, new_value = _find_min_element(curr_node.right)
            remove(tree, new_key)
            tree.size += 1
            curr_node.key = new_key
            curr_node.value = new_value
            return curr_node, result

    tree.root, value = remove_recursion(tree.root)
    tree.size -= 1
    return value


def _find_min_element(curr_node: TreeNode) -> tuple[int, Value]:
    while curr_node.left is not None:
        curr_node = curr_node.left
    return curr_node.key, curr_node.value


def get(tree: Tree[Value], key: int) -> Value:
    if not has_key(tree, key):
        raise ValueError(f"no such key {key}")
    curr_node = tree.root
    while curr_node is not None:
        if curr_node.key == key:
            return curr_node.value
        elif key > curr_node.key:
            curr_node = curr_node.right
        elif key < curr_node.key:
            curr_node = curr_node.left


def has_key(tree: Tree[Value], key: int) -> bool:
    curr_node = tree.root
    while curr_node is not None:
        if curr_node.key == key:
            return True
        elif key > curr_node.key:
            curr_node = curr_node.right
        elif key < curr_node.key:
            curr_node = curr_node.left
    return False


def get_lower_bound(tree: Tree, key: int) -> int:
    if _is_empty(tree):
        raise ValueError("the tree is empty")
    result = None
    curr_node = tree.root
    while curr_node is not None:
        if key > curr_node.key:
            curr_node = curr_node.right
        elif key < curr_node.key:
            result = curr_node.key
            curr_node = curr_node.left
        else:
            return curr_node.key
    if result is None:
        raise ValueError(f"there is no key larger than {key}")
    return result


def get_upper_bound(tree: Tree, key: int) -> int:
    if _is_empty(tree):
        raise ValueError("the tree is empty")
    result = None
    curr_node = tree.root
    while curr_node is not None:
        if key >= curr_node.key:
            curr_node = curr_node.right
        elif key < curr_node.key:
            result = curr_node.key
            curr_node = curr_node.left
    if result is None:
        raise ValueError(f"there is no key larger than {key}")
    return result


def get_maximum(tree: Tree) -> int:
    if _is_empty(tree):
        raise ValueError("tree is clear")
    new_node = tree.root
    while new_node.right is not None:
        new_node = new_node.right
    return new_node.key


def get_minimum(tree: Tree) -> int:
    if _is_empty(tree):
        raise ValueError("tree is clear")
    new_node = tree.root
    while new_node.left is not None:
        new_node = new_node.left
    return new_node.key


def _is_empty(tree: Tree) -> bool:
    return tree.size == 0


def _preorder_comparator(node: TreeNode[Value]) -> Iterable[TreeNode[Value]]:
    return filter(None, (node, node.left, node.right))


def _inorder_comparator(node: TreeNode[Value]) -> Iterable[TreeNode[Value]]:
    return filter(None, (node.left, node, node.right))


def _postorder_comparator(node: TreeNode[Value]) -> Iterable[TreeNode[Value]]:
    return filter(None, (node.left, node.right, node))


def traverse(tree: Tree[Value], order: str) -> list[[tuple[int, Value]]]:
    values = []

    def traverse_recursion(curr_node: TreeNode[Value], order_func: Callable):
        node_order = order_func(curr_node)
        for node in node_order:
            if node is not curr_node:
                traverse_recursion(node, order_func)
            else:
                values.append((node.key, node.value))

    if order == "preorder":
        traverse_recursion(tree.root, _preorder_comparator)
    elif order == "inorder":
        traverse_recursion(tree.root, _inorder_comparator)
    elif order == "postorder":
        traverse_recursion(tree.root, _postorder_comparator)
    return values


def delete_tree(tree: Tree[Value]) -> None:
    del tree.root
    del tree.size
