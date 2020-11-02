from collections import defaultdict
import random


class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._bucket = defaultdict(list)
        self._elements = list()
        self._idle_idx = list()
        self._index_set = set()
        # self._returned_idx_set = set()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        is_not_contains = True if val not in self._bucket.keys() else False
        if len(self._idle_idx) != 0:
            idx = self._idle_idx.pop()
            self._elements[idx] = val
        else:
            self._elements.append(val)
            idx = len(self._elements) - 1

        self._index_set.add(idx)
        self._bucket[val].append(idx)
        return is_not_contains

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        is_contains = True if val in self._bucket.keys() else False
        if is_contains:
            del_idx = self._bucket[val].pop()
            self._index_set.remove(del_idx)
            self._elements[del_idx] = None
            self._idle_idx.append(del_idx)
            if len(self._bucket[val]) == 0:
                del self._bucket[val]
        return is_contains

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        # if len(self._index_set) == 0 and len(self._returned_idx_set) != 0:
        #     self._index_set = self._returned_idx_set
        #     self._returned_idx_set = set()

        if len(self._index_set) != 0:
            indexes = list(self._index_set)
            idx = random.randint(0, len(indexes) - 1)
            return self._elements[indexes[idx]]
        return None


if __name__ == "__main__":
    obj = RandomizedCollection()
    print(obj.insert(1))
    print(obj.insert(1))
    print(obj.insert(2))
    print(obj.getRandom())
    print(obj.remove(1))
    print(obj.getRandom())

