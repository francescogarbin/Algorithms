from .algorithm_base import AlgorithmBase

class SelectionSort(AlgorithmBase):

    def __init__(self, unsorted_arr, console):
        super().__init__(console)
        self._unsorted_arr = unsorted_arr

    def find_smallest(self, array):
        smallest = array[0]
        smallest_index = 0
        for i in range(1, len(array)):
            if array[i] < smallest:
                smallest = array[i]
                smallest_index = i
        return smallest_index

    def selection_sort(self, array):
        new_array = []
        for i in range(len(array)):
            smallest = self.find_smallest(array)
            new_array.append(array.pop(smallest))
        return new_array

    def run(self):
        self._announce()
        self._log("array[]={}".format(self._unsorted_arr))
        self._log("running selection sort...")
        sorted_array = self.selection_sort(self._unsorted_arr)
        self._log("sorted array[]={}".format(sorted_array))

