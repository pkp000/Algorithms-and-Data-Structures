"""Implement heap data structure with multi-linked list."""
from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.ch_left = None
        self.ch_right = None


class Heap:
    def __init__(self):
        self.root = None
        # Last node in the complete BT, which is the first
        # candidate to be moved to root during extract_min.
        self.node_to_del = None
        self.insertion_pos = deque()

    def insert(self, key):
        one_node = Node(key)
        if self.root is None:
            self.root = one_node
            self.insertion_pos.append(self.root)
            return

        node_cur = self.insertion_pos.popleft()
        self.insertion_pos.append(one_node)
        if node_cur.ch_left is None:
            node_cur.ch_left = one_node
            self.insertion_pos.appendleft(node_cur)
        else:
            node_cur.ch_right = one_node

        one_node.parent = node_cur

        # Bubble-up
        node_tmp = one_node
        while node_tmp.parent is not None:
            if node_tmp.parent.data > node_tmp.data:
                node_tmp.parent.data, node_tmp.data = (
                    node_tmp.data, node_tmp.parent.data)
                node_tmp = node_tmp.parent
            else:
                break

    def extract_min(self):
        if self.root is None:
            return None
        min_val = self.root.data

        # Only one element.
        if self.root.ch_left is None and self.root.ch_right is None:
            self.root = None
            self.insertion_pos = deque()
            return min_val

        # Stack-like operation
        last_node = self.insertion_pos.pop()
        self.root.data = last_node.data

        if last_node.parent.ch_right is not None:
            last_node.parent.ch_right = None
            self.insertion_pos.appendleft(last_node.parent)
        else:
            last_node.parent.ch_left = None

        # Bubble-down
        node_cur = self.root
        while True:
            left = node_cur.ch_left
            right = node_cur.ch_right

            node_min = node_cur
            swap = False
            if left is not None and left.data < node_min.data:
                node_min = left
                swap = True
            if right is not None and right.data < node_min.data:
                node_min = right
                swap = True

            if not swap:
                break

            node_cur.data, node_min.data = (node_min.data, node_cur.data)
            node_cur = node_min

        return min_val

    def __str__(self):
        heap_list = []
        # Breadth first traversal.
        dq = deque()
        dq.append(self.root)
        try:
            while True:
                one_node = dq.popleft()
                if one_node.ch_left is not None:
                    dq.append(one_node.ch_left)
                if one_node.ch_right is not None:
                    dq.append(one_node.ch_right)
                heap_list.append(one_node.data)
        except IndexError:
            pass

        return str(heap_list)

if __name__ == '__main__':
    unordered = [4, 1, 7, 2, 6, 3, 5, 0, 9, 8]
    # reference heap: [0, 1, 3, 2, 6, 7, 5, 4, 9, 8]

    # Construct heap
    my_heap = Heap()
    # for i in unordered:
    #     my_heap.insert(i)

    # print('heap:', my_heap)

    # ordered = []
    # for i in range(len(unordered)):
    #     ordered.append(my_heap.extract_min())
    # print('after heap sort:', ordered)

    for i in range(5):
        my_heap.insert(unordered[i])

    print('heap:', my_heap)

    l = []
    for i in range(2):
        l.append(my_heap.extract_min())
    print('extract:', l)
    print('heap:', my_heap)

    for i in range(5, 10):
        my_heap.insert(unordered[i])
    print('heap:', my_heap)

    l = []
    for i in range(8):
        l.append(my_heap.extract_min())
    print(l)