# Inspiration for project:
# https://artofproblemsolving.com/community/u53544h1559064p9530694
from tkinter import *
import DataEntry as DE
import SearchPage as SP
import BrowsePage as BP
import WritePage as WP
import EditPage as EP
import json

# Credit for multi-page structure skeleton:
# https://pythonprogramming.net/change-show-new-frame-tkinter/


# s = {'tags': tag, 'topics': topic, 'sources': source,
#      'statements': statement, 'sol_no_latex': sol_no_late,
#      'sol_latex': sol_late, 'notes': note}

# Note: do not include '#' in tag entries


class Transition(Tk):
    def __init__(self):
        Tk.__init__(self)
        container = Frame(self)

        container.pack(side="top", fill="both", expand = True)
        #container.grid()
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.title("Database")
        self.geometry("540x690")
        self.frames = {}

        for F in (Home, SP.SearchPage, BP.BrowsePage, WP.WritePage,
                  EP.EditPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            #frame.grid(row=0, column=0)

        self.show_frame(Home)        

    def show_frame(self, cont):
        frame = self.frames[cont]
        if not (cont == Home):
            frame.clear()
        frame.tkraise()

    def return_home(self):
        self.frames[Home].tkraise()


class Home(Frame):
    """ Main page for database """
    """ Object-oriented design based on Michael Dawson's Python Programming
        For The Absolute Beginner """
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        # Add background color here
        # self.configure(background="#fbff8e")
        self.grid()
        
        lbl = Label(self, text = "Welcome!")
        lbl.grid(row=0,column=1)
        self.set_format(controller)


    def set_format(self, controller):
        """ Create menu buttons """
        self.bttn1 = Button(self, text = "Look Up An Entry",
                            command=lambda: controller.show_frame(SP.SearchPage))
        self.bttn1.grid(row=1,column=1, pady=10)
        self.bttn1.grid_rowconfigure(1, weight=1)
        self.bttn1.config(bg="#4bc423", activebackground="#4bc423")

        self.bttn2 = Button(self, text = "Browse Entries",
                            command=lambda: controller.show_frame(BP.BrowsePage))
        self.bttn2.grid(row=2,column=1, pady=10)
        self.bttn2.config(bg="#74eef2", activebackground="#74eef2")

        self.bttn3 = Button(self,
                            command=lambda: controller.show_frame(WP.WritePage))
        self.bttn3.grid(row=3,column=1, pady=10)
        self.bttn3.configure(text = "Add An Entry")
        #e53c12
        #fc5653
        #ff4921
        self.bttn3.config(bg="#e53c12", activebackground="#e53c12")

        self.bttn4 = Button(self,
                            command=lambda: controller.show_frame(EP.EditPage))
        self.bttn4.grid(row=4,column=1, pady=10)
        self.bttn4["text"] = "Edit An Entry"
        self.bttn4.config(bg="#e6ef64", activebackground="#e6ef64")


app = Transition()
app.mainloop()
