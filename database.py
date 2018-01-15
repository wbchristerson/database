# https://artofproblemsolving.com/community/u53544h1559064p9530694
from tkinter import *

# Credit for multi-page structure skeleton to
# https://pythonprogramming.net/change-show-new-frame-tkinter/

class Transition(Tk):
    def __init__(self):
        Tk.__init__(self)
        container = Frame(self)

        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        #container.grid_columnconfigure(1, weight=1)

        # Added Weight
        #container.grid_columnconfigure(2, weight=1)
        # Added Weight

        self.title("Database")
        self.geometry("300x300")
        self.frames = {}

        for F in (Application, WritePage):
            frame = F(container, self)
            self.frames[F] = frame
            #frame.grid(row=0, column=0, sticky="nsew")
            #frame.grid(row=0, column=0, sticky="ew")
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Application)
        #self.show_frame(WritePage)
        

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class Application(Frame):
    """ Main page for database """
    """ Object-oriented design based on Michael Dawson's Python Programming
        For The Absolute Beginner """
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.grid()

        #spacer = Label(self, text = "       ")
        #spacer = Label(self, text="")
        #spacer.grid(row=1,column=0)
        #spacer.grid_columnconfigure(0, weight=1)
        
        lbl = Label(self, text = "Welcome!")
        lbl.pack(pady=10,padx=10)
        #lbl.grid(row=1,column=3)
        #lbl.grid_rowconfigure(0, weight=2)
        lbl.grid(row=1,column=1)
        #lbl.grid_columnconfigure(1, weight=1)
        self.set_buttons(controller)


    def set_buttons(self, controller):
        """ Create text introduction """

        self.bttn1 = Button(self, text = "Look Up An Entry",
                            command=lambda: controller.show_frame(WritePage))
        #self.bttn1.grid(row=2,column=3)
        self.bttn1.grid(row=2,column=1, pady=10)
        self.bttn1.grid_rowconfigure(2, weight=1)

        self.bttn2 = Button(self, text = "Browse Entries")
        #self.bttn2.grid(row=4,column=3)
        self.bttn2.grid(row=4,column=1, pady=10)

        self.bttn3 = Button(self)
        #self.bttn3.grid(row=6,column=3)
        self.bttn3.grid(row=6,column=1, pady=10)
        self.bttn3.configure(text = "Add An Entry")

        self.bttn4 = Button(self)
        #self.bttn4.grid(row=8,column=3)
        self.bttn4.grid(row=8,column=1, pady=10)
        self.bttn4["text"] = "Edit An Entry"


class WritePage(Frame):
    """ Main page for database """
    """ Object-oriented design based on Michael Dawson's Python Programming
        For The Absolute Beginner """
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.grid()
        lbl = Label(self, text = "Bienvenidos!")
        lbl.grid()

        
#    def __init__(self, master, controller):
#        super(WritePage, self).__init__(master)
#        self.grid()
#        self.set_buttons()

#    def set_buttons(self):
#        """ Create text introduction """
#        lbl = Label(self, text = "Write Page!")
#        lbl.grid()

#        self.bttn1 = Button(self, text = "Write In An Entry")
#        self.bttn1.grid()


# main

#root = Tk()
#root.title("Database")
#root.geometry("200x150")
#app = Application(root)
#root.mainloop()

app = Transition()
app.mainloop()
