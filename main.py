import os
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from os import listdir
from os.path import isfile
import ctypes
import re


#choosing a directory
def choose_folder():
    listofphotos = []
    path = filedialog.askdirectory()
    for file in listdir(path):
        if re.search('.jpeg{1}|.jpg{1}',file):
            listofphotos.append(file)
    return listofphotos

def set_random_wallpaper():
    print(choose_folder())


#getting file path
def get_path():
    filepath = askopenfilename()
    return filepath

#setting single wallpaper
def set_wallpaper():
    path = get_path()
    if re.search('.jpeg{1}|.jpg{1}',path):
        ctypes.windll.user32.SystemParametersInfoW(20, 0, path , 0)

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
