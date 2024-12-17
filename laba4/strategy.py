from abc import ABC, abstractmethod


class SortingStrategy(ABC):
    @abstractmethod
    def sort(self, data):
        pass


class BubbleSortStrategy(SortingStrategy):
    def sort(self, data):
        print("Bubble Sort: ", sorted(data))


class QuickSortStrategy(SortingStrategy):
    def sort(self, data):
        print("Quick Sort: ", sorted(data, reverse=True))


class Sorter:
    def __init__(self, strategy: SortingStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: SortingStrategy):
        self.strategy = strategy

    def sort_data(self, data):
        self.strategy.sort(data)


items = [5, 3, 8, 4, 2]
sorter = Sorter(BubbleSortStrategy())


sorter.sort_data(items)

sorter.set_strategy(QuickSortStrategy())
sorter.sort_data(items)
