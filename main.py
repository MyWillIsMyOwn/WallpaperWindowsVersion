from tkinter import *
from tkinter.filedialog import askopenfilename



#opening a folder
def openfolder():
    filepath = askopenfilename()
    return filepath



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
browser = Button(window, text='browser',command=openfolder)
browser.pack()
choose_a_folder = Button(window, text='choose a folder',command=openfolder)




window.mainloop()