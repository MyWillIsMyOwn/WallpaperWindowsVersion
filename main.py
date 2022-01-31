from tkinter import *
from tkinter.filedialog import askopenfilename



#getting file path
def get_path():
    filepath = askopenfilename()
    return filepath

#setting wallpaper
def set_wallpaper():
    path = get_path()
    print(path)

#displaying buttons
def display(choice):
    choice = option.get()
    if choice == 'choose a photo':
        browser_button()
    if choice == 'choose a folder':
        choose_a_folder_button()

#button functions
def browser_button():
    choose_a_folder.pack_forget()
    browser.pack()
def choose_a_folder_button():
    browser.pack_forget()
    choose_a_folder.pack()

#window settings
window = Tk()
window.title('Wallpaper')
window.geometry('200x200')
window.resizable(0,0)



#drop down menu settings
options = ['choose a photo', 'choose a folder']
option = StringVar(window)
option.set(options[0])
drop_down_menu = OptionMenu(window, option, *options, command=display)
drop_down_menu.pack()

#creating buttons
browser = Button(window, text='browser',command=set_wallpaper)
browser.pack()
choose_a_folder = Button(window, text='choose a folder',command=get_path)




window.mainloop()
