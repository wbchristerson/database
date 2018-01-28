from tkinter import *
import DataEntry as DE
import SearchPage as SP
import BrowsePage as BP
import WritePage as WP
import EditPage as EP
import json

# Credit for rudimentary multi-page structure skeleton:
# https://pythonprogramming.net/change-show-new-frame-tkinter/

class Transition(Tk):
    def __init__(self):
        Tk.__init__(self)

        container = Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.title("Database")
        self.geometry("580x690")
        self.frames = {}

        for F in (Home, SP.SearchPage, BP.BrowsePage, WP.WritePage,
                  EP.EditPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Home)        


    def show_frame(self, cont):
        frame = self.frames[cont]
        if not (cont == Home):
            frame.clear()
        if ((cont == WP.WritePage) or (cont == EP.EditPage)):
            # make screen wider for Write Page
            self.geometry("680x690")
        else:
            # reset screen to narrow view when not in Write Page
            self.geometry("580x690")
        frame.tkraise()


    def return_home(self):
        # reset screen to narrow view when returning to Menu
        self.geometry("580x690")
        self.frames[Home].tkraise()



class Home(Frame):
    """ Main page for database """
    """ Object-oriented design based on Michael Dawson's Python Programming
        For The Absolute Beginner """
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=3)
        self.grid()
        
        lbl = Label(self, text = "Welcome!", font=("Verdana", 24))
        lbl.grid(row=0,column=0)
        self.set_format(controller)


    def set_format(self, controller):
        """ Create menu buttons """
        self.bttn1 = Button(self, text = "Look Up An Entry", fg="white",
                            width = 15, height = 2, font=("Verdana", 14),
                            command=lambda: controller.show_frame(SP.SearchPage))
        self.bttn1.grid(row=1,column=0)
        self.bttn1.config(bg="#33e058", activebackground="#4bc423")
        
        self.bttn2 = Button(self, text = "Browse Entries", fg = "white",
                            width = 15, height = 2, font=("Verdana", 14),
                            command=lambda: controller.show_frame(BP.BrowsePage))
        self.bttn2.grid(row=2,column=0, pady=10)
        self.bttn2.config(bg="#329de0", activebackground="#74eef2")

        self.bttn3 = Button(self, fg = "white",
                            width = 15, height = 2, font=("Verdana", 14),
                            command=lambda: controller.show_frame(WP.WritePage))
        self.bttn3.grid(row=3,column=0, pady=10)
        self.bttn3.configure(text = "Add An Entry")
        self.bttn3.config(bg="#e54242", activebackground="#e53c12")

        self.bttn4 = Button(self, fg="white",
                            width = 15, height = 2, font=("Verdana", 14),
                            command=lambda: controller.show_frame(EP.EditPage))
        self.bttn4.grid(row=4,column=0, pady=10)
        self.bttn4["text"] = "Edit An Entry"
        self.bttn4.config(bg="#e0da32", activebackground="#e6ef64")



app = Transition()
app.mainloop()
