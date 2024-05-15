from tkinter import *
import tkinter.filedialog

root = Tk()

text=Text(root)
text.grid()
"""
    Documentar as linhas do código para eu entender o que está acontecendo
"""
def saveAs():
    global text
    t = text.get("1.0", "end-1c")
    saveLocation=tkinter.filedialog.asksaveasfilename()
    file1 = open(saveLocation, "w+")
    file1.write(t)
    file1.close()

button = Button(root, text="Save", command=saveAs)
button.grid()

def fontHelvetica():
    global text

    text.config(font="Helvetica")

def fontCourier():
    global text
    text.config(font="Courier")

font=Menubutton(root, text="Font")
font.grid()
font.menu=Menu(font, tearoff=0)
font["menu"]=font.menu
helvetica=IntVar()
courier=IntVar()
font.menu.add_checkbutton(label="Courier", variable=courier, command=fontCourier)
font.menu.add_checkbutton(label="Helvetica", variable=helvetica, command=fontHelvetica)

root.mainloop()