class BitVector:
    def __init__(self, size):
        self.size = []
        size_len = size // 64
        if size_len >= 1:
            counter = 0
            while counter < size_len:
                self.size.append(64 * [0])
                counter += 1
            if size % 64 != 0:
                self.size += [(size - (size_len * 64)) * [0]]

        else:
            self.size = size * [0]
        self.size = self.size[::-1]

    def set(self, position):
        sector = -(position // 64 + 1)
        self.size[sector][-(position % 64)] = 1


    def reset(self, position):
        sector = -(position // 64 + 1)
        self.size[sector][-(position % 64)] = 0





b = BitVector(150)


print(b.size)
b.set(15)
print(b.size)
b.reset(15)
print(b.size)