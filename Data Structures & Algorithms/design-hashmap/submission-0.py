class MyHashMap:

    def __init__(self):
        self._size = 769
        self._container = []
        for _ in range(self._size):
            self._container.append([])

    def hash(self,key: int)-> int:
        return key % self._size

    def put(self, key: int, value: int) -> None:
        idx = self.hash(key)
        bucket = self._container[idx]
        i = 0 
        while i < len(bucket):
            if bucket[i][0] == key:
               bucket[i] = (key,value)
               return None
            i += 1
        bucket.append((key,value))
        return None

    def get(self, key: int) -> int:
        idx = self.hash(key)
        bucket = self._container[idx]
        i = 0
        while i < len(bucket):
            if bucket[i][0] == key:
                return bucket[i][1] 
            i += 1
        return -1


    def remove(self, key: int) -> None:
        idx = self.hash(key)
        bucket = self._container[idx]
        i = 0 
        while i < len(bucket):
            if bucket[i][0] == key:
                del bucket[i]
                return None
            i += 1
        return None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)