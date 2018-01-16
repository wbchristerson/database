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

        self.title("Database")
        self.geometry("300x550")
        self.frames = {}

        for F in (Home, SearchPage, WritePage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Home)        

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class Home(Frame):
    """ Main page for database """
    """ Object-oriented design based on Michael Dawson's Python Programming
        For The Absolute Beginner """
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.grid()
        
        lbl = Label(self, text = "Welcome!")
        lbl.pack(pady=10,padx=10)
        lbl.grid(row=0,column=1)
        self.set_format(controller)


    def set_format(self, controller):
        """ Create text introduction """

        self.bttn1 = Button(self, text = "Look Up An Entry",
                            command=lambda: controller.show_frame(SearchPage))
        self.bttn1.grid(row=1,column=1, pady=10)
        self.bttn1.grid_rowconfigure(1, weight=1)
        self.bttn1.config(bg="#4bc423", activebackground="#4bc423")

        self.bttn2 = Button(self, text = "Browse Entries",
                            command=lambda: controller.show_frame(BrowsePage))
        self.bttn2.grid(row=2,column=1, pady=10)

        self.bttn3 = Button(self,
                            command=lambda: controller.show_frame(WritePage))
        self.bttn3.grid(row=3,column=1, pady=10)
        self.bttn3.configure(text = "Add An Entry")
        self.bttn3.config(bg="#e53c12", activebackground="#e53c12")

        self.bttn4 = Button(self)
        self.bttn4.grid(row=4,column=1, pady=10)
        self.bttn4["text"] = "Edit An Entry"


class SearchPage(Frame):
    """ Object-oriented design based on Michael Dawson's Python Programming
        For The Absolute Beginner """
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.grid()
        self.set_format(controller)

    def set_format(self, controller):
        # Page title
        lbl = Label(self, text = "Search Page", font= ("Verdana", 12))
        lbl.grid(row = 0, column = 1)

        # Menu return button
        self.bttn1 = Button(self, text = "Return To Menu",
                            command=lambda: controller.show_frame(Home))
        self.bttn1.grid(row=1,column=1)

        # 'Match By' label
        Label(self, text = "Match By:").grid(row = 2, column = 0, sticky = W)

        # Radio Button
        self.query_type = StringVar()
        self.query_type.set(None)
        query_options = ['Tags', 'Mentioned Words', 'Topic']
        column = 0
        for query in query_options:
            Radiobutton(self,
                        text = query,
                        variable = self.query_type,
                        value = query
                        ).grid(row = 3, column = column, sticky = W)
            column += 1

        # 'Inputs' entry label
        Label(self, text = "Inputs").grid(row = 4, column = 0, sticky = W)

        # Input entry
        self.inputs = Entry(self)
        self.inputs.grid(row = 4, column = 1, sticky = W)

        # Expanded view option
        self.expanded_view = BooleanVar()
        Checkbutton(self,
                    text = "expanded view",
                    variable = self.expanded_view
                    ).grid(row = 5, column = 1, sticky = W)

        # Button to list items
        self.bttn2 = Button(self, text = "List Items",
                            command = self.get_items)
        self.bttn2.grid(row = 6, column = 1)

        # 'Items' label
        Label(self, text = "Items").grid(row = 7, column = 0, sticky = W)

        # Items text box
        self.results_txt = Text(self, width = 30, height = 5, wrap = WORD)
        self.results_txt.grid(row = 8, column = 0, columnspan = 3)
        

    def get_items(self):
        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, 'hello')


class WritePage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.grid()
        lbl = Label(self, text = "Write Page", font= ("Verdana", 12))
        lbl.grid(row = 0, column = 1)
        self.set_format(controller)

    def set_format(self, controller):
        # Menu return button
        self.bttn1 = Button(self, text = "Return To Menu",
                            command=lambda: controller.show_frame(Home))
        self.bttn1.grid(row = 1,column = 1)

        # 'Tags' label
        Label(self, text = "Tags").grid(row = 2, column = 0, sticky = W)

        # Tags input entry
        self.tags_input = Entry(self)
        self.tags_input.grid(row = 2, column = 1, sticky = W)

        # 'Topic' label
        Label(self, text = "Topic").grid(row = 3, column = 0, sticky = W)

        # Topic input entry
        self.topic_input = Entry(self)
        self.topic_input.grid(row = 3, column = 1, sticky = W)

        # 'Statement' label
        Label(self, text = "Statement").grid(row = 4, column = 0, sticky = W)

        # Statement text box
        self.statement_txt = Text(self, width = 30, height = 5, wrap = WORD)
        self.statement_txt.grid(row = 5, column = 0, columnspan = 3)

        # 'Solution' (without latex) label
        Label(self, text = "Solution (no latex)").grid(row = 6,
                                                       column = 0, sticky = W)

        # Solution without latex text box
        self.solution_no_latex_txt = Text(self, width = 30, height = 5,
                                          wrap = WORD)
        self.solution_no_latex_txt.grid(row = 7, column = 0, columnspan = 3)

        # 'Solution' (with latex) label
        Label(self, text = "Solution (with latex)").grid(row = 8,
                                                         column = 0, sticky = W)

        # Solution with latex text box
        self.solution_latex_txt = Text(self, width = 30, height = 5,
                                          wrap = WORD)
        self.solution_latex_txt.grid(row = 9, column = 0, columnspan = 3)

        # 'Notes' label
        Label(self, text = "Notes").grid(row = 10, column = 0, sticky = W)

        # Notes text box
        self.notes_txt = Text(self, width = 30, height = 5,
                                          wrap = WORD)
        self.notes_txt.grid(row = 11, column = 0, columnspan = 3)

        # 'Add Entry' button
        self.bttn2 = Button(self, text = "Add Entry",
                            command=lambda: controller.show_frame(Home))
        self.bttn2.grid(row = 12,column = 1)
        

class BrowsePage(Frame):
    """ Object-oriented design based on Michael Dawson's Python Programming
        For The Absolute Beginner """
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.grid()
        self.set_format(controller)

    def set_format(self, controller):
        # Page title
        lbl = Label(self, text = "Search Page", font= ("Verdana", 12))
        lbl.grid(column = 1)

        
    

app = Transition()
app.mainloop()
