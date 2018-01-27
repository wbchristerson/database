from tkinter import *
import DataEntry as DE
import json

class SearchPage(Frame):
    """ Search for entries based on various pieces of information """
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.grid_columnconfigure(1, weight=1)
        #6df241
        #a2dba7
        self.config(bg="#a2dba7")
        self.grid()
        self.set_format(controller)
        self.id_warning = False
        self.date_warning_start = False
        self.date_warning_end = False
        self.date_warning_chrono = False # whether input dates occur in order
        self.has_been_executed = False

    def set_format(self, controller):
        # Page title
        lbl = Label(self, text = "Look Up An Entry", font= ("Verdana", 14),
                    bg="#a2dba7")
        lbl.grid(row = 0, column = 1, pady = 5)

        # Menu return button
        self.bttn1 = Button(self, text = "Return To Menu",
                            font= ("Verdana", 11), width = 15,
                            command=lambda: controller.return_home())
        self.bttn1.grid(row=1,column=1, pady = 4)

        # 'Match By' label
        Label(self, text = "Match By:", bg="#a2dba7",
              font= ("Verdana", 11)).grid(row = 2, column = 0, sticky = W,
                                          ipadx = 25)

        # 'ID' check button
        self.by_id = BooleanVar()
        Checkbutton(self,
                    text = "ID",
                    command = self.toggle_id_input,
                    variable = self.by_id,
                    bg="#a2dba7",
                    activebackground="#a2dba7",
                    font= ("Verdana", 11)
                    ).grid(row = 3, column = 0, sticky = W, ipadx = 10)

        # 'Tags' check button
        self.by_tags = BooleanVar()
        Checkbutton(self,
                    text = "Tags",
                    command = self.toggle_tags_input,
                    variable = self.by_tags,
                    bg="#a2dba7",
                    activebackground="#a2dba7",
                    font= ("Verdana", 11)
                    ).grid(row = 4, column = 0, sticky = W, ipadx = 10)

        # 'Topic' check button
        self.by_topic = BooleanVar()
        Checkbutton(self,
                    text = "Topic",
                    command = self.toggle_topic_input,
                    variable = self.by_topic,
                    bg="#a2dba7",
                    activebackground="#a2dba7",
                    font= ("Verdana", 11)
                    ).grid(row = 5, column = 0, sticky = W, ipadx = 10)

        # 'Source' check button
        self.by_source = BooleanVar()
        Checkbutton(self,
                    text = "Source",
                    command = self.toggle_source_input,
                    variable = self.by_source,
                    bg="#a2dba7",
                    activebackground="#a2dba7",
                    font= ("Verdana", 11)
                    ).grid(row = 6, column = 0, sticky = W, ipadx = 10)

        # 'Date' range button
        self.by_date = BooleanVar()
        Checkbutton(self,
                    text = "Date",
                    command = self.toggle_date_input,
                    variable = self.by_date,
                    bg="#a2dba7",
                    activebackground="#a2dba7",
                    font= ("Verdana", 11)
                    ).grid(row = 7, column = 0, sticky = W, ipadx = 10)

        # 'Difficulty' range button
        self.by_difficulty = BooleanVar()
        Checkbutton(self,
                    text = "Difficulty",
                    command = self.toggle_difficulty_input,
                    variable = self.by_difficulty,
                    bg="#a2dba7",
                    activebackground="#a2dba7",
                    font= ("Verdana", 11)
                    ).grid(row = 10, column = 0, sticky = W, ipadx = 10)

        # 'Mentioned Words' check button
        self.by_words = BooleanVar()
        Checkbutton(self,
                    text = "Mentioned Words",
                    command = self.toggle_words_input,
                    variable = self.by_words,
                    bg="#a2dba7",
                    activebackground="#a2dba7",
                    font= ("Verdana", 11)
                    ).grid(row = 13, column = 0, sticky = W, ipadx = 10)

        # Expanded view check button
        self.expanded_view = BooleanVar()
        Checkbutton(self,
                    text = "Expanded view",
                    command = self.alter_results,
                    variable = self.expanded_view,
                    bg="#a2dba7",
                    activebackground="#a2dba7",
                    font= ("Verdana", 11)
                    ).grid(row = 14, column = 2, sticky = E, ipadx = 25)

        # Button to list items
        self.bttn2 = Button(self, text = "Search", font= ("Verdana", 11),
                            command = self.get_items, width = 15)
        self.bttn2.grid(row = 14, column = 1, pady = 10)

        # 'Items' label
        #Label(self, text = "Items", bg="#a2dba7",
        #      font= ("Verdana", 11)).grid(row = 15, column = 1, pady = 10)

        # Items text box
        self.results_txt = Text(self, width = 65,
                                height = 20, wrap = WORD,
                                font= ("Verdana", 9))
        self.results_txt.grid(row = 15, column = 0, columnspan = 3)

    def alter_results(self):
        if (self.has_been_executed):
            self.get_items()

    def toggle_id_input(self):
        if (self.by_id.get()):
            self.id_input = Entry(self, font= ("Verdana", 11))
            self.id_input.grid(row = 3, column = 1, sticky = W)
        elif (hasattr(self, 'id_input')):
            self.id_input.grid_remove()
            self.reset_id_warning()

    def toggle_tags_input(self):
        if (self.by_tags.get()):
            self.tags_input = Entry(self, font= ("Verdana", 11))
            self.tags_input.grid(row = 4, column = 1, sticky = W)
        elif (hasattr(self, 'tags_input')):
            self.tags_input.grid_remove()

    def toggle_topic_input(self):
        if (self.by_topic.get()):
            self.topic_input = Entry(self, font= ("Verdana", 11))
            self.topic_input.grid(row = 5, column = 1, sticky = W)
        elif (hasattr(self, 'topic_input')):
            self.topic_input.grid_remove()

    def toggle_source_input(self):
        if (self.by_source.get()):
            self.source_input = Entry(self, font= ("Verdana", 11))
            self.source_input.grid(row = 6, column = 1, sticky = W)
        elif (hasattr(self, 'source_input')):
            self.source_input.grid_remove()

    def toggle_date_input(self):
        if (self.by_date.get()):
            self.start_date_lbl = Label(self, text = "Start Date", bg="#a2dba7",
                                        font= ("Verdana", 11))
            self.start_date_lbl.grid(row = 8, column = 0, sticky = W,
                                     ipadx = 25)
            self.start_date_input = Entry(self, font= ("Verdana", 11))
            self.start_date_input.grid(row = 8, column = 1, sticky = W,
                                       pady = 3)
            self.end_date_lbl = Label(self, text = "End Date", bg="#a2dba7",
                                      font= ("Verdana", 11))
            self.end_date_lbl.grid(row = 9, column = 0, sticky = W,
                                   ipadx = 25)
            self.end_date_input = Entry(self, font= ("Verdana", 11))
            self.end_date_input.grid(row = 9, column = 1, sticky = W, pady = 3)
        elif (hasattr(self, 'start_date_input')):
            self.start_date_lbl.grid_remove()
            self.start_date_input.grid_remove()
            self.end_date_lbl.grid_remove()
            self.end_date_input.grid_remove()
            self.reset_date_warning_start()
            self.reset_date_warning_end()
            self.reset_date_warning_chrono()


    def toggle_difficulty_input(self):
        if (self.by_difficulty.get()):
            self.check_easy = BooleanVar()
            self.check_medium = BooleanVar()
            self.check_hard = BooleanVar()
            self.check_no_rank = BooleanVar()
            self.button_easy = Checkbutton(self, text = "Easy", bg="#a2dba7",
                                           variable = self.check_easy,
                                           font= ("Verdana", 11),
                                           activebackground="#a2dba7")
            self.button_easy.grid(row = 11, column = 0, ipadx = 25, sticky = W)
            self.button_medium = Checkbutton(self, text = "Medium",
                                             bg="#a2dba7",
                                             variable = self.check_medium,
                                             font= ("Verdana", 11),
                                             activebackground="#a2dba7")
            self.button_medium.grid(row = 11, column = 1)
            self.button_hard = Checkbutton(self, text = "Hard",
                                           bg="#a2dba7",
                                           variable = self.check_hard,
                                           font= ("Verdana", 11),
                                           activebackground="#a2dba7")
            self.button_hard.grid(row = 11, column = 2)
            self.button_no_rank = Checkbutton(self, text = "No Rank",
                                              bg="#a2dba7",
                                              variable = self.check_no_rank,
                                              font= ("Verdana", 11),
                                              activebackground="#a2dba7")
            self.button_no_rank.grid(row = 12, column = 0, ipadx = 25,
                                     sticky = W)
        elif (hasattr(self, 'button_easy')):
            self.button_easy.grid_remove()
            self.button_medium.grid_remove()
            self.button_hard.grid_remove()
            self.button_no_rank.grid_remove()


    def toggle_words_input(self):
        if (self.by_words.get()):
            self.words_input = Entry(self, font= ("Verdana", 11))
            self.words_input.grid(row = 13, column = 1, sticky = W)
        elif (hasattr(self, 'words_input')):
            self.words_input.grid_remove()


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
            return False


    # remove any leading or trailing white space from word_string and then
    # split the remaining string into a list of words delimited by spaces
    @staticmethod
    def split_words(word_string):
        left = 0
        while ((left < len(word_string)) and (word_string[left] == ' ')):
            left += 1
        word_string = word_string[left:]
        right = len(word_string) - 1
        while ((right >= 0) and (word_string[right] == ' ')):
            right -= 1
        word_string = word_string[:(right+1)]
        return word_string.split(' ')


    # return whether the DataEntry object obj matches contains any of the words
    # in word_string within its statements (with or without latex), solutions
    # (also with or without latex), or notes
    @staticmethod
    def data_match_words(obj, word_string):
        word_list = SearchPage.split_words(word_string)
        stnl = obj.get_stnl()
        stwl = obj.get_stwl()
        sonl = obj.get_sonl()
        sowl = obj.get_sowl()
        notes = obj.get_notes()
        for word in word_list:
            if word in stnl:
                return True
            elif word in stwl:
                return True
            elif word in sonl:
                return True
            elif word in sowl:
                return True
            elif word in notes:
                return True
        return False
        

    # return list containing objects matching the query;
    # assumes that if ID box is checked, then the given ID is valid (possibly
    # '') and likewise for date values
    def filter_query(self, ref):
        mod_ref = ref
        if (self.by_id.get() and (self.id_input.get() != '')):
            mod_ref = [mod_ref[int(self.id_input.get())]]
        if (self.by_tags.get() and (self.tags_input.get() != '')):
            tag_string = DE.DataEntry.tagify(self.tags_input.get())
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
        if self.by_words.get():
            mod_ref = list(filter(lambda x: SearchPage.data_match_words(x, self.words_input.get()),
                                  mod_ref))
        return mod_ref


    # reset id red label warning so that it is not visible
    def reset_id_warning(self):
        if (self.id_warning):
            self.id_warning = False
            self.id_warning_lbl.grid_remove()

    def reset_date_warning_start(self):
        if (self.date_warning_start):
            self.date_warning_start = False
            self.date_warning_lbl_start.grid_remove()

    def reset_date_warning_end(self):
        if (self.date_warning_end):
            self.date_warning_end = False
            self.date_warning_lbl_end.grid_remove()

    def reset_date_warning_chrono(self):
        if (self.date_warning_chrono):
            self.date_warning_chrono = False
            self.date_warning_lbl_chrono.grid_remove()


    # list items matching the query or highlight errors in input
    def get_items(self):
        self.reset_id_warning()
        self.reset_date_warning_start()
        self.reset_date_warning_end()
        self.reset_date_warning_chrono()
        if (self.by_id.get() and (self.id_input.get() != '') and
            (not DE.DataEntry.check_for_int(self.id_input.get()))):
            if not (self.id_warning):
                self.id_warning = True
                self.id_warning_lbl = Label(self,
                                            text = "ID must be integer",
                                            fg="red")
                self.id_warning_lbl.grid(row = 3, column = 2)
        elif (self.by_date.get() and ((not DE.DataEntry.is_valid_date(self.start_date_input.get())) or (self.start_date_input.get() == ''))):
            if (not (self.date_warning_start)):
                self.date_warning_start = True
                self.date_warning_lbl_start = Label(self,
                                                    text = "Start date must be valid",
                                                    fg="red")
                self.date_warning_lbl_start.grid(row = 7, column = 1)
        elif (self.by_date.get() and ((not DE.DataEntry.is_valid_date(self.end_date_input.get())) or (self.end_date_input.get() == ''))):
            if (not (self.date_warning_end)):
                self.date_warning_end = True
                self.date_warning_lbl_end = Label(self,
                                                  text = "End date must be valid",
                                                  fg="red")
                self.date_warning_lbl_end.grid(row = 7, column = 1)
        elif (self.by_date.get() and
              (not SearchPage.order_dates(self.start_date_input.get(), self.end_date_input.get()))):
            if (not (self.date_warning_chrono)):
                self.date_warning_chrono = True
                self.date_warning_lbl_chrono = Label(self,
                                                     text = "Dates must be ordered",
                                                     fg="red")
                self.date_warning_lbl_chrono.grid(row = 7, column = 1)
        else:
            with open('resources.json', 'r') as f:
                ref_dict = json.load(f)
            ref = [DE.DataEntry.from_dict(entry) for entry in ref_dict]
            if ((self.by_id.get()) and (self.id_input.get() != '') and
                (int(self.id_input.get()) >= len(ref))):
                self.id_warning = True
                self.id_warning_lbl = Label(self,
                                            text = "ID must be in range",
                                            fg="red")
                self.id_warning_lbl.grid(row = 3, column = 2)
            else:
                ref_mod = SearchPage.filter_query(self, ref)
                message = ''
                if (len(ref_mod) == 0):
                    message += 'No entries matched your query.\n\nTry '
                    message += 'expanding your search and note that the text '
                    message += 'fields above are case-sensitive.'
                else:
                    message += 'Results: ' + str(len(ref_mod)) + '\n\n\n'
                for entry in ref_mod:
                    message += DE.DataEntry.search_rep(entry,
                                                       self.expanded_view.get())
                    message += '\n\n\n'
                self.results_txt.delete(0.0, END)
                self.results_txt.insert(0.0, message)
                self.has_been_executed = True


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
        self.has_been_executed = False
