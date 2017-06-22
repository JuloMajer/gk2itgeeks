
from Tkinter import *

root = Tk()
root.geometry("200x100")


label = Label(root, text="Hello Tkinter!")
#label.pack()

def helloPython() :
    label.pack()


button = Button(root,text="Hello python",command=helloPython)
button.pack()



root.mainloop()