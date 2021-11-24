from tkinter import *

import tkinter.simpledialog
import tkinter.messagebox
import webbrowser


root = Tk()
root.geometry("700x350")


def callback(url):
   webbrowser.open_new_tab(url)

mylabel = Label(root, text="From Google drive link to working url")

mylabel.pack()

#asking for url
URL = tkinter.simpledialog.askstring("url", "What is the link?")

#take url and make it usable
#from this 
#https://drive.google.com/file/d/1FI1QjxcdBO5B3tNj6n8Z4NL8REOcou2m/view?usp=sharing
#to this 
#https://drive.google.com/uc?export=view&id=1FI1QjxcdBO5B3tNj6n8Z4NL8REOcou2m

URLpart1 = URL.replace("https://drive.google.com/file/d/","https://drive.google.com/uc?export=view&id=")
FinalURL = URLpart1.replace("/view?usp=sharing","")

#output 
output = "This is your new link \n %s" %(FinalURL)

link = Label(root, text=output,font=('Helveticabold', 15), fg="blue", cursor="hand2")
link.pack()
link.bind("<Button-1>", lambda e:
callback('"%s"'%FinalURL))

root.mainloop()