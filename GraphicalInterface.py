from Equation import Equation
import tkinter as tk
from tkinter import Grid, Frame


# Inherits from the tk.Frame class
class Calculator(tk.Frame):
    """Inherits from the tk.Frame class
    master = An instance of Tk() as a parameter
    super() = This uses the __init__ from the tk.Frame class
    """
    def __init__(self, master):
        super().__init__(master, relief=tk.RAISED)
        # self.pack() adds this instance to the window (master)
        Grid.rowconfigure(master, 0, weight=1)
        Grid.columnconfigure(master, 0, weight=1)
        self.grid(column=0, row=0, sticky="N"+'S'+'E'+'W')
        grid = Frame(self)
        grid.grid(sticky="N"+'S'+'E'+'W', column=0, row=5, columnspan=2)
        Grid.columnconfigure(master, 0, weight=1)
        Grid.rowconfigure(master, 5, weight=1)
        #self.pack()
        # Start an Equation instance and set it to an empty string
        self.equation = Equation()
        self.equation_output = tk.StringVar("")

        # Add the title to the window
        master.title("Calculator")

        # Add the equation window that shows what is being entered
        self.equation_window = tk.Label(textvariable=self.equation_output,
                                        fg="black",
                                        bg="light grey",
                                        height=3)
        #self.equation_window.pack(side=tk.TOP)
        self.equation_window.grid(column=0, row=0, columnspan=4, sticky="N"+'S'+'E'+'W')

        # Add all the number buttons
        self.one_button = tk.Button(
            text="1",
            bg="grey",
            fg="black",
            width=10,
            height=3,
            command=lambda: [Equation.numeric_input(self.equation, "1"),
                             self.equation_output.set(self.equation.equation_output())]
        )
        #self.one_button.pack(side=tk.LEFT)
        self.one_button.grid(column=0, row=2, sticky="N"+'S'+'E'+'W')
        self.two_button = tk.Button(
            text="2",
            bg="grey",
            fg="black",
            width=10,
            height=3,
            command=lambda: [Equation.numeric_input(self.equation, "2"),
                             self.equation_output.set(self.equation.equation_output())]
        )
        #self.two_button.pack(side=tk.LEFT)
        self.two_button.grid(column=1, row=2, sticky="N"+'S'+'E'+'W')
        self.three_button = tk.Button(
            text="3",
            bg="grey",
            fg="black",
            width=10,
            height=3,
            command=lambda: [Equation.numeric_input(self.equation, "3"),
                             self.equation_output.set(self.equation.equation_output())]
        )
        self.three_button.grid(column=2, row=2, sticky="N"+'S'+'E'+'W')

        self.four_button = tk.Button(
            text="4",
            bg="grey",
            fg="black",
            width=10,
            height=3,
            command=lambda: [Equation.numeric_input(self.equation, "4"),
                             self.equation_output.set(self.equation.equation_output())]
        )
        self.four_button.grid(column=0, row=3, sticky="N"+'S'+'E'+'W')
        self.five_button = tk.Button(
            text="5",
            bg="grey",
            fg="black",
            width=10,
            height=3,
            command=lambda: [Equation.numeric_input(self.equation, "5"),
                             self.equation_output.set(self.equation.equation_output())]
        )
        self.five_button.grid(column=1, row=3, sticky="N"+'S'+'E'+'W')

        self.six_button = tk.Button(
            text="6",
            bg="grey",
            fg="black",
            width=10,
            height=3,
            command=lambda: [Equation.numeric_input(self.equation, "6"),
                             self.equation_output.set(self.equation.equation_output())]
        )
        self.six_button.grid(column=2, row=3, sticky="N"+'S'+'E'+'W')
        self.seven_button = tk.Button(
            text="7",
            bg="grey",
            fg="black",
            width=10,
            height=3,
            command=lambda: [Equation.numeric_input(self.equation, "7"),
                             self.equation_output.set(self.equation.equation_output())]
        )
        self.seven_button.grid(column=0, row=4, sticky="N"+'S'+'E'+'W')

        self.eight_button = tk.Button(
            text="8",
            bg="grey",
            fg="black",
            width=10,
            height=3,
            command=lambda: [Equation.numeric_input(self.equation, "8"),
                             self.equation_output.set(self.equation.equation_output())]
        )
        self.eight_button.grid(column=1, row=4, sticky="N"+'S'+'E'+'W')
        self.nine_button = tk.Button(
            text="9",
            bg="grey",
            fg="black",
            width=10,
            height=3,
            command=lambda: [Equation.numeric_input(self.equation, "9"),
                             self.equation_output.set(self.equation.equation_output())]
        )
        self.nine_button.grid(column=2, row=4, sticky="N"+'S'+'E'+'W')

        self.zero_button = tk.Button(
            text="0",
            bg="grey",
            fg="black",
            width=10,
            height=3,
            command=lambda: [Equation.numeric_input(self.equation, "0"),
                             self.equation_output.set(self.equation.equation_output())]
        )
        self.zero_button.grid(column=0, row=5, sticky="N"+'S'+'E'+'W')

        # Add all the expression buttons
        self.addition_button = tk.Button(
            text="+",
            bg="grey",
            fg="black",
            width=10,
            height=3,
            command=lambda: [Equation.expression_input(self.equation, '+'),
                             self.equation_output.set(self.equation.equation_output())]
        )
        self.addition_button.grid(column=3, row=2, sticky="N"+'S'+'E'+'W')

        self.subtraction_button = tk.Button(
        text="-",
        bg="grey",
        fg="black",
        width=10,
        height=3,
        command=lambda: [Equation.expression_input(self.equation, '-'),
                         self.equation_output.set(self.equation.equation_output())]
        )
        self.subtraction_button.grid(column=3, row=3, sticky="N"+'S'+'E'+'W')

        self.multiplication_button = tk.Button(
            text="x",
            bg="grey",
            fg="black",
            width=10,
            height=3,
            command=lambda: [Equation.expression_input(self.equation, '*'),
                             self.equation_output.set(self.equation.equation_output())]
        )
        self.multiplication_button.grid(column=3, row=4, sticky="N"+'S'+'E'+'W')

        self.division_button = tk.Button(
            text="/",
            bg="grey",
            fg="black",
            width=10,
            height=3,
            command=lambda: [Equation.expression_input(self.equation, '/'),
                             self.equation_output.set(self.equation.equation_output())]
        )
        self.division_button.grid(column=3, row=1, sticky="N"+'S'+'E'+'W')

        self.decimal_button = tk.Button(
            text=".",
            bg="grey",
            fg="black",
            width=10,
            height=3,
            command=lambda: [Equation.decimal_input(self.equation, '.'),
                             self.equation_output.set(self.equation.equation_output())]
        )
        self.decimal_button.grid(column=1, row=5, sticky="N"+'S'+'E'+'W')

        self.open_paren_button = tk.Button(
            text="(",
            bg="grey",
            fg="black",
            width=10,
            height=3,
            command=lambda: [Equation.open_paren_input(self.equation, '('),
                             self.equation_output.set(self.equation.equation_output())]
        )
        self.open_paren_button.grid(column=0, row=1, sticky="N"+'S'+'E'+'W')
        self.closed_paren_button = tk.Button(
            text=")",
            bg="grey",
            fg="black",
            width=10,
            height=3,
            command=lambda: [Equation.closed_paren_input(self.equation, ')'),
                             self.equation_output.set(self.equation.equation_output())]
        )
        self.closed_paren_button.grid(column=1, row=1, sticky="N"+'S'+'E'+'W')

        self.exponent_button = tk.Button(
            # TODO add an exponent image instead of text="**"
            text="**",
            bg="grey",
            fg="black",
            width=10,
            height=3,
            command=lambda: [Equation.expression_input(self.equation, '**'),
                             self.equation_output.set(self.equation.equation_output())]
        )
        self.exponent_button.grid(column=2, row=1, sticky="N"+'S'+'E'+'W')
        self.equals_button = tk.Button(
            # TODO Add functionality to equals button, ex: answer is displayed as equation output
            text="=",
            bg="grey",
            fg="black",
            width=10,
            height=3,
            command=lambda: [Equation.equals_input(self.equation, '='),
                             self.equation_output.set(self.equation.equation_output())]
        )
        self.equals_button.grid(column=2, row=5, sticky="N"+'S'+'E'+'W')
        self.clear_button = tk.Button(
            # TODO Add functionality to equals button, ex: answer is displayed as equation output
            text="Clear",
            bg="grey",
            fg="black",
            width=10,
            height=3,
            command=lambda: [Equation.clear_input(self.equation),
                             self.equation_output.set(self.equation.equation_output())]
        )
        self.clear_button.grid(column=3, row=5, sticky="N"+'S'+'E'+'W')

        for x in range(4):
            Grid.columnconfigure(master, x, weight=1)
        for y in range(6):
            Grid.rowconfigure(master, y, weight=1)


