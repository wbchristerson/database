from tkinter import *
import DataEntry as DE
import json

class WritePage(Frame):
#class WritePage(Canvas): #
    """ Add a database entry """
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        #8ab4f7
        #e55b39
        self.config(bg="#dd9f9f")
        self.grid()
        self.set_intro(controller)
        # self.set_format(controller, 2)
        WritePage.set_format(self,controller, 2)
        # Whether message about invalid input is visible
        self.input_warning = False
        # Whether message about invalid date is visible
        self.date_warning = False
        
        # 'Add Entry' button
        self.bttn2 = Button(self, text = "Add Entry",
                            command=lambda: self.save_inputs(controller))
        self.bttn2.grid(row = 13, column = 1)

        # 'Cancel' button
        self.bttn3 = Button(self, text = "Cancel",
                            command=lambda: controller.return_home())
        self.bttn3.grid(row = 13, column = 2)

    def set_intro(self, controller):
        # Page title
        lbl = Label(self, text = "Write Page", font= ("Verdana", 12),
                    bg="#e55b39")
        lbl.grid(row = 0, column = 1)
        
        # Menu return button
        self.bttn1 = Button(self, text = "Return To Menu",
                            command=lambda: controller.return_home())
        self.bttn1.grid(row = 1, column = 1)

    def set_format(self, controller, offset):
        # 'Tags' label
        self.tag_lbl = Label(self, text = "Tags", bg="#e55b39")
        self.tag_lbl.grid(row = offset, column = 0, sticky = W)

        # Tags input entry
        self.tags_input = Entry(self)
        self.tags_input.grid(row = offset, column = 1, sticky = W)

        # 'Topic' label
        self.topic_lbl = Label(self, text = "Topic", bg="#e55b39")
        self.topic_lbl.grid(row = 1 + offset, column = 0, sticky = W)

        # Topic input entry
        self.topic_input = Entry(self)
        self.topic_input.grid(row = 1 + offset, column = 1, sticky = W)

        # 'Source' label
        self.source_lbl = Label(self, text = "Source", bg="#e55b39")
        self.source_lbl.grid(row = 2 + offset, column = 0, sticky = W)

        # Source input entry
        self.source_input = Entry(self)
        self.source_input.grid(row = 2 + offset, column = 1, sticky = W)

        # 'Date' label
        self.date_lbl = Label(self, text = "Date (MM/DD/YYYY)", bg="#e55b39")
        self.date_lbl.grid(row = 3 + offset, column = 0, sticky = W)

        # Date input entry
        self.date_input = Entry(self)
        self.date_input.grid(row = 3 + offset, column = 1, sticky = W)

        # 'Difficulty' label
        self.difficulty_lbl = Label(self, text = "Difficulty", bg="#e55b39")
        self.difficulty_lbl.grid(row = 4 + offset, column = 0, sticky = W)

        # Difficulty radio buttons
        self.difficulty = StringVar()
        self.difficulty.set(None)

        # 'Easy' radio button
        self.rb_easy = Radiobutton(self, text = 'easy',
                                   variable = self.difficulty, value = 'easy',
                                   bg="#e55b39", activebackground="#e55b39")
        self.rb_easy.grid(row = 4 + offset, column = 1, sticky = W)
        
        # 'Medium' radio button
        self.rb_medium = Radiobutton(self, text = 'medium',
                                     variable = self.difficulty,
                                     value = 'medium', bg="#e55b39",
                                     activebackground="#e55b39")
        self.rb_medium.grid(row = 4 + offset, column = 2, sticky = W)

        # 'Hard' radio button
        self.rb_hard = Radiobutton(self, text = 'hard',
                                   variable = self.difficulty, value = 'hard',
                                   bg="#e55b39", activebackground="#e55b39")
        self.rb_hard.grid(row = 4 + offset, column = 3, sticky = W)

        # 'No rank' radio button
        self.rb_no_rank = Radiobutton(self, text = 'no rank',
                                      variable = self.difficulty,
                                      value = 'no rank', bg="#e55b39",
                                      activebackground="#e55b39")
        self.rb_no_rank.grid(row = 4 + offset, column = 4, sticky = W)


        # 'Statement (no latex)' label
        self.stnl_lbl = Label(self, text = "Statement (no latex)", bg="#e55b39")
        self.stnl_lbl.grid(row = 5 + offset, column = 0, sticky = W)

        # Statement (no latex) text box
        self.stnl = Text(self, width = 30, height = 5, wrap = WORD,
                         font= ("Verdana", 9))
        self.stnl.grid(row = 6 + offset, column = 0, columnspan = 3, padx = 10,
                       pady = 10, sticky = W)

        # 'Statement (latex)' label
        self.stwl_lbl = Label(self, text = "Statement (with latex)",
                              bg="#e55b39")
        self.stwl_lbl.grid(row = 5 + offset, column = 3, sticky = W)

        # Statement (latex) text box
        self.stwl = Text(self, width = 30, height = 5, wrap = WORD,
                         font= ("Verdana", 9))
        self.stwl.grid(row = 6 + offset, column = 3, columnspan = 3, padx = 10,
                       pady = 10, sticky = W)

        # 'Solution' (without latex) label
        self.sonl_lbl = Label(self, text = "Solution (no latex)", bg="#e55b39")
        self.sonl_lbl.grid(row = 7 + offset, column = 0, sticky = W)

        # Solution without latex text box
        self.sonl = Text(self, width = 30, height = 5, wrap = WORD,
                         font= ("Verdana", 9))
        self.sonl.grid(row = 8 + offset, column = 0, columnspan = 3, padx = 10,
                       pady = 10, sticky = W)

        # 'Solution' (with latex) label
        self.sowl_lbl = Label(self, text = "Solution (with latex)",
                              bg="#e55b39")
        self.sowl_lbl.grid(row = 7 + offset, column = 3, sticky = W)

        # Solution with latex text box
        self.sowl = Text(self, width = 30, height = 5, wrap = WORD,
                         font= ("Verdana", 9))
        self.sowl.grid(row = 8 + offset, column = 3, columnspan = 3, padx = 10,
                       pady = 10, sticky = W)

        # 'Notes' label
        self.notes_lbl = Label(self, text = "Notes", bg="#e55b39")
        self.notes_lbl.grid(row = 9 + offset, column = 0, sticky = W)

        # Notes text box
        self.notes = Text(self, width = 30, height = 5, wrap = WORD,
                          font= ("Verdana", 9))
        self.notes.grid(row = 10 + offset, column = 0, columnspan = 3,
                        padx = 10, pady = 10, sticky = W)

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


    def save_inputs(self, controller):
        with open('resources.json', 'r') as f:
            ref_dict = json.load(f)
        ref = [DE.DataEntry.from_dict(entry) for entry in ref_dict]
        f.close()

        tags = DE.DataEntry.tagify(self.tags_input.get())
        topic = self.topic_input.get()
        source = self.source_input.get()
        date = self.date_input.get()
        difficulty = DE.DataEntry.ret_difficulty(self.difficulty.get())
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
                self.data_lbl.grid(row = 13, column = 0)

        elif (DE.DataEntry.is_valid_date(date)):
            new_entry = DE.DataEntry(len(ref), tags, topic, source, date,
                                     difficulty, stnl, stwl, sonl, sowl, notes)
            ref.append(new_entry)

            with open('resources.json', 'w') as g:
                ref_dict = [ob.to_dict() for ob in ref]
                json.dump(ref_dict, g)
            g.close()        
            controller.return_home()

        else:
            if (hasattr(self, 'data_lbl') and self.input_warning):
                self.input_warning = False
                self.data_lbl.grid_remove()
            if not (self.date_warning):
                self.date_warning = True
                self.warning_lbl = Label(self, text = "Must be valid date",
                                         fg="red")
                self.warning_lbl.grid(row = 5, column = 2)
