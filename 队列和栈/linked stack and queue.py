# N a m e   :裴鲲鹏
# Student ID:202100172014
# Date&Time :2022/9/26 21:10


class _Node():
    def __init__(self, element, next):
        self.element = element
        self.next = next


class Linked_Queue():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def first(self):
        # return but not remove the element at the front of the queue
        if self.is_empty():
            raise Empty('queue is empty')
        return self.head.element

    def dequeue(self):
        if self.is_empty():
            raise Empty('queue is empty')
        answer = self.head.element
        self.head = self.head.next
        self.size -= 1
        if self.is_e():
            self.tail = None
        return answer

    def enqueue(self,e):
        newset = self.Node(e,None)
        if self.is_empty():
            self.head = newset
        else:
            self.tail.next = newset
        self.tail = newset
        self.size += 1


class Linked_Stack:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def push(self, e):
        self.head = self.Node(e, self.head)
        self.size += 1
    
    def top(self):
        if self.is_empty():
            raise Empty('stack is empty')
        return self.head.element
    
    def pop(self):
        if self.is_empty():
            raise Empty('stack is empty')
        answer = self.head.element
        self.head = self.head.next
        self.size -= 1
        return answer

# def main():
#     pass


# if __name__ == '__main__':
#     main()
