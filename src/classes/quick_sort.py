class QuickSort:

    def __init__(self, unsorted_arr, console_log):
        self.console = console_log
        self.unsorted_arr = unsorted_arr

    def quicksort(self, array):
        if len(array) < 2:
            return array
        else:
            pivot = array[0]
            less = [i for i in array[1:] if i <= pivot]
            greater = [i for i in array[1:] if i > pivot]
        return self.quicksort(less) + [pivot] + self.quicksort(greater)

    def run(self):
        self.console.log("\n*** Quicksort ***")
        self.console.log("unordered[] = {}".format(self.unsorted_arr))
        self.console.log("running quicksort...")
        result = self.quicksort(self.unsorted_arr)
        self.console.log("sorted[] = {}".format(result))
        
