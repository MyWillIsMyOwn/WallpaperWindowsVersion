import os
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from os import listdir
import random
import ctypes
import re
from threading import Thread
import time

#getting file path
def get_path():
    filepath = askopenfilename()
    return filepath

#checking file format
def check_if_correct_file(file):
    if re.search('.jpeg{1}|.jpg{1}', file):
        return file

#choosing a directory
def choose_folder():
    return filedialog.askdirectory()

def path(path):
    listofphotos = []
    for file in listdir(path):
        if check_if_correct_file(file):
            listofphotos.append(path+'//'+file)
    return listofphotos

#setting wallpaper
def pick_photo(path):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path , 0)

def swap(swap):
    global flag
    flag = swap

#choosing random photo
def set_random_wallpaper():
    folder = choose_folder()
    swap(False)
    def thread():
        while True:
            if flag:
                break
            global set
            set = random.choice(path(folder))
            pick_photo(set)
            time.sleep(period())
    Thread(target=thread).start()


#choosing single photo
def set_wallpaper():
    path = get_path()
    if check_if_correct_file(path):
        swap(True)
        pick_photo(path)


#calling a button
def call(choice):
    choice = option.get()
    if choice == 'choose a photo':
        display_browser_button()
    if choice == 'choose a folder':
        display_choose_a_folder_button()

#period setting
def period():
    period = choosen_time.get()
    match period:
        case '5s':
            return 5
            swap(True)
        case '15s':
            return 15
            swap(True)
        case '30s':
            return 30
            swap(True)
        case '1min':
            return 60
            swap(True)
        case '15min':
            return 900
            swap(True)
    pick_photo(set)
    swap(False)

#displaying button
def display_browser_button():
    choose_a_folder_button.pack_forget()
    drop_down_times.pack_forget()
    browser_button.pack()
def display_choose_a_folder_button():
    browser_button.pack_forget()
    choose_a_folder_button.pack()
    drop_down_times.pack()

#window settings
window = Tk()
window.title('Wallpaper')
window.geometry('200x200')
window.resizable(0,0)

#drop down menu settings for buttons
options = ['choose a photo', 'choose a folder']
option = StringVar(window)
option.set(options[0])
drop_down_menu = OptionMenu(window, option, *options, command=call)
drop_down_menu.pack()

#drop down menu for timer
times = ['5s','15s','30s','1min','15min']
choosen_time = StringVar(window)
choosen_time.set(times[0])
drop_down_times = OptionMenu(window, choosen_time, *times)

#creating buttons
browser_button = Button(window, text='browser',command=set_wallpaper)
browser_button.pack()
choose_a_folder_button = Button(window, text='browser',command=set_random_wallpaper)

window.mainloop()

