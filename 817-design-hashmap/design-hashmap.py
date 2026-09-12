class MyHashMap:

    def __init__(self):
        self.arr = []

    def put(self, key: int, value: int) -> None:
        for pair in self.arr:
            if pair[0] == key:
                pair[1] = value
                return
        self.arr.append([key, value])

    def get(self, key: int) -> int:
        for pair in self.arr:
            if pair[0] == key:
                return pair[1]
        return -1

    def remove(self, key: int) -> None:
        for i in range(len(self.arr)):
            if self.arr[i][0] == key:
                self.arr.pop(i)
                return