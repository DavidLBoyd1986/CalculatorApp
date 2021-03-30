from GraphicalInterface import *
import tkinter as tk


def run_app():
    """Function that launches the application"""

    # root is an instance of the Tk class (Main window)
    root = tk.Tk()

    # Create instance of Calculator class that uses the tk instance
    calculator_app = Calculator(root)

    # This starts the event loop of the GUI which opens the window.\
    calculator_app.mainloop()


if __name__ == '__main__':
    run_app()
