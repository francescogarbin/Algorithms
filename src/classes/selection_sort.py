class SelectionSort:

    def __init__(self, unsorted_arr, console_log):
        self.unsorted_arr = unsorted_arr
        self.console = console_log

    def find_smallest(self, arr):
        smallest = arr[0]
        smallest_index = 0
        for i in range(1, len(arr)):
            if arr[i] < smallest:
                smallest = arr[i]
                smallest_index = i
        return smallest_index

    def selection_sort(self, arr):
        newArr = []
        for i in range(len(arr)):
            smallest = self.find_smallest(arr)
            newArr.append(arr.pop(smallest))
        return newArr

    def run(self):
        self.console.log("\n*** Selection sort ***")
        self.console.log("array[]={}".format(self.unsorted_arr))
        self.console.log("running selection sort...")
        sorted_arr = self.selection_sort(self.unsorted_arr)
        self.console.log("sorted array[]={}".format(sorted_arr))

