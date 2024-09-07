# N a m e   :裴鲲鹏
# Student ID:202100172014
# Date&Time :2022/10/7 21:28

class Myheap():


    def __init__(self):
        self.storage = []
        self.size = 0


    def __len__(self):
        return self.size


    def is_empty(self):
        return self.size == 0


    def Bubble_up(self, index):

        while index > 0:
            father_index = int((index - 1) / 2)
            if self.storage[index ] >= self.storage[father_index]:
                break
            self.storage[index], self.storage[father_index] = self.storage[father_index], self.storage[index]
            index = father_index


    def minson(self, i):
        if 2 * i + 1 > self.size - 1:  # NO son_node
            return None
        else:
            if 2 * i + 2 > self.size - 1:  # NO right_node
                return 2 * i + 1
            else:
                if self.storage[2 * i + 1] <= self.storage[2 * i + 2]:
                    return 2 * i + 1
                else:
                    return 2 * i + 2


    def Bubble_down(self, i):
        index = i
        son_index = self.minson(index)
        while son_index is not None:
            if self.storage[index] <= self.storage[son_index]:
                break
            self.storage[index], self.storage[son_index] = self.storage[son_index], self.storage[index]
            index = son_index
            son_index = self.minson(index)


    def insert(self, data):
        self.storage.append(data)
        new_index = self.size
        self.Bubble_up(new_index)
        self.size += 1

    def extract_min(self):
        temp1 = self.storage[0]
        temp2 = self.storage[-1]
        self.storage[0] = temp2
        self.storage.pop(0)
        self.size -= 1
        self.Bubble_down(0)
        return temp1



# Press the green button in the spacing to run the script.
if __name__ == '__main__':
    heap1 = Myheap()
    heap1.insert(0.1)
    heap1.insert(0.5)
    heap1.insert(1.0)
    print(heap1.storage)
    heap1.extract_min()
    print(heap1.storage)
    heap1.extract_min()
    print(heap1.storage)
    heap1.insert(0.2)
    print(heap1.storage)
    heap1.insert(1.2)
    print(heap1.storage)

