import tkinter as tk
import numpy as np
import functools

class grid(tk.Frame):
    def __init__(
        self, numberx, numbery=None, parent=None, text = None, xoffset = 0, yoffset = 0,
        command = None, widget = tk.Checkbutton, **kwargs
    ):
        tk.Frame.__init__(self, parent)
        self.xoffset = xoffset
        self.yoffset = yoffset
        self.text = text
        self.boxlist, self.varlist = [], []
        self.numberx, self.numbery = numberx, numbery
        self.xgrid, self.ygrid = 0, 0

        self.coordrost = [[i for i in range(self.numberx*x,self.numberx+self.numberx*x)] for x in range(numbery)]

        i = 0
        while True:
            self.varlist.append(tk.BooleanVar())
            if type(widget) == tk.Checkbutton:
                self.boxlist.append(widget(
                    self,
                    text=self.text,
                    variable=self.varlist[i],
                    command = command,
                    highlightthickness=0,
                )
                )
            else:
                kwargs['variable'] = variable=self.varlist[i]
                self.boxlist.append(widget(self, **kwargs))
            row, col = self.ygrid+self.yoffset, self.xgrid + self.xoffset
            self.boxlist[i].grid(row=row, sticky=tk.W, column=col)
            self.boxlist[i].configure(bg='light gray')
            self.xgrid += 1
            if self.xgrid == self.numberx:
                self.ygrid += 1
                self.xgrid = 0

            if self.ygrid == self.numbery:
                break
            i += 1


    def coords(self, x, y=None):
        if type(x) == tuple or type(x) == list:
            x, y = x[0], x[1]
        elif not y:
            print('Please enter a y')
            return
        return self.coordrost[self.numbery-y][x-1]

    def uncoords(self, coord):
        for i in range(len(self.coordrost)):
            if coord in self.coordrost[i]:
                x1 = self.coordrost[i].index(coord) + 1
                y1 = self.numbery - i
                return [x1, y1]

    def var_2d(self, get=True):

        l = [i.get() for i in self.varlist] if get else self.varlist
        l = [l[i:i+self.numberx] for i in range(0, len(l), self.numberx)]

        return l


if __name__ == "__main__":
    def hey():
        print('hey')
    root = tk.Tk()
    grid1 = grid(2,2,root,command=hey)
    grid1.grid()
    grid1.var_2d()
    root.mainloop()
