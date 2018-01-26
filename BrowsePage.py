from tkinter import *
import DataEntry as DE
import json

class BrowsePage(Frame):
    """ See a full list of database items in either of a concise or expanded
        view """
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.grid_columnconfigure(0, weight=2)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=2)
        self.config(bg="#74eef2")
        self.grid()
        self.set_format(controller)
        self.executed = False # whether the user has clicked browse at all

    def set_format(self, controller):
        # Page title
        lbl = Label(self, text = "Browse Entries", font= ("Verdana", 14),
                    bg="#74eef2")
        lbl.grid(column = 1, pady = 10)

        # Menu return button
        self.bttn1 = Button(self, text = "Return To Menu", width = 15,
                            command=lambda: controller.return_home(),
                            font = ("Verdana", 11))
        self.bttn1.grid(row = 1,column = 1)

        # Expanded view check button -- 'expanded view' includes the problem
        # statements
        self.expanded_view = BooleanVar()
        Checkbutton(self,
                    text = "Expanded view",
                    variable = self.expanded_view,
                    # allow toggling of expanded view within the frame
                    command = self.update_view,
                    bg="#74eef2",
                    activebackground="#74eef2",
                    font = ("Verdana", 11)
                    ).grid(row = 2, column = 0, pady = 10)

        # Entry appearance button
        self.bttn2 = Button(self, text = "Browse", font = ("Verdana", 11),
                            command=lambda: self.populate_browser(), width = 15)
        self.bttn2.grid(row = 2, column = 2, padx = 20)

        # 'Items' label
        #Label(self, text = "Results", bg="#74eef2",
        #      font = ("Verdana", 11)).grid(row = 4, column = 1)

        # Items text box
        self.results_txt = Text(self, width = 60, height = 35, wrap = WORD,
                                font= ("Verdana", 9))
        self.results_txt.grid(row = 4, column = 0, columnspan = 3, padx=20,
                              pady=20)

    def display(self):
        message = ""
        with open('resources.json', 'r') as f:
            ref_dict = json.load(f)
        ref = [DE.DataEntry.from_dict(entry) for entry in ref_dict]

        for i in range(len(ref)):
            message += ref[i].browse_rep(self.expanded_view.get())
            message += '\n\n\n'

        f.close()
        return message

    def populate_browser(self):
        # assume that all dictionary entries have the same length
        self.results_txt.delete(0.0, END)
        message = self.display()
        self.results_txt.insert(0.0, message)
        self.executed = True # mark as having used browsing button

    def update_view(self):
        if (self.executed):
            self.populate_browser()

    def clear(self):
        self.expanded_view.set(False)
        self.results_txt.delete(0.0, END)
        self.executed = False
