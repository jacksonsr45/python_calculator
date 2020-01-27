__author__ = 'jacksonsr45@gmail.com'

import tkinter

class __calc__(object):
    def __init__(self):
        self.font = ("Ubunto", 20)
        self.font_display = ("Ubunto", 40)
        self.__display__ = tkinter.StringVar()


    def _Frame_Calc_(self, frame, side):
        __storeObj__ = tkinter.Frame(frame, borderwidth= 1, bd = 4, bg="black")
        __storeObj__.pack(side= side, expand=tkinter.YES, fill= tkinter.BOTH)
        return __storeObj__

    def _calculadora_(self, frame):
        for __NumBut__ in ("()%","/789", "*456", "-123", "+.0"):
            __FunctionNum__ = self._Frame_Calc_( frame, tkinter.TOP)
            for __iEquals__ in __NumBut__:
                self.Button(__FunctionNum__, tkinter.LEFT, __iEquals__,
                            lambda __storeObj__= self.__display__, q=__iEquals__: __storeObj__.set(__storeObj__.get() + q))
            
    def _display_(self, frame):
        __display_entry__ = tkinter.Entry(frame)
        __display_entry__.configure(textvariable=self.__display__)
        __display_entry__.configure(font=self.font_display)
        __display_entry__.configure(justify='right')
        __display_entry__.pack(side=tkinter.TOP, expand= tkinter.YES, fill= tkinter.BOTH)
        return __display_entry__

    def _clearBut_(self, frame):
        for __clearBut__ in (["CE"],["C"]):
            __erase__ = self._Frame_Calc_( frame, tkinter.TOP)
            for __ichar__ in __clearBut__:
                self.__Button__(__erase__, tkinter.LEFT, __ichar__,
                            lambda storeObj=self.__display__, q=__ichar__: storeObj.set(''))

    def _equals_(self, frame):
        __EqualsButton__ = self._Frame_Calc_( frame, tkinter.TOP)
        for __iEquals__ in "=":
            if __iEquals__ == '=':
                __btniEquals__ = self.__Button__(__EqualsButton__, tkinter.LEFT, __iEquals__)
                __btniEquals__.bind('<ButtonRelease-1>',
                        lambda e, s=self, storeObj=self.__display__: s.calc(storeObj), '+')
            else:
                __btniEquals__ = self.__Button__(__EqualsButton__, tkinter.LEFT, __iEquals__,
                        lambda storeObj=self.__display__, s=' %s '%__iEquals__: storeObj.set(storeObj.get()+s))

    def calc(self, display):
        try: 
            display.set(eval(display.get()))
        except:
            display.set("ERROR")

    def __Button__(self, frame, side, text, command=None):
        __objButton__ = tkinter.Button(frame)
        __objButton__.configure(text= text)
        __objButton__.configure(font= self.font)
        __objButton__.configure(command=command)
        __objButton__.pack( side=side, expand=tkinter.YES, fill=tkinter.BOTH)
        return __objButton__ 