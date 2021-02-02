from tkinter import *
from tkinter import ttk


class calculator:
    def getInput(self):
        self.userInput = self.entry.get()
    def clearInput(self):
        self.entry.delete(0, END)  
    def buttonPress(self, argv):
        self.entry.insert(END, argv)   
    def evaluate(self):
        self.getInput()
        try:
            self.result = eval(self.userInput)
        except ZeroDivisionError:
            self.entry.delete(0, END)
            self.entry.insert(0, "Not a number")
        except SyntaxError:
            self.entry.delete(0, END)
            self.entry.insert(0, "Input error")
        else:
            self.entry.delete(0, END)
            self.entry.insert(0, self.result)  
    def __init__(self, nui):        
        nui.title("Kalkulator")
        self.entry = Entry(nui, fg = "black")
        self.entry.grid(row = 0, column = 0, columnspan = 4)        
        bAC = Button(nui, text = "AC", width =14, height = 2, fg = "black",
        command = lambda: self.clearInput())
        bAC.grid(row = 1, column = 0, columnspan = 3)
        bDiv = Button(nui, text = "/", width = 5, height = 5, fg = "black",
        command = lambda: self.buttonPress("/"))
        bDiv.grid(row = 1, column = 3)
        b7 = Button(nui, text = "7", width = 6, height = 5, fg = "black",
        command = lambda: self.buttonPress("7"))
        b7.grid(row = 2, column = 0)
        b8 = Button(nui, text = "8", width = 6, height = 5, fg = "black",
        command = lambda: self.buttonPress("8"))
        b8.grid(row = 2, column = 1)
        b9 = Button(nui, text = "9", width = 6, height = 5, fg = "black",
        command = lambda: self.buttonPress("9"))
        b9.grid(row = 2, column = 2)
        bMult = Button(nui, text = "*", width = 6, height = 5, fg = "black",
        command = lambda: self.buttonPress("*"))
        bMult.grid(row = 2, column = 3)
        b4 = Button(nui, text = "4", width = 6, height = 5, fg = "black",
        command = lambda: self.buttonPress("4"))
        b4.grid(row = 3, column = 0)
        b5 = Button(nui, text = "5", width = 6, height = 5, fg = "black",
        command = lambda: self.buttonPress("5"))
        b5.grid(row = 3, column = 1)
        b6 = Button(nui, text = "6", width = 6, height = 5, fg = "black",
        command = lambda: self.buttonPress("6"))
        b6.grid(row = 3, column = 2)
        bSub = Button(nui, text = "-", width = 6, height = 5, fg = "black",
        command = lambda: self.buttonPress("-"))
        bSub.grid(row = 3, column = 3)
        b1 = Button(nui, text = "1", width = 6, height = 5, fg = "black",
        command = lambda: self.buttonPress("1"))
        b1.grid(row = 4, column = 0)
        b2 = Button(nui, text = "2", width = 6, height = 5, fg = "black",
        command = lambda: self.buttonPress("2"))
        b2.grid(row = 4, column = 1)
        b3 = Button(nui, text = "3", width = 6, height = 5, fg = "black",
        command = lambda: self.buttonPress("3"))
        b3.grid(row = 4, column = 2)
        bAdd = Button(nui, text = "+", width = 6, height = 5, fg = "black",
        command = lambda: self.buttonPress("+"))
        bAdd.grid(row = 4, column = 3)
        b0 = Button(nui, text = "0", width = 13, height = 5, fg = "black",
        command = lambda: self.buttonPress("0"))
        b0.grid(row = 5, column = 0, columnspan = 2)
        bDot = Button(nui, text = ".", width = 6, height = 5, fg = "black",
        command = lambda: self.buttonPress("."))
        bDot.grid(row = 5, column = 2)
        bEquals = Button(nui, text = "=", width = 6, height = 5, fg = "black",
        command = lambda: self.evaluate())
        bEquals.grid(row = 5, column = 3)
       
        






root = Tk()
root.geometry("240x444")




calculator(root)
root.mainloop()