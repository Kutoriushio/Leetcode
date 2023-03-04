class RandomizedSet:

    def __init__(self):
        self.dic = {}
        self.data = []

    def insert(self, val: int) -> bool:
        if val in self.dic:
            return False
        self.dic[val] = len(self.data)
        self.data.append(val)
        return True
    def remove(self, val: int) -> bool:
        if val not in self.dic:
            return False
        last = self.data[-1]
        remove_index = self.dic[val]
        self.dic[last] = remove_index
        self.data[remove_index] = last
        
        self.data.pop()
        self.dic.pop(val)
        return True

    def getRandom(self) -> int:
        return random.choice(self.data)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()