# FINAL GUI

from tkinter import *
from typing import Sized

root = Tk()
root.geometry("800x800")
root.maxsize(400, 400)
root.minsize(400, 400)
root.title("Currency Converter")

# Label

Label(root, text="Welcome to Currency Converter",
      border=2, relief=SOLID, bg="indigo", fg="yellow", font="Arial 19 bold").pack()

# Frames

frame1 = LabelFrame(root, text="Select FROM CURRENCY",
                    padx=5, pady=5, background="#F4C430", foreground="navy blue")
frame1.place(x=10, y=100)

frame2 = LabelFrame(root, text="Select TO CURRENCY",
                    padx=5, pady=5, background="green", foreground="yellow")
frame2.place(x=265, y=100)

# Manual Entry

a = float()
amt = Entry(root, justify=CENTER, borderwidth=2,
            textvariable=a, width=23, ).place(x=10, y=190)

res = Text(root,  borderwidth=2, height=0.8,
           width=15, state=DISABLED).place(x=262, y=190)

options = ["...",
           "USD",
           "AUD",
           "CAD",
           "INR"
           ]

clicked1 = StringVar()
clicked2 = StringVar()

clicked1.set(options[0])
clicked2.set(options[0])

# Drop Menu
drop1 = OptionMenu(frame1, clicked1, *options).pack()
drop2 = OptionMenu(frame2, clicked2, *options).pack()

# Conversion Button
btn1 = Button(root, text="Get Value").place(x=178, y=120)

# Exit Button
btn2 = Button(root, text="Exit", command=root.quit,
              width=8).place(x=178, y=250)
root.mainloop()
