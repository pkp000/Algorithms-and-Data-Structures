# N a m e   :裴鲲鹏
# Student ID:202100172014
# Date&Time :2022/9/25 10:20
import big_o


# Familiarize how to use this moudle
help(big_o.big_o)


class Node(object):
    '''Define a linked list node'''
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def __repr__(self):
        return f"Node({self.data})"


# First define the linked list class when there is no tail
class LinkedList(object):
    '''Define a linked list'''

    def __init__(self):
        self.head = Node()
        self.size = 0

    def get_size(self):
        return self.size

    def is_empty(self) -> bool:
        """Determine if it is empty"""
        return self.get_size() == 0

    def insert(self, index, data):
        '''
        Universal insertion function.
        index: position to insert
        data: element to be inserted
        '''
        if index < 0 or index > self.size:
            raise Exception("add fail. illegal index.")
        prev = self.head
        for i in range(index):
            prev = prev.next_node
        prev.next_node = Node(data, prev.next_node)
        self.size += 1

    def push_front(self,data):
        one_node = node()
        one_node.value = data
        one_node.next = head
        head = one_node

        # The second method, slightly faster after testing
        # self.insert(0, data)

    def push_back(self,data):
        self.insert(self.size,data)


# Inherit no-tail linked list and then add the definition of tail
class LinkedList_tail(LinkedList):
    def tail(self):
        one_node.next = Null
        tail.next = one_node
        tail = one_node


def main():
    link1 = LinkedList()
    print(big_o.big_o(link1.push_front, lambda n: list(range(n)), n_measures=100000)[0])
    print(big_o.big_o(link1.push_back, lambda n: list(range(n)), n_measures=100000)[0])
    link2 = LinkedList_tail()
    print(big_o.big_o(link2.push_back, lambda n: list(range(n)), n_measures=100000)[0])


if __name__ == '__main__':
    main()