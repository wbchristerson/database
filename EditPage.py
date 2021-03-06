from tkinter import *
import WritePage as WP
import DataEntry as DE
import json

class EditPage(Frame):
    """ Edit an entry based on the ID """
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.config(bg="#fafccf")
        self.grid_columnconfigure(1, weight=1)
        self.grid()
        self.set_format(controller)
        self.curr_id = -1
        self.warning_id = False # whether message about invalid id is visible
        # whether message about invalid date is visible:
        self.warning_date = False

    def set_format(self, controller):
        # Page title
        lbl = Label(self, text = "Edit An Entry", font= ("Verdana", 14),
                    bg="#fafccf")
        lbl.grid(row = 0, column = 1, sticky = W, padx = (70,0), pady = 5)
        
        # Menu return button
        self.bttn1 = Button(self, text = "Return To Menu",
                            command=lambda: controller.return_home(),
                            width = 15, font = ("Verdana", 11))
        self.bttn1.grid(row = 1,column = 1, sticky = W, padx = (60,0),
                        pady = (0,5))

        # 'ID' label
        Label(self, text = "ID", bg="#fafccf",
              font = ("Verdana", 11)).grid(row = 2, column = 0, sticky = W,
                                           padx = 10, pady = (0,20))

        # ID input entry
        self.id_input = Entry(self, font = ("Verdana", 11))
        self.id_input.grid(row = 2, column = 1, sticky = W, padx = (32,0),
                           pady = (0,20))

        # Entry display button
        self.bttn2 = Button(self, text = "Edit",
                            command=self.populate_by_id, width = 10,
                            font = ("Verdana", 11))
        self.bttn2.grid(row = 2,column = 2, sticky = W, padx = 10,
                        pady = (0,20))

        # Set page format similarly to write page
        WP.WritePage.set_format(self,controller, 3)

        # Alter coloration of page from default given by edit page
        self.tag_lbl.config(bg="#fafccf")
        self.tags_input.grid(padx = (32,0), pady = 2)
        self.topic_lbl.config(bg="#fafccf")
        self.topic_input.grid(padx = (32,0), pady = 2)
        self.source_lbl.config(bg="#fafccf")
        self.source_input.grid(padx = (32,0), pady = 2)
        self.date_lbl.config(bg="#fafccf")
        self.date_input.grid(padx = (32,0), pady = 2)
        self.difficulty_lbl.config(bg="#fafccf")
        self.rb_easy.config(bg="#fafccf", activebackground="#fafccf")
        self.rb_easy.grid(padx = (0,120))
        self.rb_medium.config(bg="#fafccf", activebackground="#fafccf")
        self.rb_hard.config(bg="#fafccf", activebackground="#fafccf")
        self.rb_hard.grid(padx = (0,120))
        self.rb_no_rank.config(bg="#fafccf", activebackground="#fafccf")
        self.stnl_lbl.config(bg="#fafccf")
        self.stwl_lbl.config(bg="#fafccf")
        self.sonl_lbl.config(bg="#fafccf")
        self.sowl_lbl.config(bg="#fafccf")
        self.notes_lbl.config(bg="#fafccf")

        self.stnl_lbl.grid(pady = (0,2))
        self.stwl_lbl.grid(pady = (0,2))
        
        # Save button
        self.bttn3 = Button(self, text = "Save",
                            command=lambda: self.update_entry(controller),
                            width = 15, font = ("Verdana", 11))
        self.bttn3.grid(row = 14,column = 1, sticky = E)

        # Cancel button
        self.bttn4 = Button(self, text = "Cancel",
                            command=lambda: controller.return_home(),
                            width = 15, font = ("Verdana", 11))
        self.bttn4.grid(row = 15,column = 1, sticky = E)


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


    def populate_by_id(self):
        if (self.warning_id):
            self.warning_id = False
            self.red_id.grid_remove()
        if (self.warning_date):
            self.warning_date = False
            self.red_date.grid_remove()
        rec_id = self.id_input.get()
        if (DE.DataEntry.check_for_int(rec_id)):
            with open('resources.json', 'r') as f:
                ref_dict = json.load(f)
            ref = [DE.DataEntry.from_dict(entry) for entry in ref_dict]
            int_id = int(rec_id)
            if ((int_id >= len(ref_dict)) or (int_id < 0)):
                if (self.warning_id):
                    self.warning_id = False
                    self.red_id.grid_remove()
                self.red_id = Label(self, text = "ID must be in range",
                                    fg="red")
                self.red_id.grid(row = 1, column = 2, sticky = W, padx = 10)
                self.warning_id = True
            else:
                self.clear()
                self.curr_id = int_id
                self.id_input.insert(0, rec_id)
                tag_str = DE.DataEntry.detagify(ref[int_id].get_tags())
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
            if (self.warning_id):
                self.warning_id = False
                self.red_id.grid_remove()
            self.red_id = Label(self, text = "ID must be integer",fg="red")
            self.red_id.grid(row = 1, column = 2, sticky = W, padx = 10)
            self.warning_id = True

    def update_entry(self, controller):
        if ((not (DE.DataEntry.is_valid_date(self.date_input.get()))) and
            (self.curr_id != -1)):
            if not (self.warning_date):
                self.warning_date = True
                self.red_date = Label(self, text = "Must be valid date",
                                      fg="red")
                self.red_date.grid(row = 1, column = 2)
        else:
            if (self.curr_id != -1):
                with open('resources.json', 'r') as f:
                    ref_dict = json.load(f)
                ref = [DE.DataEntry.from_dict(entry) for entry in ref_dict]      
            
                tags_str = DE.DataEntry.tagify(self.tags_input.get())
                ref[self.curr_id].set_tags(tags_str)
                ref[self.curr_id].set_topic(self.topic_input.get())
                ref[self.curr_id].set_source(self.source_input.get())
                ref[self.curr_id].set_date(self.date_input.get())
                diff_str = DE.DataEntry.ret_difficulty(self.difficulty.get())
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
            
            controller.return_home()
