# Inspiration for project:
# https://artofproblemsolving.com/community/u53544h1559064p9530694
from tkinter import *
import json

# Credit for multi-page structure skeleton:
# https://pythonprogramming.net/change-show-new-frame-tkinter/


# s = {'tags': tag, 'topics': topic, 'sources': source,
#      'statements': statement, 'sol_no_latex': sol_no_late,
#      'sol_latex': sol_late, 'notes': note}

# Note: do not include '#' in tag entries


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
        self.stnl = statement_no_latex # 'statement with no latex'
        self.stwl = statement_latex # 'statement with latex'
        self.sonl = solution_no_latex # 'solution with no latex'
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
        self.date = new_date

    def get_date(self):
        return self.date

    def set_difficulty(self, new_difficulty):
        self.difficulty = new_difficulty

    def get_difficulty(self):
        return self.difficulty

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
    # between them
    @staticmethod
    def tagify(tags):
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

    @staticmethod
    def detagify(tags_string):
        tags = ', '.join(tags_string.split('#'))
        if (len(tags) > 0):
            tags = tags[2:]
        return tags

    def small_string_rep(self):
        message = 'ID: ' + str(self.id) + '\n'
        message += 'Tags: ' + DataEntry.detagify(self.tags) + '\n'
        message += 'Topic: ' + self.topic + '\n'
        return message

    def medium_string_rep(self):
        message = DataEntry.small_string_rep(self)
        message += 'Source: ' + self.source + '\n'
        message += 'Date: ' + self.date + '\n'
        message += 'Statement: '
        if (self.stnl == ''):
            message += self.stwl + '\n'
        else:
            message += self.stnl + '\n'
        return message

    def large_string_rep(self):
        message = DataEntry.small_string_rep(self)
        message += 'Source: ' + self.source + '\n'
        message += 'Date: ' + self.date + '\n'
        message += 'Statement (No Latex): ' + self.stnl + '\n'
        message += 'Statement (With Latex): ' + self.stwl + '\n'
        message += 'Difficulty: ' + self.difficulty + '\n'
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
        self.geometry("540x690")
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
        #e53c12
        #fc5653
        #ff4921
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
        self.id_warning = False
        self.date_warning_start = False
        self.date_warning_end = False
        self.date_warning_chrono = False # whether input dates occur in order

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
                    command = self.toggle_tags_input,
                    variable = self.by_tags
                    ).grid(row = 4, column = 0, sticky = W)

        # 'Topic' check button
        self.by_topic = BooleanVar()
        Checkbutton(self,
                    text = "Topic",
                    command = self.toggle_topic_input,
                    variable = self.by_topic
                    ).grid(row = 5, column = 0, sticky = W)

        # 'Source' check button
        self.by_source = BooleanVar()
        Checkbutton(self,
                    text = "Source",
                    command = self.toggle_source_input,
                    variable = self.by_source
                    ).grid(row = 6, column = 0, sticky = W)

        # 'Date' range button
        self.by_date = BooleanVar()
        Checkbutton(self,
                    text = "Date",
                    command = self.toggle_date_input,
                    variable = self.by_date
                    ).grid(row = 7, column = 0, sticky = W)

        # 'Difficulty' range button
        self.by_difficulty = BooleanVar()
        Checkbutton(self,
                    text = "Difficulty",
                    command = self.toggle_difficulty_input,
                    variable = self.by_difficulty
                    ).grid(row = 9, column = 0, sticky = W)

        # 'Mentioned Words' check button
        self.by_words = BooleanVar()
        Checkbutton(self,
                    text = "Mentioned Words",
                    command = self.toggle_words_input,
                    variable = self.by_words
                    ).grid(row = 11, column = 0, sticky = W)

        # Expanded view check button
        self.expanded_view = BooleanVar()
        Checkbutton(self,
                    text = "expanded view",
                    variable = self.expanded_view
                    ).grid(row = 12, column = 1, sticky = W)

        # Button to list items
        self.bttn2 = Button(self, text = "List Items", command = self.get_items)
        self.bttn2.grid(row = 13, column = 1)

        # 'Items' label
        Label(self, text = "Items").grid(row = 14, column = 0, sticky = W)

        # Items text box
        self.results_txt = Text(self, width = 50, height = 20, wrap = WORD)
        self.results_txt.grid(row = 15, column = 0, columnspan = 3)

    def toggle_id_input(self):
        if (self.by_id.get()):
            self.id_input = Entry(self)
            self.id_input.grid(row = 3, column = 1, sticky = W)
        elif (hasattr(self, 'id_input')):
            self.id_input.grid_remove()

    def toggle_tags_input(self):
        if (self.by_tags.get()):
            self.tags_input = Entry(self)
            self.tags_input.grid(row = 4, column = 1, sticky = W)
        elif (hasattr(self, 'tags_input')):
            self.tags_input.grid_remove()

    def toggle_topic_input(self):
        if (self.by_topic.get()):
            self.topic_input = Entry(self)
            self.topic_input.grid(row = 5, column = 1, sticky = W)
        elif (hasattr(self, 'topic_input')):
            self.topic_input.grid_remove()

    def toggle_source_input(self):
        if (self.by_source.get()):
            self.source_input = Entry(self)
            self.source_input.grid(row = 6, column = 1, sticky = W)
        elif (hasattr(self, 'source_input')):
            self.source_input.grid_remove()

    def toggle_date_input(self):
        if (self.by_date.get()):
            self.start_date_lbl = Label(self, text = "Start Date")
            self.start_date_lbl.grid(row = 8, column = 0, sticky = W)
            self.start_date_input = Entry(self)
            self.start_date_input.grid(row = 8, column = 1, sticky = W)
            self.end_date_lbl = Label(self, text = "End Date")
            self.end_date_lbl.grid(row = 8, column = 2, sticky = W)
            self.end_date_input = Entry(self)
            self.end_date_input.grid(row = 8, column = 3, sticky = W)
        elif (hasattr(self, 'start_date_input')):
            self.start_date_lbl.grid_remove()
            self.start_date_input.grid_remove()
            self.end_date_lbl.grid_remove()
            self.end_date_input.grid_remove()

    def toggle_difficulty_input(self):
        if (self.by_difficulty.get()):
            self.check_easy = BooleanVar()
            self.check_medium = BooleanVar()
            self.check_hard = BooleanVar()
            self.check_no_rank = BooleanVar()
            self.button_easy = Checkbutton(self, text = "Easy",
                                           variable = self.check_easy)
            self.button_easy.grid(row = 10, column = 0, sticky = W)
            self.button_medium = Checkbutton(self, text = "Medium",
                                             variable = self.check_medium)
            self.button_medium.grid(row = 10, column = 1,sticky = W)
            self.button_hard = Checkbutton(self, text = "Hard",
                                           variable = self.check_hard)
            self.button_hard.grid(row = 10, column = 2,sticky = W)
            self.button_no_rank = Checkbutton(self, text = "No Rank",
                                              variable = self.check_no_rank)
            self.button_no_rank.grid(row = 10,column = 3,sticky = W)
        elif (hasattr(self, 'button_easy')):
            self.button_easy.grid_remove()
            self.button_medium.grid_remove()
            self.button_hard.grid_remove()
            self.button_no_rank.grid_remove()


    def toggle_words_input(self):
        if (self.by_words.get()):
            self.words_input = Entry(self)
            self.words_input.grid(row = 11, column = 1, sticky = W)
        elif (hasattr(self, 'words_input')):
            self.words_input.grid_remove()
            

    # inputs given with pound signs between entries
#    def collect_tags(self, ref_dict, inputs):
#        message = ""
#        inputs = inputs.split('#')
#        inputs = inputs[1:]
#        if (len(inputs) == 1):
#            for i in range(len(ref_dict['tags'])):
#                if (inputs[0] in ref_dict['tags'][i].split('#')[1:]):
#                    message += BrowsePage.display_entry(self, i, ref_dict)                        
#        else:
#            used_ids = {}
#            for i in range(len(ref_dict['tags'])):
#                tested = True
#                for entry in inputs:
#                    if not (entry in ref_dict['tags'][i].split('#')[1:]):
#                        tested = False
#                        break
#                if (tested):
#                    message += BrowsePage.display_entry(self, i, ref_dict)
#                    used_ids[i] = True;
#            for i in range(len(ref_dict['tags'])):
#                if not (i in used_ids):
#                    for entry in inputs:
#                        if (entry in ref_dict['tags'][i].split('#')[1:]):
#                            message += BrowsePage.display_entry(self,i,ref_dict)
#                            break
#        return message

    # reformat date string so single digit months and days have leading 0s;
    # assume date_str is a valid date string and is not ''
    @staticmethod
    def reformat_date(date_str):
        ans = date_str
        if (ans[1] == '/'):
            ans = '0' + ans
        if (ans[4] == '/'):
            ans = ans[:4] + '0' + ans[4:]
        return ans

    # check that the first listed date string comes earlier or at the same time
    # as the second listed date string;
    # assume date_early and date_late are valid date string not equal to ''
    @staticmethod
    def order_dates(date_early, date_late):
        format_early = SearchPage.reformat_date(date_early)
        format_late = SearchPage.reformat_date(date_late)
        if (int(format_early[6:]) < int(format_late[6:])):
            return True
        elif (int(format_early[6:]) > int(format_late[6:])):
            return False
        elif (int(format_early[:2]) < int(format_late[:2])):
            return True
        elif (int(format_early[:2]) > int(format_late[:2])):
            return False
        elif (int(format_early[3:5]) < int(format_late[3:5])):
            return True
        elif (int(format_early[3:5]) > int(format_late[3:5])):
            return False
        else:
            return True

    # return whether or not any element of tag_list appears among the tags of
    # the DataEntry object obj
    @staticmethod
    def data_match_tag(obj, tag_list):
        obj_tag_str = obj.get_tags()
        if (obj_tag_str == ''):
            return False
        else:
            obj_tag_arr = obj_tag_str.split('#')
            obj_tag_arr = obj_tag_arr[1:]
            for entry in tag_list:
                if (entry in obj_tag_arr):
                    return True
            return False

    # return whether the DataEntry object obj has the parameter topic as its
    # topic attribute
    @staticmethod
    def data_match_topic(obj, topic):
        return topic == obj.get_topic()

    # return whether the DataEntry object obj has the parameter source as its
    # source attribute or at least contains the source in the attribute
    @staticmethod
    def data_match_source(obj, source):
        return (source in obj.get_source())

    # return whether the DataEntry object obj has the parameter date within
    # the specified date range;
    # assume all dates are valid
    @staticmethod
    def data_match_date(obj, start_date, end_date):
        if (obj.get_date() == ''):
            return True
        a = SearchPage.order_dates(start_date, obj.get_date())
        b = SearchPage.order_dates(obj.get_date(), end_date)
        return (a and b)

    # return whether the DataEntry object obj matches any of the True booleans
    # from among is_easy, is_medium, is_hard, is_no_rank
    @staticmethod
    def data_match_difficulty(obj, is_easy, is_medium, is_hard, is_no_rank):
        if ((obj.get_difficulty() == 'easy') and is_easy):
            return True
        elif ((obj.get_difficulty() == 'medium') and is_medium):
            return True
        elif ((obj.get_difficulty() == 'hard') and is_hard):
            return True
        elif ((obj.get_difficulty() == 'no rank') and is_no_rank):
            return True
        else:
            print('Nothing: ')
            return False

    # return list containing objects matching the query;
    # assumes that if ID box is checked, then the given ID is valid (possibly
    # '') and likewise for date values
    def filter_query(self, ref):
        mod_ref = ref
        if (self.by_id.get() and (self.id_input.get() != '')):
            mod_ref = [mod_ref[int(self.id_input.get())]]
        if (self.by_tags.get() and (self.tags_input.get() != '')):
            tag_string = DataEntry.tagify(self.tags_input.get())
            tag_list = tag_string.split('#')
            tag_list = tag_list[1:]
            mod_ref = list(filter(lambda x: SearchPage.data_match_tag(x, tag_list),
                                  mod_ref))
        if (self.by_topic.get() and (self.topic_input.get() != '')):
            mod_ref = list(filter(lambda x: SearchPage.data_match_topic(x, self.topic_input.get()),
                                  mod_ref))
        if (self.by_source.get() and (self.source_input.get() != '')):
            mod_ref = list(filter(lambda x: SearchPage.data_match_source(x, self.source_input.get()),
                                  mod_ref))
        if (self.by_date.get() and (self.start_date_input.get() != '') and (self.end_date_input.get() != '')):
            mod_ref = list(filter(lambda x: SearchPage.data_match_date(x, self.start_date_input.get(),
                                                                       self.end_date_input.get()),
                                  mod_ref))
        if self.by_difficulty.get():
            mod_ref = list(filter(lambda x: SearchPage.data_match_difficulty(x, self.check_easy.get(),
                                                                             self.check_medium.get(),
                                                                             self.check_hard.get(),
                                                                             self.check_no_rank.get()),
                                  mod_ref))
        return mod_ref



    # list items matching the query or highlight errors in input
    def get_items(self):
        if (self.id_warning):
            self.id_warning = False
            self.id_warning_lbl.grid_remove()
        if (self.date_warning_start):
            self.date_warning_start = False
            self.date_warning_lbl_start.grid_remove()
        if (self.date_warning_end):
            self.date_warning_end = False
            self.date_warning_lbl_end.grid_remove()
        if (self.date_warning_chrono):
            self.date_warning_chrono = False
            self.date_warning_lbl_chrono.grid_remove()
            
        if (self.by_id.get() and (self.id_input.get() != '') and
            (not EditPage.check_for_int(self,self.id_input.get()))):
            if not (self.id_warning):
                self.id_warning = True
                self.id_warning_lbl = Label(self,
                                            text = "ID must be integer",
                                            fg="red")
                self.id_warning_lbl.grid(row = 3, column = 2)
        elif (self.by_date.get() and ((not WritePage.is_valid_date(self,self.start_date_input.get())) or (self.start_date_input.get() == ''))):
            if (not (self.date_warning_start)):
                self.date_warning_start = True
                self.date_warning_lbl_start = Label(self,
                                                    text = "Start date must be valid",
                                                    fg="red")
                self.date_warning_lbl_start.grid(row = 7, column = 1)
        elif (self.by_date.get() and ((not WritePage.is_valid_date(self,self.end_date_input.get())) or (self.end_date_input.get() == ''))):
            if (not (self.date_warning_end)):
                self.date_warning_end = True
                self.date_warning_lbl_end = Label(self,
                                                  text = "End date must be valid",
                                                  fg="red")
                self.date_warning_lbl_end.grid(row = 7, column = 3)
        elif (self.by_date.get() and
              (not SearchPage.order_dates(self.start_date_input.get(), self.end_date_input.get()))):
            if (not (self.date_warning_chrono)):
                self.date_warning_chrono = True
                self.date_warning_lbl_chrono = Label(self,
                                                     text = "Dates must be ordered",
                                                     fg="red")
                self.date_warning_lbl_chrono.grid(row = 6, column = 1)
        else:
            with open('resources.json', 'r') as f:
                ref_dict = json.load(f)
            ref = [DataEntry.from_dict(entry) for entry in ref_dict]
            ref_mod = SearchPage.filter_query(self, ref)
            message = ''
            for entry in ref_mod:
                message += DataEntry.search_rep(entry, self.expanded_view.get())
                message += '\n'
            self.results_txt.delete(0.0, END)
            self.results_txt.insert(0.0, message)
            #print('Reached here: ' + str(self.by_date.get()))
            #print('Start: ' + str(self.start_date_input.get() == ''))
        # set warning booleans back to False and remove warning labels





    # clear the entry and text boxes of any data from previous uses
    def clear(self):
        if (self.by_id.get()):
            self.id_input.grid_remove()
            self.by_id.set(False)
        if (self.by_tags.get()):
            self.tags_input.grid_remove()
            self.by_tags.set(False)
        if (self.by_topic.get()):
            self.topic_input.grid_remove()
            self.by_topic.set(False)
        if (self.by_source.get()):
            self.source_input.grid_remove()
            self.by_source.set(False)
        if (self.by_date.get()):
            self.start_date_lbl.grid_remove()
            self.start_date_input.grid_remove()
            self.end_date_lbl.grid_remove()
            self.end_date_input.grid_remove()
            self.by_date.set(False)
        if (self.by_difficulty.get()):
            self.button_easy.grid_remove()
            self.button_medium.grid_remove()
            self.button_hard.grid_remove()
            self.button_no_rank.grid_remove()
            self.by_difficulty.set(False)
        if (self.by_words.get()):
            self.words_input.grid_remove()
            self.by_words.set(False)
        self.expanded_view.set(False)
        self.results_txt.delete(0.0, END)
        if (self.id_warning):
            self.id_warning = False
            self.id_warning_lbl.grid_remove()
        if (self.date_warning_start):
            self.date_warning_start = False
            self.date_warning_start_lbl.grid_remove()
        if (self.date_warning_end):
            self.date_warning_end = False
            self.date_warning_end_lbl.grid_remove()
        if (self.date_warning_chrono):
            self.date_warning_chrono = False
            self.date_warning_lbl_chrono.grid_remove()
        


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
    #    tag_string = BrowsePage.detagify(ref_dict['tags'][index]) + '\n'
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
        # Whether message about invalid input is visible
        self.input_warning = False
        # Whether message about invalid date is visible
        self.date_warning = False
        
        # 'Add Entry' button
        self.bttn2 = Button(self, text = "Add Entry",
                            command=lambda: self.save_inputs(controller))
        self.bttn2.grid(row = 17, column = 1)

        # 'Cancel' button
        self.bttn3 = Button(self, text = "Cancel",
                            command=lambda: controller.show_frame(Home))
        self.bttn3.grid(row = 17, column = 2)

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

        # 'Date' label
        Label(self, text = "Date (MM/DD/YYYY)").grid(row = 3 + offset,
                                                     column = 0, sticky = W)

        # Date input entry
        self.date_input = Entry(self)
        self.date_input.grid(row = 3 + offset, column = 1, sticky = W)

        # 'Difficulty' label
        Label(self, text = "Difficulty").grid(row = 4 + offset,
                                                     column = 0, sticky = W)

        # Difficulty radio buttons
        self.difficulty = StringVar()
        self.difficulty.set(None)
        difficulties = ['easy', 'medium', 'hard', 'no rank']
        column = 1
        for rank in difficulties:
            Radiobutton(self, text = rank, variable = self.difficulty,
                        value = rank).grid(row = 4 + offset, column = column,
                                           sticky = W)
            column += 1

        # 'Statement (no latex)' label
        Label(self, text = "Statement (no latex)").grid(row = 5 + offset,
                                                        column = 0, sticky = W)

        # Statement (no latex) text box
        self.stnl = Text(self, width = 30, height = 5, wrap = WORD)
        self.stnl.grid(row = 6 + offset, column = 0, columnspan = 3, sticky = W)

        # 'Statement (latex)' label
        Label(self, text = "Statement (with latex)").grid(row = 7 + offset,
                                                          column = 0,
                                                          sticky = W)

        # Statement (latex) text box
        self.stwl = Text(self, width = 30, height = 5, wrap = WORD)
        self.stwl.grid(row = 8 + offset, column = 0, columnspan = 3, sticky = W)

        # 'Solution' (without latex) label
        Label(self, text = "Solution (no latex)").grid(row = 9 + offset,
                                                       column = 0, sticky = W)

        # Solution without latex text box
        self.sonl = Text(self, width = 30, height = 5, wrap = WORD)
        self.sonl.grid(row = 10 + offset, column = 0, columnspan = 3,
                       sticky = W)

        # 'Solution' (with latex) label
        Label(self, text = "Solution (with latex)").grid(row = 11 + offset,
                                                         column = 0, sticky = W)

        # Solution with latex text box
        self.sowl = Text(self, width = 30, height = 5, wrap = WORD)
        self.sowl.grid(row = 12 + offset, column = 0, columnspan = 3,
                       sticky = W)

        # 'Notes' label
        Label(self, text = "Notes").grid(row = 13 + offset,
                                         column = 0, sticky = W)

        # Notes text box
        self.notes = Text(self, width = 30, height = 5, wrap = WORD)
        self.notes.grid(row = 14 + offset, column = 0, columnspan = 3,
                        sticky = W)

    # clear write page of inputs
    def clear(self):
        self.tags_input.delete(0, END)
        self.topic_input.delete(0, END)
        self.source_input.delete(0, END)
        self.date_input.delete(0, END)
        self.stnl.delete(0.0, END)
        self.stwl.delete(0.0, END)
        self.sonl.delete(0.0, END)
        self.sowl.delete(0.0, END)
        self.notes.delete(0.0, END)
        self.difficulty.set(None)
        if (self.date_warning):
            self.date_warning = False
            self.warning_lbl.grid_remove()
        if (self.input_warning):
            self.input_warning = False
            self.data_lbl.grid_remove()
        #if (hasattr(self, 'data_lbl')):
        #    self.data_lbl.grid_remove()


    # check whether date string is valid; a valid string is '' or a string of
    # the form 'MM/DD/YYYY' where (MM,DD) is a valid month-day pair
    def is_valid_date(self,ds):
        if ((len(ds) >= 2) and (ds[1] == '/')):
            ds = '0' + ds
        if ((len(ds) >= 5) and (ds[4] == '/')):
            ds = ds[:3] + '0' + ds[3:]
        if (ds == ''):
            return True
        elif ((len(ds) < 3) or (ds[2] != '/')):
            return False
        elif ((len(ds) < 6) or (ds[5] != '/')):
            return False
        elif not ((EditPage.check_for_int(self,ds[0:2])) and
                  (EditPage.check_for_int(self,ds[3:5])) and
                  (EditPage.check_for_int(self,ds[6:]))):
            return False
        elif not ((int(ds[0:2]) >= 1) and (int(ds[0:2]) <= 12)):
            return False
        elif not ((int(ds[3:5]) >= 1) and (int(ds[3:5]) <= 31)):
            return False
        elif ((int(ds[0:2]) == 2) and (int(ds[3:5]) > 29)):
            return False
        elif (((int(ds[0:2]) == 4) or (int(ds[0:2]) == 6) or
               (int(ds[0:2]) == 9) or (int(ds[0:2]) == 11)) and
              (int(ds[3:5]) > 30)):
            return False
        return True

    # check that write page entry has some content
    def has_inputs(self):
        if (self.tags_input.get() != ''):
            return True
        elif (self.topic_input.get() != ''):
            return True
        elif (self.source_input.get() != ''):
            return True
        elif (self.date_input.get() != ''):
            return True
        elif (self.stnl.get("1.0", END) != '\n'):
            print('Value: ' + self.stnl.get("1.0", END))
            return True
        elif (self.stwl.get("1.0", END) != '\n'):
            return True
        elif (self.sonl.get("1.0", END) != '\n'):
            return True
        elif (self.sowl.get("1.0", END) != '\n'):
            return True
        elif (self.notes.get("1.0", END) != '\n'):
            return True
        elif ((self.difficulty.get() == 'easy') or
              (self.difficulty.get() == 'medium') or
              (self.difficulty.get() == 'hard') or
              (self.difficulty.get() == 'no rank')):
            return True
        else:
            return False

    # if a trailing '\n' is present in the content of a text widget, then
    # remove it
    @staticmethod
    def truncate_new_line(in_str):
        ans = in_str
        if ((len(ans) > 0) and (ans[-1] == '\n')):
            ans = ans[:-1]
        return ans

    @staticmethod
    def ret_difficulty(diff):
        if ((diff == 'easy') or (diff == 'medium') or (diff == 'hard') or
            (diff == 'no rank')):
            return diff
        return 'no rank'


    def save_inputs(self, controller):
        with open('resources.json', 'r') as f:
            ref_dict = json.load(f)
        ref = [DataEntry.from_dict(entry) for entry in ref_dict]
        f.close()

        tags = DataEntry.tagify(self.tags_input.get())
        topic = self.topic_input.get()
        source = self.source_input.get()
        date = self.date_input.get()
        difficulty = WritePage.ret_difficulty(self.difficulty.get())
        stnl = WritePage.truncate_new_line(self.stnl.get("1.0", END))
        stwl = WritePage.truncate_new_line(self.stwl.get("1.0", END))
        sonl = WritePage.truncate_new_line(self.sonl.get("1.0", END))
        sowl = WritePage.truncate_new_line(self.sowl.get("1.0", END))
        notes = WritePage.truncate_new_line(self.notes.get("1.0", END))

        if not(WritePage.has_inputs(self)):
            if (hasattr(self, 'warning_lbl') and self.date_warning):
                self.date_warning = False
                self.warning_lbl.grid_remove()
            if not (self.input_warning):
                self.input_warning = True
                self.data_lbl = Label(self, text = "Entry must include data",
                                      fg="red")
                self.data_lbl.grid(row = 17, column = 0)

        elif (WritePage.is_valid_date(self,date)):
            new_entry = DataEntry(len(ref), tags, topic, source, date,
                                  difficulty, stnl, stwl, sonl, sowl, notes)
            ref.append(new_entry)

            with open('resources.json', 'w') as g:
                ref_dict = [ob.to_dict() for ob in ref]
                json.dump(ref_dict, g)
            g.close()        
            controller.show_frame(Home)

        else:
            if (hasattr(self, 'data_lbl') and self.input_warning):
                self.input_warning = False
                self.data_lbl.grid_remove()
            if not (self.date_warning):
                self.date_warning = True
                self.warning_lbl = Label(self, text = "Must be valid date",
                                         fg="red")
                self.warning_lbl.grid(row = 5, column = 2)



class EditPage(Frame):
    """ Edit an entry based on the ID """
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.grid()
        self.set_format(controller)
        self.curr_id = -1
        self.warning_id = False # whether message about invalid id is visible
        # whether message about invalid date is visible
        self.warning_date = False

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
        self.bttn3.grid(row = 19,column = 0)

        # Cancel button
        self.bttn4 = Button(self, text = "Cancel",
                            command=lambda: controller.show_frame(Home))
        self.bttn4.grid(row = 19,column = 1)

    def clear(self):
        self.id_input.delete(0, END)
        self.tags_input.delete(0, END)
        self.topic_input.delete(0, END)
        self.source_input.delete(0, END)
        self.date_input.delete(0, END)
        self.stnl.delete(0.0, END)
        self.stwl.delete(0.0, END)
        self.sonl.delete(0.0, END)
        self.sowl.delete(0.0, END)
        self.notes.delete(0.0, END)
        self.difficulty.set(None)
        if (self.warning_id):
            self.warning_id = False
            self.red_id.grid_remove()
        if (self.warning_date):
            self.warning_date = False
            self.red_date.grid_remove()
        self.curr_id = -1

    def check_for_int(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    def populate_by_id(self):
        if (self.warning_id):
            self.warning_id = False
            self.red_id.grid_remove()
        if (self.warning_date):
            self.warning_date = False
            self.red_date.grid_remove()
        rec_id = self.id_input.get()
        if (EditPage.check_for_int(self,rec_id)):
            with open('resources.json', 'r') as f:
                ref_dict = json.load(f)
            ref = [DataEntry.from_dict(entry) for entry in ref_dict]
            int_id = int(rec_id)
            if ((int_id >= len(ref_dict)) or (int_id < 0)):
                #self.id_input.delete(0, END)
                if (self.warning_id):
                    self.warning_id = False
                    self.red_id.grid_remove()
                self.red_id = Label(self, text = "ID must be in range",
                                    fg="red")
                self.red_id.grid(row = 2, column = 2)
                self.warning_id = True
            else:
                self.clear()
                self.curr_id = int_id
                self.id_input.insert(0, rec_id)
                tag_str = DataEntry.detagify(ref[int_id].get_tags())
                self.tags_input.insert(0, tag_str)
                self.topic_input.insert(0, ref[int_id].get_topic())
                self.source_input.insert(0, ref[int_id].get_source())
                self.difficulty.set(ref[int_id].get_difficulty())
                self.date_input.insert(0, ref[int_id].get_date())
                self.stnl.insert(0.0, ref[int_id].get_stnl())
                self.stwl.insert(0.0, ref[int_id].get_stwl())
                sol_no_latex_str = ref[int_id].get_sonl()
                self.sonl.insert(0.0, sol_no_latex_str)
                sol_latex_str = ref[int_id].get_sowl()
                self.sowl.insert(0.0, sol_latex_str)
                self.notes.insert(0.0, ref[int_id].get_notes())
            f.close()
        else:
            #self.id_input.delete(0, END)
            if (self.warning_id):
                self.warning_id = False
                self.red_id.grid_remove()
            self.red_id = Label(self, text = "ID must be integer",fg="red")
            self.red_id.grid(row = 2, column = 2)
            self.warning_id = True

    def update_entry(self, controller):
        if not (WritePage.is_valid_date(self,self.date_input.get())):
            if not (self.warning_date):
                self.warning_date = True
                self.red_date = Label(self, text = "Must be valid date",
                                      fg="red")
                self.red_date.grid(row = 7, column = 2)
        else:
            if (self.curr_id != -1):
                with open('resources.json', 'r') as f:
                    ref_dict = json.load(f)
                ref = [DataEntry.from_dict(entry) for entry in ref_dict]      
            
                tags_str = DataEntry.tagify(self.tags_input.get())
                ref[self.curr_id].set_tags(tags_str)
                ref[self.curr_id].set_topic(self.topic_input.get())
                ref[self.curr_id].set_source(self.source_input.get())
                ref[self.curr_id].set_date(self.date_input.get())
                diff_str = WritePage.ret_difficulty(self.difficulty.get())
                ref[self.curr_id].set_difficulty(diff_str)
                stnl_str = self.stnl.get("1.0", END)[:-1]
                ref[self.curr_id].set_stnl(stnl_str)
                stwl_str = self.stwl.get("1.0", END)[:-1]
                ref[self.curr_id].set_stwl(stwl_str)
                sonl_str = self.sonl.get("1.0", END)[:-1]
                ref[self.curr_id].set_sonl(sonl_str)
                sowl_str = self.sowl.get("1.0", END)[:-1]
                ref[self.curr_id].set_sowl(sowl_str)
                ref[self.curr_id].set_notes(self.notes.get("1.0", END)[:-1])
        
                f.close()

                with open('resources.json', 'w') as g:
                    ref_dict = [ob.to_dict() for ob in ref]
                    json.dump(ref_dict, g)
                g.close()        
            
            controller.show_frame(Home)



app = Transition()
app.mainloop()
