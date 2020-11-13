from .algorithm_base import AlgorithmBase

class QuickSort(AlgorithmBase):

    def __init__(self, unsorted_arr, console):
        super().__init__(console)
        self._unsorted_arr = unsorted_arr

    def quicksort(self, array):
        if len(array) < 2:
            return array
        else:
            pivot = array[0]
            less = [i for i in array[1:] if i <= pivot]
            greater = [i for i in array[1:] if i > pivot]
        return self.quicksort(less) + [pivot] + self.quicksort(greater)

    def run(self):
        self._announce()
        self._log("unordered[] = {}".format(self._unsorted_arr))
        self._log("running quicksort...")
        result = self.quicksort(self._unsorted_arr)
        self._log("sorted[] = {}".format(result))
        
