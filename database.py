from tkinter import *

root = Tk()

root.title("Database")
root.geometry("200x100")

app = Frame(root)
app.grid()

lbl = Label(app, text = "Welcome!")
lbl.grid()


bttn1 = Button(app, text = "Look Up An Entry")
bttn1.grid()

bttn2 = Button(app)
bttn2.grid()
bttn2.configure(text = "Add An Entry")


root.mainloop()
