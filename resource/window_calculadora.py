__author__ = 'jacksonsr45@gmail.com'

import tkinter
from data.calculadora import __calc__

class Calculadora(__calc__):
    def __init__(self, root):
        super().__init__()

        root = root
        root.geometry("550x600")
        root.title("Calculadora")
        
        self._Frame_Calc_(root, tkinter.TOP)
        self._display_(root)
        self._clearBut_(root)
        self._calculadora_(root)
        self._equals_(root)