from tkinter import *
from tkinter import ttk
import time
import tkinter

import greet
import scrape
import automation


def start_control_center():
    ControlCenter()


class ControlCenter:
    def __init__(self):
        self.control_center = Tk()
        self.control_center.title("Python Controll-Center")

        # Frame
        mainframe = ttk.Frame(self.control_center, padding="5")
        mainframe.grid(column=0, row=0)
        # Button - Description
        btn_greet_simple = ttk.Button(mainframe, text='Terminal sagt Hallo (Simple)',
                                      command=self.call_simple_greet)
        lbl_greet_simple = ttk.Label(
            mainframe, text='Einfacher Gruß im Terminal')

        btn_greet = ttk.Button(mainframe, text='Terminal sagt Hallo',
                               command=self.call_greet)
        lbl_greet = ttk.Label(
            mainframe, text='Terminal grüßt Input-Name')

        btn_scrape_hacker_news = ttk.Button(
            mainframe, text='Scrape Hacker News', command=self.call_scrape)
        lbl_scrape_hacker_news = ttk.Label(
            mainframe, text='Top Votings der Seite Hacker News\nwerden im Terminal ausgegeben')

        btn_automation_test = ttk.Button(
            mainframe, text='Test Selenium', command=self.call_automation_test)
        lbl_automation_test = ttk.Label(
            mainframe, text='Selenium/Automation testen')

        btn_quit = ttk.Button(mainframe, text='Beenden',
                              command=self.destroy_control_center)

        # Widget Positions
        btn_quit.grid(column=0, row=100)
        btn_scrape_hacker_news.grid(column=0, row=0)
        lbl_scrape_hacker_news.grid(column=1, row=0)

        btn_automation_test.grid(column=0, row=1)
        lbl_automation_test.grid(column=1, row=1)

        btn_greet_simple.grid(column=2, row=0)
        lbl_greet_simple.grid(column=4, row=0)

        btn_greet.grid(column=2, row=1)
        lbl_greet.grid(column=4, row=1)

        btn_quit.grid(column=0, row=1000)

        for window_child in self.control_center.winfo_children():
            window_child.grid_configure(padx=5, pady=5)
            if window_child.winfo_class() == 'TFrame':
                for frame_child in window_child.winfo_children():
                    frame_child.grid_configure(
                        padx=5, pady=5)
                    frame_child.grid(sticky=W+N+S)

        self.control_center.attributes('-alpha', 1)
        self.control_center.minsize(500, 500)
        # self.control_center.maxsize(600, 600)
        self.control_center.bind('<Return>', self.clickWidget)
        self.control_center.mainloop()

    def clickWidget(self, *args):
        widget = self.control_center.focus_get()
        if widget.winfo_class() == 'TButton':
            widget.invoke()
        else:
            print(widget.winfo_class())

    def destroy_control_center(self):
        self.control_center.destroy()

    def call_simple_greet(self):
        greet.simple_greet()

    def call_greet(self):
        window = Toplevel(self.control_center)
        greet.start_gui(window)

    def call_scrape(self):
        scrape.main()

    def call_automation_test(self):
        automation.selenium_test()


start_control_center()
