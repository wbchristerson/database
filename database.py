# Inspiration for project:
# https://artofproblemsolving.com/community/u53544h1559064p9530694
from tkinter import *
import json

# Credit for multi-page structure skeleton:
# https://pythonprogramming.net/change-show-new-frame-tkinter/


# s = {'tags': tag, 'topics': topic, 'sources': source,
#      'statements': statement, 'sol_no_latex': sol_no_late,
#      'sol_latex': sol_late, 'notes': note}
    
class Transition(Tk):
    def __init__(self):
        Tk.__init__(self)
        container = Frame(self)

        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.title("Database")
        self.geometry("370x620")
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
        self.bttn2 = Button(self, text = "List Items", command = self.get_items)
        self.bttn2.grid(row = 6, column = 1)

        # 'Items' label
        Label(self, text = "Items").grid(row = 7, column = 0, sticky = W)

        # Items text box
        self.results_txt = Text(self, width = 30, height = 5, wrap = WORD)
        self.results_txt.grid(row = 8, column = 0, columnspan = 3)

    # inputs given with pound signs between entries
    def collect_tags(self, ref_dict, inputs):
        message = ""
        inputs = inputs.split('#')
        inputs = inputs[1:]
        if (len(inputs) == 1):
            for i in range(len(ref_dict['tags'])):
                if (inputs[0] in ref_dict['tags'][i].split('#')[1:]):
                    message += BrowsePage.display_entry(self, i, ref_dict)                        
        else:
            used_ids = {}
            for i in range(len(ref_dict['tags'])):
                tested = True
                for entry in inputs:
                    if not (entry in ref_dict['tags'][i].split('#')[1:]):
                        tested = False
                        break
                if (tested):
                    message += BrowsePage.display_entry(self, i, ref_dict)
                    used_ids[i] = True;
            for i in range(len(ref_dict['tags'])):
                if not (i in used_ids):
                    for entry in inputs:
                        if (entry in ref_dict['tags'][i].split('#')[1:]):
                            message += BrowsePage.display_entry(self,i,ref_dict)
                            break
        return message

# s = {'tags': tag, 'topics': topic, 'sources': source,
#      'statements': statement, 'sol_no_latex': sol_no_late,
#      'sol_latex': sol_late, 'notes': note}

    # list matching items
    def get_items(self):
        # ['Tags', 'Mentioned Words', 'Topic', 'ID', 'Source']
        inputs = self.inputs.get()
        if (inputs == ''):
            message = BrowsePage.display(self)
            self.results_txt.delete(0.0, END)
            self.results_txt.insert(0.0, message)
        else:
            message = ''
            with open('resources.json', 'r') as f:
                ref_dict = json.load(f)
            if (self.query_type.get() == 'Tags'):
                inputs = WritePage.tagify(self, inputs)
                message = SearchPage.collect_tags(self, ref_dict, inputs)
            elif (self.query_type.get() == 'Mentioned Words'):
                print('aisle')
            elif (self.query_type.get() == 'Topic'):
                print('aisle')
            elif (self.query_type.get() == 'ID'):
                print('aisle')
            elif (self.query_type.get() == 'Source'):
                print('aisle')
        
            f.close()

            if (message == ''):
                message = 'No matching entries'
            self.results_txt.delete(0.0, END)
            self.results_txt.insert(0.0, message)

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
        self.executed = False # whether the user has clicked browse at all

    def set_format(self, controller):
        # Page title
        lbl = Label(self, text = "Browse Page", font= ("Verdana", 12))
        lbl.grid(column = 1, sticky = W)

        # Menu return button
        self.bttn1 = Button(self, text = "Return To Menu",
                            command=lambda: controller.show_frame(Home))
        self.bttn1.grid(row = 1,column = 1, sticky = W)

        # Expanded view check button -- 'expanded view' includes the problem
        # statements
        self.expanded_view = BooleanVar()
        Checkbutton(self,
                    text = "expanded view",
                    variable = self.expanded_view,
                    # allow toggling of expanded view within the frame
                    command = self.update_view
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

    def detagify(self, tags_string):
        tags = ', '.join(tags_string.split('#'))
        if (len(tags) > 0):
            tags = tags[2:]
        return tags
    
    # structure format for display of entry in 'browse' section
    def display_entry(self, index, ref_dict):
        message = 'ID: ' + str(index) + '\n'
        message += 'Topic: ' + ref_dict['topics'][index] + '\n'
        tag_string = BrowsePage.detagify(self, ref_dict['tags'][index]) + '\n'
        message +='Tags: ' + tag_string
        if (self.expanded_view.get()):
            message += 'Statement: '
            message += ref_dict['statements'][index] + '\n'
        message += '\n'
        return message

    def display(self):
        message = ""
        with open('resources.json', 'r') as f:
            ref_dict = json.load(f)

        for i in range(len(ref_dict['tags'])):
            message += BrowsePage.display_entry(self, i, ref_dict)

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


class WritePage(Frame):
    """ Add a database entry """
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.grid()
        self.set_intro(controller)
        self.set_format(controller, 2)
        
        # 'Add Entry' button
        self.bttn2 = Button(self, text = "Add Entry",
                            command=lambda: self.save_inputs(controller))
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
        self.statement_txt.grid(row = 4 + offset, column = 0, columnspan = 3,
                                sticky = W)

        # 'Solution' (without latex) label
        Label(self, text = "Solution (no latex)").grid(row = 5 + offset,
                                                       column = 0, sticky = W)

        # Solution without latex text box
        self.solution_no_latex_txt = Text(self, width = 30, height = 5,
                                          wrap = WORD)
        self.solution_no_latex_txt.grid(row = 6 + offset,
                                        column = 0, columnspan = 3, sticky = W)

        # 'Solution' (with latex) label
        Label(self, text = "Solution (with latex)").grid(row = 7 + offset,
                                                         column = 0, sticky = W)

        # Solution with latex text box
        self.solution_latex_txt = Text(self, width = 30, height = 5,
                                          wrap = WORD)
        self.solution_latex_txt.grid(row = 8 + offset,
                                     column = 0, columnspan = 3, sticky = W)

        # 'Notes' label
        Label(self, text = "Notes").grid(row = 9 + offset,
                                         column = 0, sticky = W)

        # Notes text box
        self.notes_txt = Text(self, width = 30, height = 5,
                                          wrap = WORD)
        self.notes_txt.grid(row = 10 + offset, column = 0, columnspan = 3,
                            sticky = W)

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

    def save_inputs(self, controller):
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
        
        f.close()

        with open('resources.json', 'w') as g:
            json.dump(ref_dict, g)
        g.close()        
        controller.show_frame(Home)


class EditPage(Frame):
    """ Edit an entry based on the ID """
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.grid()
        self.set_format(controller)
        self.curr_id = -1

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
                            command=self.populate_by_id)
        self.bttn2.grid(row = 3,column = 1)

        # Set page format similarly to write page
        WritePage.set_format(self,controller, 4)

        # Save button
        self.bttn3 = Button(self, text = "Save",
                            command=lambda: self.update_entry(controller))
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
        if (hasattr(self, 'warning_lbl')):
            self.warning_lbl.grid_remove()
        self.curr_id = -1

    def check_for_int(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    def populate_by_id(self):
        if (hasattr(self, 'warning_lbl')):
            self.warning_lbl.grid_remove()
        rec_id = self.id_input.get()
        if (self.check_for_int(rec_id)):
            with open('resources.json', 'r') as f:
                ref_dict = json.load(f)
            int_id = int(rec_id)
            if (int_id >= len(ref_dict['tags'])):
                self.id_input.delete(0, END)
                self.warning_lbl = Label(self, text = "ID must be in range",
                                         fg="red")
                self.warning_lbl.grid(row = 2, column = 2)
            else:
                self.clear()
                self.curr_id = int_id
                self.id_input.insert(0, rec_id)
                tag_str = BrowsePage.detagify(self, ref_dict['tags'][int_id])
                self.tags_input.insert(0, tag_str)
                self.topic_input.insert(0, ref_dict['topics'][int_id])
                self.source_input.insert(0, ref_dict['sources'][int_id])
                self.statement_txt.insert(0.0, ref_dict['statements'][int_id])
                sol_no_latex_str = ref_dict['sol_no_latex'][int_id]
                self.solution_no_latex_txt.insert(0.0, sol_no_latex_str)
                sol_latex_str = ref_dict['sol_latex'][int_id]
                self.solution_latex_txt.insert(0.0, sol_latex_str)
                self.notes_txt.insert(0.0, ref_dict['notes'][int_id])
            f.close()
        else:
            self.id_input.delete(0, END)
            self.warning_lbl = Label(self, text = "ID must be integer",fg="red")
            self.warning_lbl.grid(row = 2, column = 2)

    def update_entry(self, controller):
        if (self.curr_id != -1):
            with open('resources.json', 'r') as f:
                ref_dict = json.load(f)
            tags_str = WritePage.tagify(self, self.tags_input.get())
            ref_dict['tags'][self.curr_id] = tags_str
            ref_dict['topics'][self.curr_id] = self.topic_input.get()
            ref_dict['sources'][self.curr_id] = self.source_input.get()
            statement_str = self.statement_txt.get("1.0", END)
            ref_dict['statements'][self.curr_id] = statement_str
            sol_str = self.solution_no_latex_txt.get("1.0", END)
            ref_dict['sol_no_latex'][self.curr_id] = sol_str
            new_sol_latex_str = self.solution_latex_txt.get("1.0", END)
            ref_dict['sol_latex'][self.curr_id] = new_sol_latex_str
            ref_dict['notes'][self.curr_id] = self.notes_txt.get("1.0", END)
        
            f.close()

            with open('resources.json', 'w') as g:
                json.dump(ref_dict, g)
            g.close()        
            
        controller.show_frame(Home)
        
        

app = Transition()
app.mainloop()
