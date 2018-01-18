# Inspiration for project:
# https://artofproblemsolving.com/community/u53544h1559064p9530694
from tkinter import *
import json

# Credit for multi-page structure skeleton:
# https://pythonprogramming.net/change-show-new-frame-tkinter/

class Transition(Tk):
    def __init__(self):
        Tk.__init__(self)
        container = Frame(self)

        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.title("Database")
        self.geometry("350x620")
        self.frames = {}

        for F in (Home, SearchPage, BrowsePage, WritePage, EditPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Home)        

    def show_frame(self, cont):
        frame = self.frames[cont]
        if not (cont == Home):
            frame.clear()
        frame.tkraise()


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
        lbl.pack(pady=10,padx=10)
        lbl.grid(row=0,column=1)
        self.set_format(controller)


    def set_format(self, controller):
        """ Create menu buttons """
        self.bttn1 = Button(self, text = "Look Up An Entry",
                            command=lambda: controller.show_frame(SearchPage))
        self.bttn1.grid(row=1,column=1, pady=10)
        self.bttn1.grid_rowconfigure(1, weight=1)
        self.bttn1.config(bg="#4bc423", activebackground="#4bc423")

        self.bttn2 = Button(self, text = "Browse Entries",
                            command=lambda: controller.show_frame(BrowsePage))
        self.bttn2.grid(row=2,column=1, pady=10)
        self.bttn2.config(bg="#74eef2", activebackground="#74eef2")

        self.bttn3 = Button(self,
                            command=lambda: controller.show_frame(WritePage))
        self.bttn3.grid(row=3,column=1, pady=10)
        self.bttn3.configure(text = "Add An Entry")
        self.bttn3.config(bg="#e53c12", activebackground="#e53c12")

        self.bttn4 = Button(self,
                            command=lambda: controller.show_frame(EditPage))
        self.bttn4.grid(row=4,column=1, pady=10)
        self.bttn4["text"] = "Edit An Entry"
        self.bttn4.config(bg="#e6ef64", activebackground="#e6ef64")


class SearchPage(Frame):
    """ Search for entries based on various pieces of information """
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
        query_options = ['Tags', 'Mentioned Words', 'Topic', 'ID', 'Source']
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

        # Expanded view check button
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

    # clear the entry and text boxes of any data from previous uses
    def clear(self):
        self.inputs.delete(0, END)
        self.results_txt.delete(0.0, END)
        self.expanded_view.set(False)
        self.query_type.set(None)
        


class BrowsePage(Frame):
    """ See a full list of database items in either of a concise or expanded
        view """
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.grid()
        self.set_format(controller)

    def set_format(self, controller):
        # Page title
        lbl = Label(self, text = "Browse Page", font= ("Verdana", 12))
        lbl.grid(column = 1, sticky = W)

        # Menu return button
        self.bttn1 = Button(self, text = "Return To Menu",
                            command=lambda: controller.show_frame(Home))
        self.bttn1.grid(row = 1,column = 1, sticky = W)

        # Expanded view check button
        self.expanded_view = BooleanVar()
        Checkbutton(self,
                    text = "expanded view",
                    variable = self.expanded_view
                    ).grid(row = 2, column = 0, sticky = W)

        # Entry appearance button
        self.bttn2 = Button(self, text = "Browse",
                            command=lambda: self.populate_browser())
        self.bttn2.grid(row = 3, column = 0, sticky = W)

        # 'Items' label
        Label(self, text = "Items").grid(row = 4, column = 1, sticky = W)

        # Items text box
        self.results_txt = Text(self, width = 35, height = 25, wrap = WORD)
        self.results_txt.grid(row = 5, column = 0, columnspan = 3)

    def display(self, tags_lines, topics_lines):
        message = ""
        with open('resources.json', 'r') as f:
            ref_dict = json.load(f)
        
        for i in range(len(ref_dict['tags'])):
            message += 'ID: ' + str(i) + '\n'
            message += 'Topic: ' + ref_dict['topics'][i] + '\n'
            tags = ', '.join(ref_dict['tags'][i].split('#'))
            if (len(tags) > 0):
                tags = tags[2:]
            message += 'Tags: ' + tags + '\n'

        f.close()
        return message

    def populate_browser(self):
        tags_file = open("tags.txt", "r")
        topics_file = open("topics.txt", "r")
        tags_lines = tags_file.readlines()
        topics_lines = topics_file.readlines()

        # assume that tags_lines and topics_lines have the same length
        self.results_txt.delete(0.0, END)
        message = self.display(tags_lines, topics_lines)
        self.results_txt.insert(0.0, message)        
        
        tags_file.close()
        topics_file.close()

    def clear(self):
        self.expanded_view.set(False)
        self.results_txt.delete(0.0, END)


class WritePage(Frame):
    """ Add a database entry """
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.grid()
        self.set_intro(controller)
        self.set_format(controller, 2)
        
        # 'Add Entry' button
        self.bttn2 = Button(self, text = "Add Entry",
                            command=lambda: self.save_inputs())
        self.bttn2.grid(row = 13, column = 1)

        # 'Cancel' button
        self.bttn3 = Button(self, text = "Cancel",
                            command=lambda: controller.show_frame(Home))
        self.bttn3.grid(row = 13, column = 2)

    def set_intro(self, controller):
        # Page title
        lbl = Label(self, text = "Write Page", font= ("Verdana", 12))
        lbl.grid(row = 0, column = 1)
        
        # Menu return button
        self.bttn1 = Button(self, text = "Return To Menu",
                            command=lambda: controller.show_frame(Home))
        self.bttn1.grid(row = 1, column = 1)

    def set_format(self, controller, offset):
        # 'Tags' label
        Label(self, text = "Tags").grid(row = offset, column = 0, sticky = W)

        # Tags input entry
        self.tags_input = Entry(self)
        self.tags_input.grid(row = offset, column = 1, sticky = W)

        # 'Topic' label
        Label(self, text = "Topic").grid(row = 1 + offset,
                                         column = 0, sticky = W)

        # Topic input entry
        self.topic_input = Entry(self)
        self.topic_input.grid(row = 1 + offset, column = 1, sticky = W)

        # 'Source' label
        Label(self, text = "Source").grid(row = 2 + offset,
                                          column = 0, sticky = W)

        # Source input entry
        self.source_input = Entry(self)
        self.source_input.grid(row = 2 + offset, column = 1, sticky = W)

        # 'Statement' label
        Label(self, text = "Statement").grid(row = 3 + offset,
                                             column = 0, sticky = W)

        # Statement text box
        self.statement_txt = Text(self, width = 30, height = 5, wrap = WORD)
        self.statement_txt.grid(row = 4 + offset, column = 0, columnspan = 3)

        # 'Solution' (without latex) label
        Label(self, text = "Solution (no latex)").grid(row = 5 + offset,
                                                       column = 0, sticky = W)

        # Solution without latex text box
        self.solution_no_latex_txt = Text(self, width = 30, height = 5,
                                          wrap = WORD)
        self.solution_no_latex_txt.grid(row = 6 + offset,
                                        column = 0, columnspan = 3)

        # 'Solution' (with latex) label
        Label(self, text = "Solution (with latex)").grid(row = 7 + offset,
                                                         column = 0, sticky = W)

        # Solution with latex text box
        self.solution_latex_txt = Text(self, width = 30, height = 5,
                                          wrap = WORD)
        self.solution_latex_txt.grid(row = 8 + offset,
                                     column = 0, columnspan = 3)

        # 'Notes' label
        Label(self, text = "Notes").grid(row = 9 + offset,
                                         column = 0, sticky = W)

        # Notes text box
        self.notes_txt = Text(self, width = 30, height = 5,
                                          wrap = WORD)
        self.notes_txt.grid(row = 10 + offset, column = 0, columnspan = 3)

    # clear write page of inputs
    def clear(self):
        self.tags_input.delete(0, END)
        self.topic_input.delete(0, END)
        self.source_input.delete(0, END)
        self.statement_txt.delete(0.0, END)
        self.solution_no_latex_txt.delete(0.0, END)
        self.solution_latex_txt.delete(0.0, END)
        self.notes_txt.delete(0.0, END)

    # given the tags listed with commas and possibly spaces, place pound signs
    # between tags
    def tagify(self, tags):
        tag_arr = tags.split(',')
        for i in range(len(tag_arr)):
            if ((len(tag_arr[i]) > 0) and (tag_arr[i][0] == ' ')):
                tag_arr[i] = tag_arr[i][1:]
        ans = '#'.join(tag_arr)
        if (len(ans) > 0):
            ans = '#' + ans
        return ans
            
            
    # s = {'tags': tag, 'topics': topic, 'sources': source,
    #      'statements': statement, 'sol_no_latex': sol_no_late,
    #      'sol_latex': sol_late, 'notes': note}

    def save_inputs(self):
        with open('resources.json', 'r') as f:
            ref_dict = json.load(f)
        ref_dict['tags'].append(self.tagify(self.tags_input.get()))
        ref_dict['topics'].append(self.topic_input.get())
        ref_dict['sources'].append(self.source_input.get())
        ref_dict['statements'].append(self.statement_txt.get("1.0", END))
        sol_str = self.solution_no_latex_txt.get("1.0", END)
        ref_dict['sol_no_latex'].append(sol_str)
        ref_dict['sol_latex'].append(self.solution_latex_txt.get("1.0", END))
        ref_dict['notes'].append(self.notes_txt.get("1.0", END))
        
        #print('Hello ' + str(len(ref_dict['tags'])))
        f.close()

        with open('resources.json', 'w') as g:
            json.dump(ref_dict, g)
        g.close()


class EditPage(Frame):
    """ Edit an entry based on the ID """
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.grid()
        self.set_format(controller)

    def set_format(self, controller):
        # Page title
        lbl = Label(self, text = "Edit Page", font= ("Verdana", 12))
        lbl.grid(row = 0, column = 1)
        
        # Menu return button
        self.bttn1 = Button(self, text = "Return To Menu",
                            command=lambda: controller.show_frame(Home))
        self.bttn1.grid(row = 1,column = 1)

        # 'ID' label
        Label(self, text = "ID").grid(row = 2, column = 0, sticky = W)

        # ID input entry
        self.id_input = Entry(self)
        self.id_input.grid(row = 2, column = 1, sticky = W)

        # Entry display button
        self.bttn2 = Button(self, text = "Edit",
                            command=lambda: controller.show_frame(Home))
        self.bttn2.grid(row = 3,column = 1)

        # Set page format similarly to write page
        WritePage.set_format(self,controller, 4)

        # Save button
        self.bttn3 = Button(self, text = "Save",
                            command=lambda: controller.show_frame(Home))
        self.bttn3.grid(row = 15,column = 0)

        # Cancel button
        self.bttn4 = Button(self, text = "Cancel",
                            command=lambda: controller.show_frame(Home))
        self.bttn4.grid(row = 15,column = 1)

    def clear(self):
        self.id_input.delete(0, END)
        self.tags_input.delete(0, END)
        self.topic_input.delete(0, END)
        self.source_input.delete(0, END)
        self.statement_txt.delete(0.0, END)
        self.solution_no_latex_txt.delete(0.0, END)
        self.solution_latex_txt.delete(0.0, END)
        self.notes_txt.delete(0.0, END)
        


app = Transition()
app.mainloop()
