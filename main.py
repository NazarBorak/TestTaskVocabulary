from tkinter import Tk, Label, Frame, Button, Entry, Listbox, END, messagebox


class Vocabulary:
    TITLE = 'VOCABULARY'
    RED_LABEL = 'red'
    BUTTON_BORDER_BACKGROUND_COLOR = 'grey'
    BUTTON_BORDER_THICKNESS = 3
    HEADERS_COLOR = '#f5d72c'
    GREEN_STATUS_COLOR = '#75e864'
    RED_STATUS_COLOR = '#e86464'
    vocabulary_list = []
    COUNT_OF_SHOWN_WORDS = 10
    BAD_REQUEST = 400
    U_ARE_TEAPOT = 418
    CREATED = 201
    FONT = ('Abril Fatface', 20)

    def __init__(self, master):
        self.root = master
        # FRAMES SECTION
        self.frame_for_rules = Frame(self.root, width=1000, height=50, bg='#75e091')
        self.frame_for_add = Frame(self.root, width=1000, height=150, bg='#9775e0')
        self.frame_for_replace = Frame(self.root, width=1000, height=150, bg='#e38f5b')
        self.frame_for_showing_words_and_num_of_letters = Frame(self.root, width=1000, height=800, bg='#e35b5b')

        # SECTION LABELS
        self.add_section_label = Label(self.frame_for_add, text='Add word section', bg=self.HEADERS_COLOR,
                                       font=self.FONT, borderwidth=1, relief='solid')
        self.replace_section_label = Label(self.frame_for_replace, text='Replace word section', bg=self.HEADERS_COLOR,
                                           font=self.FONT, borderwidth=1, relief='solid')
        self.finding_section_label = Label(self.frame_for_showing_words_and_num_of_letters,
                                           text='Finding words with exact letters section', bg=self.HEADERS_COLOR,
                                           font=self.FONT, borderwidth=1, relief='solid')

        # RULES SECTION
        self.rules_button = Button(self.frame_for_rules, text='RULES', command=lambda: self.rules_pop_out(),
                                   font=self.FONT, highlightthickness=self.BUTTON_BORDER_THICKNESS,
                                   highlightbackground='grey', )

        # ADD SECTION
        self.add_enter_field = Entry(self.frame_for_add, highlightthickness=0)
        self.add_button = Button(self.frame_for_add, text='Add word', highlightthickness=self.BUTTON_BORDER_THICKNESS,
                                 highlightbackground='grey',
                                 command=lambda: self.add_word_in_vocabulary())

        self.add_status_label = Label(self.frame_for_add,
                                      text='Status: Nothing was added. Word must contain only alphabetic symbols and '
                                           'be without spaces.\n NOTE: words Example and example are same, so you '
                                           'can\'t add both', borderwidth=1, relief='solid')

        # REPLACE SECTION
        self.replace_label = Label(self.frame_for_replace, text='Replace', borderwidth=1, relief='solid')
        self.enter_field_after_replace_label = Entry(self.frame_for_replace, highlightthickness=0)
        self.with_label = Label(self.frame_for_replace, text='with', borderwidth=1, relief='solid')
        self.enter_field_after_with_label = Entry(self.frame_for_replace, highlightthickness=0)
        self.replace_button = Button(self.frame_for_replace, text='Replace word',
                                     highlightthickness=self.BUTTON_BORDER_THICKNESS, highlightbackground='grey',
                                     command=lambda: self.replace_word_with_another())

        self.replace_status_label = Label(self.frame_for_replace, text='Status: Nothing was replaced', borderwidth=1,
                                          relief='solid')

        # FINDING WORDS AND SHOWING NUMBERS SECTION
        self.enter_letter_s_label = Label(self.frame_for_showing_words_and_num_of_letters, text='Enter letter(-s)',
                                          borderwidth=1, relief='solid')
        self.enter_field_for_entered_letter = Entry(self.frame_for_showing_words_and_num_of_letters,
                                                    highlightthickness=0)

        self.find_and_show_letter_and_its_number_button = Button(self.frame_for_showing_words_and_num_of_letters,
                                                                 text='Find and show exact number of words that contain'
                                                                      ' provided letters: ',
                                                                 highlightthickness=self.BUTTON_BORDER_THICKNESS,
                                                                 highlightbackground='grey',
                                                                 command=lambda: self.find_and_show_number())
        self.find_and_show_letter_and_its_number_label = Label(self.frame_for_showing_words_and_num_of_letters,
                                                               text='0', borderwidth=1, relief='solid')

        self.generator_button = Button(self.frame_for_showing_words_and_num_of_letters,
                                       text='Show words that contain provided letters: ',
                                       highlightthickness=self.BUTTON_BORDER_THICKNESS,
                                       highlightbackground='grey',
                                       command=lambda: self.show_up_to_ten_words())
        self.listbox_for_generated_words = Listbox(self.frame_for_showing_words_and_num_of_letters, height=20)

        self.show_all_vocabulary = Button(self.frame_for_showing_words_and_num_of_letters, text='Show vocabulary: ',
                                          highlightthickness=self.BUTTON_BORDER_THICKNESS, highlightbackground='grey',
                                          command=lambda: self.show_vocabulary())
        self.listbox_for_all_vocabulary = Listbox(self.frame_for_showing_words_and_num_of_letters, height=20)

        self.placement()


    def placement(self):
        self.root.title(self.TITLE)
        self.root.geometry('1000x1080')
        self.root.resizable(width=False, height=False)

        # FRAMES
        self.frame_for_rules.place(x=1, y=1)
        self.frame_for_add.place(x=1, y=51)
        self.frame_for_replace.place(x=1, y=201)
        self.frame_for_showing_words_and_num_of_letters.place(x=1, y=351)

        # SECTION LABELS
        self.add_section_label.place(x=410, y=5)
        self.replace_section_label.place(x=388, y=5)
        self.finding_section_label.place(x=300, y=5)

        # RULES SECTION
        self.rules_button.place(x=460, y=8)

        # ADD SECTION
        self.add_enter_field.place(x=10, y=50)
        self.add_button.place(x=220, y=50)

        self.add_status_label.place(x=10, y=90)

        # REPLACE SECTION
        self.replace_label.place(x=10, y=70)
        self.enter_field_after_replace_label.place(x=90, y=70)
        self.with_label.place(x=300, y=70)
        self.enter_field_after_with_label.place(x=350, y=70)
        self.replace_button.place(x=550, y=70)

        self.replace_status_label.place(x=10, y=110)

        # FINDING WORDS AND SHOWING NUMBERS SECTION
        self.enter_letter_s_label.place(x=10, y=70)
        self.enter_field_for_entered_letter.place(x=130, y=70)

        self.find_and_show_letter_and_its_number_button.place(x=10, y=130)
        self.find_and_show_letter_and_its_number_label.place(x=500, y=130)

        self.generator_button.place(x=10, y=180)
        self.listbox_for_generated_words.place(x=50, y=210)

        self.show_all_vocabulary.place(x=385, y=180)
        self.listbox_for_all_vocabulary.place(x=370, y=210)

    def add_word_in_vocabulary(self):
        lowercase_list = [x.lower() for x in self.vocabulary_list]
        if ' ' in self.add_enter_field.get() or self.add_enter_field.get() == '':
            self.add_status_label.config(text=f'{self.BAD_REQUEST}, You can\'t enter a word with space in it',
                                         background=self.RED_STATUS_COLOR)
        elif self.add_enter_field.get() == f'{self.U_ARE_TEAPOT}':
            self.add_status_label.config(text='YOU ARE A TEAPOT, GOTCHA :D', background=self.RED_STATUS_COLOR)
        elif not self.add_enter_field.get().isalpha():
            self.add_status_label.config(text=f'{self.BAD_REQUEST}, Word must contain only alphabetic symbols',
                                         background=self.RED_STATUS_COLOR)
        elif self.add_enter_field.get().lower() in lowercase_list:
            self.add_status_label.config(text=f'{self.BAD_REQUEST}, Already exists', background=self.RED_STATUS_COLOR)
        else:
            self.add_status_label.config(text=f'{self.CREATED}, Created', background=self.GREEN_STATUS_COLOR)
            self.vocabulary_list.append(self.add_enter_field.get())
        self.add_enter_field.delete(0, END)

    def replace_word_with_another(self):
        replace_enter_field = self.enter_field_after_replace_label.get()
        with_enter_field = self.enter_field_after_with_label.get()
        if ((' ' in replace_enter_field) or (not replace_enter_field)) or (
                (' ' in with_enter_field) or (not with_enter_field)):
            self.replace_status_label.config(
                text=f'{self.BAD_REQUEST}: Replace is not allowed - You entered space symbol or nothing into one of '
                     'enter fields.Try again', background=self.RED_STATUS_COLOR)
        elif replace_enter_field not in self.vocabulary_list or with_enter_field in self.vocabulary_list:
            self.replace_status_label.config(
                text=f'{self.BAD_REQUEST}: Nothing was replaced - "Word to replace" is Not in vocabulary list or\n'
                     '"word to be replaced" already exists in vocabulary.Try again', background=self.RED_STATUS_COLOR)
        elif (replace_enter_field not in self.vocabulary_list) and (with_enter_field in self.vocabulary_list):
            self.replace_status_label.config(text=f'{self.BAD_REQUEST}: One of these words already',
                                             background=self.RED_STATUS_COLOR)
        elif (replace_enter_field in self.vocabulary_list) and (with_enter_field not in self.vocabulary_list):
            self.replace_status_label.config(text=f'{self.CREATED}: Word was replaced!!!',
                                             background=self.GREEN_STATUS_COLOR)
            self.vocabulary_list[self.vocabulary_list.index(replace_enter_field)] = with_enter_field

    def find_and_show_number(self):
        temp = []
        inp = ''.join(sorted(list(self.enter_field_for_entered_letter.get())))
        for x in self.vocabulary_list:
            compare = x
            empty_str = ''
            counter = 0
            for y in inp:
                if y in compare:
                    empty_str += y
                    compare = compare.replace(y, '', 1)
                if counter == (len(inp) - 1):
                    empty_str = ''.join(sorted(list(empty_str)))
                    if inp == empty_str:
                        temp.append(x)
                counter += 1
        self.find_and_show_letter_and_its_number_label.config(text=f'{inp} | {len(temp)}')
        return temp

    def show_up_to_ten_words(self):
        try:
            self.listbox_for_generated_words.delete(0, END)
            new_temp = (x for x in self.find_and_show_number())
            for y in range(self.COUNT_OF_SHOWN_WORDS):
                self.listbox_for_generated_words.insert(END, next(new_temp))
            self.COUNT_OF_SHOWN_WORDS += 10
        except StopIteration:
            pass

    def show_vocabulary(self):
        self.listbox_for_all_vocabulary.delete(0, END)
        for x in self.vocabulary_list:
            self.listbox_for_all_vocabulary.insert(END, x)

    @staticmethod
    def rules_pop_out():
        messagebox.showinfo('RULES',
                            'BEFORE READING THESE RULES, YOU MUST READ READFILE. \n\nWORD MUST:\n1. '
                            'Contain only alphabetic symbols.\n2. Be without spaces. \n3. Be unique'
                            '(words Example and example are same)')


if __name__ == '__main__':
    root = Tk()
    Vocabulary(root)
    root.mainloop()
