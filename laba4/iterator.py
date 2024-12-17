class Iterator:
    def __init__(self, collection):
        self._collection = collection
        self._index = 0

    def has_next(self):
        return self._index < len(self._collection)

    def next(self):
        if not self.has_next():
            raise StopIteration("Stop iteration")
        value = self._collection[self._index]
        self._index += 1
        return value


class IterableCollection:
    def __init__(self, items):
        self._items = items

    def create_iterator(self):
        return Iterator(self._items)


collection = IterableCollection([1, 2, 3, 4, 5])
iterator = collection.create_iterator()

while iterator.has_next():
    print(iterator.next())
