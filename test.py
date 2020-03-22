from tkinter import *
from tkinter import ttk


class SortVisualizer:
    def __init__(self, master):
        sorting_options = [
            "Choose a sorting algorithm",
            "bubble",
            "insertion",
            "heap"
        ]
        options = ttk.LabelFrame(master, text="Options", padding=5)
        options.pack()
        self._sort = StringVar()

        ttk.Label(options, text='Size:').grid(row=0, column=0)
        self._sizeEntry = ttk.Entry(options, width=20).grid(row=1, column=0, padx=50)

        ttk.Label(options, text="Algorithm:").grid(row=0, column=1)
        self._sortingMenu = ttk.OptionMenu(options, self._sort, *sorting_options).grid(row=1, column=1,padx=50)

        startButton = ttk.Button(options, text="Sort")
        startButton.grid(row=0, column=2, rowspan=2,padx=50)


def main():
    root = Tk()
    SortVisualizer(root)
    root.mainloop()


if __name__ == "__main__": main()