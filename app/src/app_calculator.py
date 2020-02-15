__author__ = "jacksonsr45@gmail.com"

import tkinter

class Calculator:
    def __init__(self,root):
        self.root = root
        self.root.title("Calculator")
        x = (self.root.winfo_screenwidth() // 2) - (550 // 2)
        y = (self.root.winfo_screenheight() // 2) - (600 // 2)
        self.root.geometry("550x600+{}+{}".format( x, y))

        self.value_display = tkinter.StringVar()

        self.frame = self.frame_calc(self.root, tkinter.TOP, 1, 4, "black")

        self.display(self.frame, ("Ubunto", 17))

        self.clear(self.root)

        self.button_calculator(self.root)

        self.equals(self.root)


    def frame_calc(self, root, side, bw, bd, bg):
        frame = tkinter.Frame(root, borderwidth= bw, bd= bw, bg= bg)
        frame.pack(side= side, expand=tkinter.YES, fill= tkinter.BOTH)
        return frame


    def display(self, frame, font):
        display = tkinter.Entry(frame)
        display.configure(textvariable=self.value_display)
        display.configure(font=font)
        display.configure(justify='right')
        display.pack(side=tkinter.TOP, expand= tkinter.YES, fill= tkinter.BOTH)
        return display


    def button(self, frame, side, text, command=None):
        button = tkinter.Button(frame)
        button.configure(text= text)
        button.configure(font= ("Ubunto", 14))
        button.configure(command=command)
        button.pack( side=side, expand=tkinter.YES, fill=tkinter.BOTH)
        return button 


    def clear(self, root):
        for clear in (["CE"],["C"]):
            erase = self.frame_calc( root, tkinter.TOP, 1, 4, "white")
            for row in clear:
                self.button( erase, tkinter.LEFT, row,
                            lambda storeObj=self.value_display, q= row: 
                                        storeObj.set(''))

    def button_calculator(self, root):
        for num_btn in ("()%","/789", "*456", "-123", "+.0"):
            btn_calc = self.frame_calc( root, tkinter.TOP, 1, 4, "white")
            for row in num_btn:
                self.button( btn_calc, tkinter.LEFT, row,
                            lambda display= self.value_display, q=row: 
                                    display.set(display.get() + q))



    def equals(self, root):
        equals_button = self.frame_calc( root, tkinter.TOP, 1, 4, "white")
        for value in "=":
            if value == '=':
                btn_equals = self.button( equals_button, tkinter.LEFT, value)
                btn_equals.bind('<ButtonRelease-1>',
                        lambda e, s=self, display=self.value_display: s.calc(display), '+')
            else:
                btn_equals = self.button( equals_button, tkinter.LEFT, value,
                        lambda display=self.value_display, s=' %s '%value: 
                                display.set(display.get()+s))

    def calc(self, display):
        try: 
            display.set(eval(display.get()))
        except:
            display.set("ERROR")