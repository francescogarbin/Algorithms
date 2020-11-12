class BinarySearch:

    def __init__(self, console_log):
        self.console = console_log

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
        self.console.log("\n*** Binary Search ***")
        self.console.log("values[] = {}".format(vals))
        self.console.log("running binary search to look for index of value {}...".format(item))
        result = self.binary_search(vals, item)
        self.console.log("item {} found at index {}".format(item, result))





