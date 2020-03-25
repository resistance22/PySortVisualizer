from tkinter import *
from tkinter import ttk
from Animations import Bubble_sort_anim

class SortVisualizer:
    def __init__(self, master):
        sorting_options = [
            "Choose a sorting algorithm",
            "bubble",
            "insertion",
            "heap"
        ]
        options = ttk.LabelFrame(master,width=800, height=200, text="Options", padding=5)
        options.pack()
        self._sort = StringVar()
        #The array size variable
        ttk.Label(options, text='Size(2<integer<50):').grid(row=0, column=0)
        #registering the validator function
        validate = options.register(self.size_valiator)

        self._sizeEntry = ttk.Entry(options, width=20, validate="key", validatecommand=(validate,"%P"))
        self._sizeEntry.grid(row=1, column=0, padx=50)
        ttk.Label(options, text="Algorithm:").grid(row=0, column=1)
        self._sortingMenu = ttk.OptionMenu(options, self._sort, *sorting_options).grid(row=1, column=1,padx=50,)

        startButton = ttk.Button(options, text="Sort",command=self.button_command)
        startButton.grid(row=0, column=2, rowspan=2,padx=50)

    def size_valiator(self,inpt):
        return inpt.isdigit() and int(inpt) > 1 and int(inpt) < 51 or inpt == ""
    def button_command(self):
        input = self._sizeEntry.get()
        if input is not "":
            size = int(input)
            anim = Bubble_sort_anim(size,100)
            anim.start_anim()

def main():
    root = Tk()
    SortVisualizer(root)
    root.mainloop()


if __name__ == "__main__": main()