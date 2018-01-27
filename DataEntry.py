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

    @staticmethod
    def check_for_int(s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    @staticmethod
    def ret_difficulty(diff):
        if ((diff == 'easy') or (diff == 'medium') or (diff == 'hard') or
            (diff == 'no rank')):
            return diff
        return 'no rank'

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

    # check whether date string is valid; a valid string is '' or a string of
    # the form 'MM/DD/YYYY' where (MM,DD) is a valid month-day pair
    @staticmethod
    def is_valid_date(ds):
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
        elif not ((DataEntry.check_for_int(ds[0:2])) and
                  (DataEntry.check_for_int(ds[3:5])) and
                  (DataEntry.check_for_int(ds[6:]))):
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
        message += 'Date: ' + self.date + '\n\n'
        message += 'Statement (No LaTeX): ' + self.stnl + '\n\n'
        message += 'Statement (With LaTeX): ' + self.stwl + '\n\n'
        message += 'Difficulty: ' + self.difficulty + '\n\n'
        message += 'Solution (No LaTeX): ' + self.sonl + '\n\n'
        message += 'Solution (With LaTeX): ' + self.sowl + '\n\n'
        message += 'Notes: ' + self.notes + '\n\n\n'
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
