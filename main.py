import os
import logging

import tkinter as tk
from tkinter import *
from tkinter import ttk

from src.classes.binary_search import BinarySearch
from src.classes.selection_sort import SelectionSort
from src.classes.quick_sort import QuickSort

class TextConsole(tk.Text):

    def __init__(self, root):
        super().__init__(root)

    def log(self, message):
        self.configure(state='normal')
        self.insert(INSERT, message + os.linesep)
        self.configure(state='disabled')


class ConsoleFrame(ttk.Frame):

    def __init__(self, root):
        super().__init__(root, borderwidth=1, padding="2")
        self.text_console = TextConsole(self)
        self.text_console.pack(fill=BOTH, expand=True)
        self.text_console.log("Click a button to run an algorithm :-)")
        self.pack(fill=BOTH, expand=True)

    def log(self, message):
        self.text_console.log(message)


class StatusBar(ttk.Frame):

    def __init__(self, root):
        super().__init__(root, padding="2")
        self.label = None
        self.setup_ui()

    def setup_ui(self):
        self.label = ttk.Label(self, text="Idle", padding="0 0 5 0")
        self.label.grid(row=0, column=0, sticky=E)
        self.pack(fill=X, expand=False)

    def set_message(self, message):
        self.label.text = message


class AppicationFrame(ttk.Frame):

    def __init__(self, root, styleName):
        super().__init__(root, style=styleName)
        self.console = None
        self.statusbar = None
        self.setup_ui()

    def setup_ui(self):
        self.grid(column=0, row=0, sticky=(N, W, E, S))
        toolbar = ttk.Frame(self, padding="3")
        button_one = ttk.Button(toolbar, text="Binary Search", 
                                command=self.on_binarysearch_clicked)
        button_one.pack(side=LEFT, padx=2)
        button_two = ttk.Button(toolbar, text="Selection Sort", 
                                command=self.on_selectionsort_clicked)
        button_two.pack(side=LEFT, padx=2)
        button_three = ttk.Button(toolbar, text="Quicksort",
                                  command=self.on_quicksort_clicked)
        button_three.pack(side=LEFT, padx=2)
        toolbar.pack(fill=X)
        self.console = ConsoleFrame(self)
        self.statusbar = StatusBar(self)
        self.pack(fill=BOTH, expand=True)

    def on_binarysearch_clicked(self):
        bsearch = BinarySearch(self.console)
        bsearch.run()

    def on_selectionsort_clicked(self):
        unsorted_values = [8,6,3,2]
        algo = SelectionSort(unsorted_values, self.console)
        algo.run()

    def on_quicksort_clicked(self):
        unsorted_values = [8,6,3,2]
        algo = QuickSort(unsorted_values, self.console)
        algo.run()


def main():
    logging.basicConfig(level='DEBUG', filename='../algorithms.log',
                        filemode='w',
                        format='%(name)s - %(levelname)s - %(message)s')
    logging.info("starting session...")
    root = Tk()
    root.style = ttk.Style()
    root.style.theme_use("clam")
    root.style.configure("My.TFrame", background='grey99')
    root.style.configure("My.TLabel", background='grey99')
    root.title("Algorithms")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    AppicationFrame(root, "My.TFrame")
    root.mainloop()


if __name__ == "__main__":
    main()

