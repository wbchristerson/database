# https://artofproblemsolving.com/community/u53544h1559064p9530694
from tkinter import *

class Transition(Tk):
    def __init__(self):
        Tk.__init__(self)
        container = Frame(self)

        # Structure to be possibly removed
        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        # Structure to be possibly removed

        self.title("Database")
        self.geometry("200x200")
        self.frames = {}

        for F in (Application, WritePage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        #self.frames[Application] = Application(self, container)
        #self.frame[Application] = Application(container, self)
        #self.frames[WritePage] = WritePage(self, container)
        #self.frame[WritePage] = WritePage(container, self)

        self.show_frame(Application)
        

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

# https://pythonprogramming.net/change-show-new-frame-tkinter/

class Application(Frame):
    """ Main page for database """
    """ Object-oriented design based on Michael Dawson's Python Programming
        For The Absolute Beginner """
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.grid()
        lbl = Label(self, text = "Welcome!")
        lbl.grid()
        self.set_buttons(controller)

    def set_buttons(self, controller):
        """ Create text introduction """
        lbl = Label(self, text = "Welcome!")
        lbl.grid()

        self.bttn1 = Button(self, text = "Look Up An Entry",
                            command=lambda: controller.show_frame(WritePage))
        self.bttn1.grid()

        self.bttn2 = Button(self, text = "Browse Entries")
        self.bttn2.grid()

        self.bttn3 = Button(self)
        self.bttn3.grid()
        self.bttn3.configure(text = "Add An Entry")

        self.bttn4 = Button(self)
        self.bttn4.grid()
        self.bttn4["text"] = "Edit An Entry"


class WritePage(Frame):
    """ Main page for database """
    """ Object-oriented design based on Michael Dawson's Python Programming
        For The Absolute Beginner """
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        #self.grid()
        #lbl = Label(self, text = "Bienvenidos!")
        #lbl.grid()
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
