__author__ = "jacksonsr45@gmail.com"

import tkinter
from app.src.app_calculator import Calculator

class Main:
    def __init__(self):
        root = tkinter.Tk()
        Calculator(root)
        root.mainloop()