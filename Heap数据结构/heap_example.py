import random


def heapify(l):
    """Turn l into a heap in place."""
    for i in range(len(l)):
        idx_cur = i
        while idx_cur != 0:
            idx_par = (idx_cur - 1) // 2
            if l[idx_par] > l[idx_cur]:
                l[idx_par], l[idx_cur] = (l[idx_cur], l[idx_par])
                idx_cur = idx_par
            else:
                break


def extract_min(l, length):
    if len(l) == 0:
        return None
    min_val = l[0]
    last_value = l[length - 1]
    length -= 1
    if length == 0:
        return min_val

    l[0] = last_value

    idx_cur = 0
    while idx_cur <= length:
        idx_child0 = idx_cur * 2 + 1
        idx_child1 = idx_cur * 2 + 2

        # idx_cur is leaf node
        if idx_child0 >= length:
            break

        idx_small_child = idx_child0

        if (idx_child1 < length and
                l[idx_child0] > l[idx_child1]):
            idx_small_child = idx_child1

        if l[idx_cur] > l[idx_small_child]:
            (l[idx_cur], l[idx_small_child]) = (
                l[idx_small_child], l[idx_cur])

        idx_cur = idx_small_child

    return min_val


def heap_sort(l):
    heapify(l)
    length = len(l)
    while length > 0:
        min_val = extract_min(l, length)
        l[length - 1] = min_val
        length -= 1
    l.reverse()


class Heap:
    def __init__(self):

        # Complete binary tree implemented using python list.
        self.tree = []

    def insert(self, key):
        idx_cur = len(self.tree)
        self.tree.append(key)
        while idx_cur != 0:
            idx_par = (idx_cur - 1) // 2
            if self.tree[idx_par] > self.tree[idx_cur]:
                (self.tree[idx_par], self.tree[idx_cur]) = (
                                  self.tree[idx_cur], self.tree[idx_par])
            idx_cur = idx_par

    def extract_min(self):
        if len(self.tree) == 0:
            return None
        min_val = self.tree[0]
        last_value = self.tree.pop()
        if len(self.tree) == 0:
            return min_val

        self.tree[0] = last_value

        idx_cur = 0
        while idx_cur <= len(self.tree):
            idx_child0 = idx_cur * 2 + 1
            idx_child1 = idx_cur * 2 + 2

            # idx_cur is leaf node
            if idx_child0 >= len(self.tree):
                break

            idx_small_child = idx_child0

            if (idx_child1 < len(self.tree) and
               self.tree[idx_child0] > self.tree[idx_child1]):
                idx_small_child = idx_child1

            if self.tree[idx_cur] > self.tree[idx_small_child]:
                (self.tree[idx_cur], self.tree[idx_small_child]) = (
                    self.tree[idx_small_child], self.tree[idx_cur])
            else:
                break

            idx_cur = idx_small_child

        return min_val


if __name__ == '__main__':
    unordered = list(range(10))
    random.shuffle(unordered)
    print('before heap sort:', unordered)

    l = unordered[:]
    heapify(l)
    print('unordered:', unordered)
    print('heapify:', l)
    heap_sort(l)
    print('heapsort:', l)

    # Construct heap
    my_heap = Heap()
    for i in range(len(unordered)):
        my_heap.insert(unordered[i])

    print('heap:', my_heap.tree)
    # Heap sort
    ordered = []
    for i in range(len(unordered)):
        ordered.append(my_heap.extract_min())
    print('after heap sort:', ordered)
