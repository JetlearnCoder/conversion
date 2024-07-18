from tkinter import *

window = Tk()
window.geometry("500x100")

window.config(background = "lightgreen")

def conversion():
    temp = float(temp_value.get())
    celcius = temp
    farenheit = (temp * 9/5) + 32
    celciustext.delete("1.0",END)
    celciustext.insert(END,celcius)
    farenheittext.delete("1.0",END)
    farenheittext.insert(END,farenheit)
    
temp = Label(window,text = "Enter the temperature in celcius:",font =("Arial",15),fg = "green",background = "beige")
temp_value = Entry(window)
convert = Button(window,text = "Convert",command = conversion)
btn = Button(window,text='Click me !', bd='5',background="cyan")


celcius = Label(window,text = "celcius")
farenheit = Label(window,text = "farenheit")

celciustext = Text(window,height = 1,width = 20,background = "beige")
farenheittext = Text(window, height = 1, width = 20)

temp.grid(row = 0 ,column = 0)
temp_value.grid(row = 0,column = 1)
convert.grid(row = 0,column = 2)

celcius.grid(row = 1, column = 0)
farenheit.grid(row = 1, column = 1)

celciustext.grid(row = 2, column = 0)
farenheittext.grid(row = 2, column = 1)

btn.grid(row = 3, column = 1)

window.mainloop()