from tkinter import *
from tkinter import ttk


class Calculator:

    def __init__(self, root):
        # Will hold the changing value stored in the entry
        self.entry_value = StringVar(root, value="")

        # Define title for the app
        root.title("Calculator")

        # Defines the width and height of the window
        root.geometry("483x220")

        # Block resizing of Window
        root.resizable(width=False, height=False)

        # Customize the styling for the buttons and entry
        style = ttk.Style()
        style.configure("TButton",
                        font="Serif 15",
                        padding=10)

        style.configure("TEntry",
                        font="Serif 18",
                        padding=10)

        # Create the text entry box
        self.number_entry = ttk.Entry(root,
                                      textvariable=self.entry_value, width=50)
        self.number_entry.grid(row=0, columnspan=4, sticky=(W, E))

        # ----- 1st Row -----

        self.button7 = ttk.Button(root, text="7").grid(row=1, column=0, sticky=(W, E))

        self.button8 = ttk.Button(root, text="8").grid(row=1, column=1, sticky=(W, E))

        self.button9 = ttk.Button(root, text="9").grid(row=1, column=2, sticky=(W, E))

        self.button_div = ttk.Button(root, text="/").grid(row=1, column=3, sticky=(W, E))

        # ----- 2nd Row -----

        self.button4 = ttk.Button(root, text="4").grid(row=2, column=0, sticky=(W, E))

        self.button5 = ttk.Button(root, text="5").grid(row=2, column=1, sticky=(W, E))

        self.button6 = ttk.Button(root, text="6").grid(row=2, column=2, sticky=(W, E))

        self.button_mult = ttk.Button(root, text="*").grid(row=2, column=3, sticky=(W, E))

        # ----- 3rd Row -----

        self.button1 = ttk.Button(root, text="1").grid(row=3, column=0, sticky=(W, E))

        self.button2 = ttk.Button(root, text="2").grid(row=3, column=1, sticky=(W, E))

        self.button3 = ttk.Button(root, text="3").grid(row=3, column=2, sticky=(W, E))

        self.button_add = ttk.Button(root, text="+").grid(row=3, column=3, sticky=(W, E))

        # ----- 4th Row -----

        self.button_clear = ttk.Button(root, text="AC").grid(row=4, column=0, sticky=(W, E))

        self.button0 = ttk.Button(root, text="0").grid(row=4, column=1, sticky=(W, E))

        self.button_equal = ttk.Button(root, text="=").grid(row=4, column=2, sticky=(W, E))

        self.button_sub = ttk.Button(root, text="-").grid(row=4, column=3, sticky=(W, E))


# Get the root window object
root = Tk()

# Create the calculator
calc = Calculator(root)

# Run the app until exited
root.mainloop()

