from tkinter import *

window = Tk()
window.geometry("500x100")

window.config(background = "lightgreen")

def conversion():
    kg = float(wt_value.get())
    gramz = kg * 1000
    poundz = kg * 2.204
    ouncez = kg * 35.274
    gramtext.delete("1.0",END)
    gramtext.insert(END,gramz)
    poundtext.delete("1.0",END)
    poundtext.insert(END,poundz)
    ouncetext.delete("1.0",END)
    ouncetext.insert(END,ouncez)


wt = Label(window,text = "Enter the weight in kg:",font =("Arial",15),fg = "green",background = "beige")
wt_value = Entry(window)
convert = Button(window,text = "Convert",command = conversion)
btn = Button(window,text='Click me !', bd='5',background="cyan")


gram = Label(window,text = "Grams")
pound = Label(window,text = "Pounds")
ounce = Label(window,text = "Ounces")

gramtext = Text(window,height = 1,width = 20,background = "beige")
poundtext = Text(window, height = 1, width = 20)
ouncetext = Text(window,height = 1, width = 20)

wt.grid(row = 0 ,column = 0)
wt_value.grid(row = 0,column = 1)
convert.grid(row = 0,column = 2)

gram.grid(row = 1, column = 0)
pound.grid(row = 1, column = 1)
ounce.grid(row = 1, column = 2)

gramtext.grid(row = 2, column = 0)
poundtext.grid(row = 2, column = 1)
ouncetext.grid(row = 2 , column = 2)

btn.grid(row = 3, column = 1)

window.mainloop()