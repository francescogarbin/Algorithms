from .algorithm_base import AlgorithmBase

class BinarySearch(AlgorithmBase):

    def __init__(self, console):
        super().__init__(console)

    def binary_search(self, list, item):
        low = 0
        high = len(list) - 1
        while low <= high:
            mid = (low + high)
            guess = list[mid]
            if guess == item:
                return mid
            if guess > item:
                high = mid - 1
            else:
                low = mid + 1
        return None

    def run(self):
        vals = [1, 3, 5, 7, 9]
        item = 5
        self._announce()
        self._log("values[] = {}".format(vals))
        self._log("binary search index lookup of {}...".format(item))
        result = self.binary_search(vals, item)
        self._log("item {} found at index {}".format(item, result))





