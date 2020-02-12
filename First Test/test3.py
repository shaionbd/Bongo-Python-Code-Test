"""
:TODO Answer of "Explain the Runtime and Memory requirements for your solution."
Explanation of the Runtime and Memory requirements for my solution.

Time Complexity: Time complexity of above solution is O(h) where h is height of tree. Because you call the wile loop from
bottom(node_left/node_right) and jump it's previous parent which exists on bottom-1 tree and Continue it.
So runtime will be O(h).

Space Complexity: Space Complexity is O(1). Since it's calling as a iterative and does not need extra space to execute this program.

"""

class Node:
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent


def lca(node_left, node_right):
    if node_left == node_right:
        return node_right
    if node_left.parent is None:
        return node_left
    if node_right.parent is None:
        return node_right

    find_ancestor = None
    visited_nodes = [node_left]
    while node_left.parent is not None:
        if node_left.parent == node_right.parent or node_left.parent == node_right:
            find_ancestor = node_left.parent
            break
        node_left = node_left.parent
        visited_nodes.append(node_left.parent)

    while node_right.parent is not None:
        if node_right.parent in visited_nodes:
            find_ancestor = node_right.parent
            break
        node_right = node_right.parent
    if find_ancestor is None and node_right.parent in visited_nodes:
            find_ancestor = node_right
    return find_ancestor

if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2, node1)
    node3 = Node(3, node1)

    ancestor = lca(node1, node3)
    if ancestor:
        print("{} & {} ancestor is: {}".format(node1.value, node3.value, ancestor.value))
    else:
        print("No ancestor found")
