from tkinter import *
from tkinter import ttk
import sys


class ProgForm:

    def __init__(self, root):

        # self.root = Tk()
        self.root = root
        self.entry_input = StringVar()
        self.label_output = StringVar()

        self.root.title('Eingabe')
        self.frame = ttk.Frame(self.root, padding="5")

        # Labels
        self.lbl_desc = ttk.Label(
            self.frame, text='Bitte gib deinen Usernamen ein (Ein String).')

        self.lbl_output = ttk.Label(
            self.frame, textvariable=self.label_output)

        # Entry
        self.user_name_entry = ttk.Entry(
            self.frame, width=20, textvariable=self.entry_input)

        # Buttons
        self.button_next = ttk.Button(
            self.frame, text='Start', command=self.proceed)
        self.button_quit = ttk.Button(
            self.frame, text='Beenden', command=self.end)

        # Positioning
        self.frame.grid(column=0, row=0)
        self.lbl_desc.grid(column=0, row=0)
        self.user_name_entry.grid(column=0, row=1)
        self.button_next.grid(column=0, row=2)
        self.lbl_output.grid(column=0, row=3)
        self.button_quit.grid(column=0, row=5)

        for root_child in self.root.winfo_children():
            root_child.grid_configure(padx=5, pady=5)
            if root_child.winfo_class() == 'TFrame':
                for frame_child in root_child.winfo_children():
                    frame_child.grid_configure(padx=5, pady=5)

        self.root.bind('<Return>', self.clickWidget)
        self.user_name_entry.focus()
        self.root.focus_force()
        self.root.mainloop()
    # def my_focus(self, *args):
    #     button_next.focus()

    def clickWidget(self, *args):
        widget = self.root.focus_get()
        if widget == self.user_name_entry:
            self.button_next.focus()
        elif widget.winfo_class() == 'TButton':
            widget.invoke()
        else:
            print(widget.winfo_class())

    def proceed(self, *args):
        self.label_output.set(f'Hello {self.entry_input.get()}')
        print(self.entry_input.get())
        self.my_function(self.entry_input.get())

    def end(self, *args):
        self.root.destroy()

    def my_function(self, args):
        args_list = args.split(' ')
        print('Hello there')
        print('Here comes my function')
        print(args_list)


def simple_greet():
    print('Hallo Sebastian und Benjamin')


def start_gui(window):
    ProgForm(window)


def main_terminal(args_list):
    print(args_list)
    print('Hello', args_list[1])


if __name__ == '__main__':
    # print(sys.argv)
    if sys.argv[1] == '-gui':
        window = Tk()
        ProgForm(window)
        # ProgForm()
    else:
        main_terminal(sys.argv)
