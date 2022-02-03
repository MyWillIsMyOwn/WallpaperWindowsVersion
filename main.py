import os
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from os import listdir
from os.path import isfile
import random
import ctypes
import re

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
    listofphotos = []
    path = filedialog.askdirectory()
    for file in listdir(path):
        if check_if_correct_file(file):
            listofphotos.append(path+'//'+file)
    return listofphotos

#setting wallpaper
def pick_photo(path):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path , 0)


#choosing random photo
def set_random_wallpaper():
    photo = random.choice(choose_folder())
    pick_photo(photo)

#choosing single photo
def set_wallpaper():
    path = get_path()
    if check_if_correct_file(path):
        pick_photo(path)


#calling a button
def call(choice):
    choice = option.get()
    if choice == 'choose a photo':
        display_browser_button()
    if choice == 'choose a folder':
        display_choose_a_folder_button()

#displaying button
def display_browser_button():
    choose_a_folder_button.pack_forget()
    browser_button.pack()
def display_choose_a_folder_button():
    browser_button.pack_forget()
    choose_a_folder_button.pack()

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

#creating buttons
browser_button = Button(window, text='browser',command=set_wallpaper)
browser_button.pack()
choose_a_folder_button = Button(window, text='choose a folder',command=set_random_wallpaper)

window.mainloop()
