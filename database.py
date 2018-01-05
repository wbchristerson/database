from tkinter import *

class Application(Frame):
    """ Main page for database """
    """ Object-oriented design based on Michael Dawson's Python Programming
        For The Absolute Beginner """
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.set_buttons()

    def set_buttons(self):
        """ Create text introduction """
        lbl = Label(self, text = "Welcome!")
        lbl.grid()

        self.bttn1 = Button(self, text = "Look Up An Entry")
        self.bttn1.grid()

        self.bttn2 = Button(self, text = "Browse Entries")
        self.bttn2.grid()

        self.bttn3 = Button(self)
        self.bttn3.grid()
        self.bttn3.configure(text = "Add An Entry")

        self.bttn4 = Button(self)
        self.bttn4.grid()
        self.bttn4["text"] = "Edit An Entry"

# main
root = Tk()
root.title("Database")
root.geometry("200x150")
app = Application(root)
root.mainloop()
