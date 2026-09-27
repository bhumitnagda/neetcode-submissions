class Bucket:
    def __init__(self):
        self._container = []

    def add(self,key:int)-> None:
        if key not in self._container:
            self._container.append(key)

    def remove(self,key:int)->None:
        if key in self._container:
            self._container.remove(key)

    def contains(self, key:int)-> bool:
        if key in self._container:
            return True
        else:
            return False

class MyHashSet:

    def __init__(self):
        self._bucket = []
        self.size = 769
        for _ in range(self.size):
            self._bucket.append(Bucket())

    def hash(self,key:int)->int:
        return key % self.size

    def add(self, key: int) -> None:
        idx = self.hash(key)
        self._bucket[idx].add(key)

    def remove(self, key: int) -> None:
        idx = self.hash(key)
        self._bucket[idx].remove(key)

    def contains(self, key: int) -> bool:
        idx = self.hash(key)
        return self._bucket[idx].contains(key)


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)