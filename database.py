# Inspiration for project:
# https://artofproblemsolving.com/community/u53544h1559064p9530694
from tkinter import *
import json

# Credit for multi-page structure skeleton:
# https://pythonprogramming.net/change-show-new-frame-tkinter/


# s = {'tags': tag, 'topics': topic, 'sources': source,
#      'statements': statement, 'sol_no_latex': sol_no_late,
#      'sol_latex': sol_late, 'notes': note}


# class to serialize objects in JSON file
# credit for this class:
# https://code.tutsplus.com/tutorials/serialization-and-deserialization-of-
# python-objects-part-1--cms-26183
#class CustomEncoder(json.JSONEncoder):
#    def default(self, o):
#        return {'__{}__'.format(o.__class__.__name__): o.__dict__}


# class for individual entries to database
class DataEntry():
    def __init__(self, new_id, tags = '', topic = '', source = '', date = '',
                 difficulty = '', statement_no_latex = '', statement_latex = '',
                 solution_no_latex = '', solution_latex = '', notes = ''):
        self.id = new_id
        self.tags = tags
        self.topic = topic
        self.source = source
        self.date = date
        self.difficulty = difficulty
        self.stnl = statement_no_latex # 'statement no latex'
        self.stwl = statement_latex # 'statement with latex'
        self.sonl = solution_no_latex # 'solution no latex'
        self.sowl = solution_latex # 'solution with latex'
        self.notes = notes

    def set_id(self, new_id):
        self.id = new_id

    def set_tags(self, new_tags):
        self.tags = new_tags

    def get_tags(self):
        return self.tags

    def set_topic(self, new_topic):
        self.topic = new_topic

    def get_topic(self):
        return self.topic

    def set_source(self, new_source):
        self.source = new_source

    def get_source(self):
        return self.source

    def set_date(self, new_date):
        raise SyntaxError('Uncertain How To Represent Dates')

    def set_difficulty(self, new_difficulty):
        self.difficulty = new_difficulty

    def set_stnl(self, new_stat):
        self.stnl = new_stat

    def get_stnl(self):
        return self.stnl

    def set_stwl(self, new_stat):
        self.stwl = new_stat

    def get_stwl(self):
        return self.stwl

    def set_sonl(self, new_sol):
        self.sonl = new_sol

    def get_sonl(self):
        return self.sonl

    def set_sowl(self, new_sol):
        self.sowl = new_sol

    def get_sowl(self):
        return self.sowl

    def set_notes(self, new_notes):
        self.notes = new_notes

    def get_notes(self):
        return self.notes

    # given the tags listed with commas and possibly spaces, place pound signs
    # between tags
    def tagify(self, tags):
        tag_arr = tags.split(',')
        for i in range(len(tag_arr)):
            j = 0
            while ((j < len(tag_arr[i])) and (tag_arr[i][j] == ' ')):
                j += 1
            tag_arr[i] = tag_arr[i][j:]
            j = len(tag_arr[i])-1
            while ((j >= 0) and (tag_arr[i][j] == ' ')):
                j-= 1
            tag_arr[i] = tag_arr[i][:(j+1)]
        ans = '#'.join(tag_arr)
        if (len(ans) > 0):
            ans = '#' + ans
        return ans

    def detagify(self, tags_string):
        tags = ', '.join(tags_string.split('#'))
        if (len(tags) > 0):
            tags = tags[2:]
        return tags

    def small_string_rep(self):
        message = 'ID: ' + str(self.id) + '\n'
        message += 'Tags: ' + DataEntry.detagify(self,self.tags) + '\n'
        message += 'Topic: ' + self.topic + '\n'
        return message

    def medium_string_rep(self):
        message = DataEntry.small_string_rep(self)
        message += 'Source: ' + self.source + '\n'
        message += 'Statement: '
        if (self.stnl == ''):
            message += self.stwl + '\n'
        else:
            message += self.stnl + '\n'
        return message

    def large_string_rep(self):
        message = DataEntry.small_string_rep(self)
        message += 'Source: ' + self.source + '\n'
        message += 'Statement (No Latex): ' + self.stnl + '\n'
        message += 'Statement (With Latex): ' + self.stwl + '\n'
        message += 'Difficulty: ' + str(self.difficulty) + '\n'
        message += 'Solution (No Latex): ' + self.sonl + '\n'
        message += 'Solution (With Latex): ' + self.sowl + '\n'
        message += 'Notes: ' + self.notes + '\n'
        return message

    def browse_rep(self, expand):
        if (expand):
            return DataEntry.medium_string_rep(self)
        else:
            return DataEntry.small_string_rep(self)

    def search_rep(self, expand):
        if (expand):
            return DataEntry.large_string_rep(self)
        else:
            return DataEntry.medium_string_rep(self)

    # return a dictionary representation of the object for JSON serialization
    def to_dict(self):
        ent_dict = {}
        ent_dict['id'] = self.id
        ent_dict['tags'] = self.tags
        ent_dict['topic'] = self.topic
        ent_dict['source'] = self.source
        ent_dict['date'] = self.date
        ent_dict['difficulty'] = self.difficulty
        ent_dict['stnl'] = self.stnl
        ent_dict['stwl'] = self.stwl
        ent_dict['sonl'] = self.sonl
        ent_dict['sowl'] = self.sowl
        ent_dict['notes'] = self.notes
        return ent_dict

    # return a DataEntry object representation of the dictionary
    @staticmethod
    def from_dict(ent_dict):
        return DataEntry(ent_dict['id'], ent_dict['tags'], ent_dict['topic'],
                         ent_dict['source'], ent_dict['date'],
                         ent_dict['difficulty'], ent_dict['stnl'],
                         ent_dict['stwl'], ent_dict['sonl'], ent_dict['sowl'],
                         ent_dict['notes'])


class Transition(Tk):
    def __init__(self):
        Tk.__init__(self)
        container = Frame(self)

        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.title("Database")
        self.geometry("370x670")
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

        # 'ID' check button
        self.by_id = BooleanVar()
        Checkbutton(self,
                    text = "ID",
                    command = self.toggle_id_input,
                    variable = self.by_id
                    ).grid(row = 3, column = 0, sticky = W)

        # 'Tags' check button
        self.by_tags = BooleanVar()
        Checkbutton(self,
                    text = "Tags",
                    variable = self.by_tags
                    ).grid(row = 4, column = 0, sticky = W)

        # 'Topic' check button
        self.by_topic = BooleanVar()
        Checkbutton(self,
                    text = "Topic",
                    variable = self.by_topic
                    ).grid(row = 5, column = 0, sticky = W)

        # 'Source' check button
        self.by_source = BooleanVar()
        Checkbutton(self,
                    text = "Source",
                    variable = self.by_source
                    ).grid(row = 6, column = 0, sticky = W)

        # 'Date' range button
        self.by_date = BooleanVar()
        Checkbutton(self,
                    text = "Date",
                    variable = self.by_date
                    ).grid(row = 7, column = 0, sticky = W)

        # 'Difficulty' range button
        self.by_difficulty = BooleanVar()
        Checkbutton(self,
                    text = "Difficulty",
                    variable = self.by_date
                    ).grid(row = 8, column = 0, sticky = W)

        # 'Mentioned Words' check button
        self.by_words = BooleanVar()
        Checkbutton(self,
                    text = "Mentioned Words",
                    variable = self.by_words
                    ).grid(row = 9, column = 0, sticky = W)

        # Expanded view check button
        self.expanded_view = BooleanVar()
        Checkbutton(self,
                    text = "expanded view",
                    variable = self.expanded_view
                    ).grid(row = 10, column = 1, sticky = W)

        # Button to list items
        self.bttn2 = Button(self, text = "List Items", command = self.get_items)
        self.bttn2.grid(row = 11, column = 1)

        # 'Items' label
        Label(self, text = "Items").grid(row = 12, column = 0, sticky = W)

        # Items text box
        self.results_txt = Text(self, width = 30, height = 5, wrap = WORD)
        self.results_txt.grid(row = 13, column = 0, columnspan = 3)

    def toggle_id_input(self):
        if (self.by_id.get()):
            self.id_input = Entry(self)
            self.id_input.grid(row = 3, column = 1, sticky = W)
        else:
            if (hasattr(self, 'id_input')):
                self.id_input.grid_remove()
            
            

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

    # list matching items
    def get_items(self):
        print('eraser')
#        inputs = self.inputs.get()
#        if (inputs == ''):
#            message = BrowsePage.display(self)
#            self.results_txt.delete(0.0, END)
#            self.results_txt.insert(0.0, message)
#        else:
#            message = ''
#            with open('resources.json', 'r') as f:
#                ref_dict = json.load(f)
#            if (self.query_type.get() == 'Tags'):
#                inputs = WritePage.tagify(self, inputs)
#                message = SearchPage.collect_tags(self, ref_dict, inputs)
#            elif (self.query_type.get() == 'Mentioned Words'):
#                print('aisle')
#            elif (self.query_type.get() == 'Topic'):
#                print('aisle')
#            elif (self.query_type.get() == 'ID'):
#                print('aisle')
#            elif (self.query_type.get() == 'Source'):
#                print('aisle')
#        
#            f.close()

#            if (message == ''):
#                message = 'No matching entries'
#            self.results_txt.delete(0.0, END)
#            self.results_txt.insert(0.0, message)

    # clear the entry and text boxes of any data from previous uses
    def clear(self):
        self.by_id.set(False)
        self.by_tags.set(False)
        self.by_topic.set(False)
        self.by_source.set(False)
        self.by_date.set(False)
        self.by_difficulty.set(False)
        self.by_words.set(False)
        self.expanded_view.set(False)
        self.results_txt.delete(0.0, END)
        


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
    
    # structure format for display of entry in 'browse' section
    #def display_entry(self, index, ref_dict):
    #    message = 'ID: ' + str(index) + '\n'
    #    message += 'Topic: ' + ref_dict['topics'][index] + '\n'
    #    tag_string = BrowsePage.detagify(self, ref_dict['tags'][index]) + '\n'
    #    message +='Tags: ' + tag_string
    #    if (self.expanded_view.get()):
    #        message += 'Statement: '
    #        message += ref_dict['statements'][index] + '\n'
    #    message += '\n'
    #    return message

    def display(self):
        message = ""
        with open('resources.json', 'r') as f:
            ref_dict = json.load(f)
        ref = [DataEntry.from_dict(entry) for entry in ref_dict]

        for i in range(len(ref)):
            message += ref[i].browse_rep(self.expanded_view.get())
            message += '\n'

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
        self.bttn2.grid(row = 15, column = 1)

        # 'Cancel' button
        self.bttn3 = Button(self, text = "Cancel",
                            command=lambda: controller.show_frame(Home))
        self.bttn3.grid(row = 15, column = 2)

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

        # 'Statement (no latex)' label
        Label(self, text = "Statement (no latex)").grid(row = 3 + offset,
                                                        column = 0, sticky = W)

        # Statement (no latex) text box
        self.stnl = Text(self, width = 30, height = 5, wrap = WORD)
        self.stnl.grid(row = 4 + offset, column = 0, columnspan = 3, sticky = W)

        # 'Statement (latex)' label
        Label(self, text = "Statement (no latex)").grid(row = 5 + offset,
                                                        column = 0, sticky = W)

        # Statement (latex) text box
        self.stwl = Text(self, width = 30, height = 5, wrap = WORD)
        self.stwl.grid(row = 6 + offset, column = 0, columnspan = 3, sticky = W)

        # 'Solution' (without latex) label
        Label(self, text = "Solution (no latex)").grid(row = 7 + offset,
                                                       column = 0, sticky = W)

        # Solution without latex text box
        self.sonl = Text(self, width = 30, height = 5, wrap = WORD)
        self.sonl.grid(row = 8 + offset, column = 0, columnspan = 3, sticky = W)

        # 'Solution' (with latex) label
        Label(self, text = "Solution (with latex)").grid(row = 9 + offset,
                                                         column = 0, sticky = W)

        # Solution with latex text box
        self.sowl = Text(self, width = 30, height = 5, wrap = WORD)
        self.sowl.grid(row = 10 + offset, column = 0, columnspan = 3,
                       sticky = W)

        # 'Notes' label
        Label(self, text = "Notes").grid(row = 11 + offset,
                                         column = 0, sticky = W)

        # Notes text box
        self.notes = Text(self, width = 30, height = 5, wrap = WORD)
        self.notes.grid(row = 12 + offset, column = 0, columnspan = 3,
                        sticky = W)

    # clear write page of inputs
    def clear(self):
        self.tags_input.delete(0, END)
        self.topic_input.delete(0, END)
        self.source_input.delete(0, END)
        self.stnl.delete(0.0, END)
        self.stwl.delete(0.0, END)
        self.sonl.delete(0.0, END)
        self.sowl.delete(0.0, END)
        self.notes.delete(0.0, END)


    def save_inputs(self, controller):
        with open('resources.json', 'r') as f:
            ref_dict = json.load(f)
        ref = [DataEntry.from_dict(entry) for entry in ref_dict]

        tags = DataEntry.tagify(self, self.tags_input.get())
        topic = self.topic_input.get()
        source = self.source_input.get()
        date = '01/01/2000'
        difficulty = 1
        stnl = self.stnl.get("1.0", END)
        stwl = self.stwl.get("1.0", END)
        sonl = self.sonl.get("1.0", END)
        sowl = self.sowl.get("1.0", END)
        notes = self.notes.get("1.0", END)

        new_entry = DataEntry(len(ref), tags, topic, source, date,
                              difficulty, stnl, stwl, sonl, sowl, notes)
        ref.append(new_entry)
        
        f.close()

        with open('resources.json', 'w') as g:
            ref_dict = [ob.to_dict() for ob in ref]
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
        self.bttn3.grid(row = 17,column = 0)

        # Cancel button
        self.bttn4 = Button(self, text = "Cancel",
                            command=lambda: controller.show_frame(Home))
        self.bttn4.grid(row = 17,column = 1)

    def clear(self):
        self.id_input.delete(0, END)
        self.tags_input.delete(0, END)
        self.topic_input.delete(0, END)
        self.source_input.delete(0, END)
        self.stnl.delete(0.0, END)
        self.stwl.delete(0.0, END)
        self.sonl.delete(0.0, END)
        self.sowl.delete(0.0, END)
        self.notes.delete(0.0, END)
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
            ref = [DataEntry.from_dict(entry) for entry in ref_dict]
            int_id = int(rec_id)
            if (int_id >= len(ref_dict)):
                self.id_input.delete(0, END)
                self.warning_lbl = Label(self, text = "ID must be in range",
                                         fg="red")
                self.warning_lbl.grid(row = 2, column = 2)
            else:
                self.clear()
                self.curr_id = int_id
                self.id_input.insert(0, rec_id)
                tag_str = DataEntry.detagify(self, ref[int_id].get_tags())
                self.tags_input.insert(0, tag_str)
                self.topic_input.insert(0, ref[int_id].get_topic())
                self.source_input.insert(0, ref[int_id].get_source())
                self.stnl.insert(0.0, ref[int_id].get_stnl())
                self.stwl.insert(0.0, ref[int_id].get_stwl())
                sol_no_latex_str = ref[int_id].get_sonl()
                self.sonl.insert(0.0, sol_no_latex_str)
                sol_latex_str = ref[int_id].get_sowl()
                self.sowl.insert(0.0, sol_latex_str)
                self.notes.insert(0.0, ref[int_id].get_notes())
            f.close()
        else:
            self.id_input.delete(0, END)
            self.warning_lbl = Label(self, text = "ID must be integer",fg="red")
            self.warning_lbl.grid(row = 2, column = 2)

    def update_entry(self, controller):
        if (self.curr_id != -1):
            with open('resources.json', 'r') as f:
                ref_dict = json.load(f)
            ref = [DataEntry.from_dict(entry) for entry in ref_dict]      
            
            tags_str = DataEntry.tagify(self, self.tags_input.get())
            ref[self.curr_id].set_tags(tags_str)
            ref[self.curr_id].set_topic(self.topic_input.get())
            ref[self.curr_id].set_source(self.source_input.get())
            stnl_str = self.stnl.get("1.0", END)
            ref[self.curr_id].set_stnl(stnl_str)
            stwl_str = self.stwl.get("1.0", END)
            ref[self.curr_id].set_stwl(stwl_str)
            sonl_str = self.sonl.get("1.0", END)
            ref[self.curr_id].set_sonl(sonl_str)
            sowl_str = self.sowl.get("1.0", END)
            ref[self.curr_id].set_sowl(sowl_str)
            ref[self.curr_id].set_notes(self.notes.get("1.0", END))
        
            f.close()

            with open('resources.json', 'w') as g:
                ref_dict = [ob.to_dict() for ob in ref]
                json.dump(ref_dict, g)
            g.close()        
            
        controller.show_frame(Home)
        
        

app = Transition()
app.mainloop()
