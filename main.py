from tkinter import *

FONT = ('Arial', 10, 'bold')


window = Tk()
window.title("Mile To KM Converter")
# window.minsize(height=250, width=50)
window.config(padx=20, pady=20)


# Entry
miles = Entry(width=10)
miles.grid(column=1, row=0)

label = Label(text=" Miles", font=FONT)
label.grid(column=2, row=0)

label1 = Label(text="is equal to", font=FONT)
label1.grid(column=0, row=1)

km = Label(text=0)
km.grid(column=1, row=1)

label2 = Label(text="KM", font=FONT)
label2.grid(column=2, row=1)


def calculate():
    mile = float(miles.get())
    kilometer = mile * 1.609
    km.config(text=kilometer)


button = Button(text='Calculate', command=calculate)
button.grid(column=1, row=2)

window.mainloop()
