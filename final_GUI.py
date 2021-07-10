# FINAL GUI

from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("800x800")
root.maxsize(400, 400)
root.minsize(400, 400)
root.title("Currency Converter")
root.config(bg="#99FFFF")


def clicked():
    if(clicked1.get() == options[0] or clicked2.get() == options[0]):
        messagebox.showinfo("Info", "Please select a valid currency")
    else:
        pass


# Label


Label(root, text="Welcome to Currency Converter",
      border=2, relief=SOLID, bg="indigo", fg="yellow", font="Arial 19 bold").pack()

# Frames

frame1 = LabelFrame(root, text="Select FROM CURRENCY",
                    padx=5, pady=5, background="#FF9933", foreground="navy blue")
frame1.place(x=10, y=100)

frame2 = LabelFrame(root, text="Select TO CURRENCY",
                    padx=5, pady=5, background="#138808", foreground="yellow")
frame2.place(x=265, y=100)

frame3 = LabelFrame(root, text="Enter your Amount here",
                    padx=5, pady=5, background="#CCCCCC", foreground="navy blue")
frame3.place(x=10, y=180)

frame4 = LabelFrame(root, text="Converted Amount",
                    padx=5, pady=5, background="#CCCCCC", foreground="navy blue")
frame4.place(x=263, y=180)

# Manual Entry

a = StringVar(root)
amt = Entry(frame3, justify=CENTER, borderwidth=2).pack()

res = Text(frame4,  borderwidth=2, height=0.9,
           width=13, state=DISABLED).pack()

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
btn1 = Button(root, text="Get Value", fg="#000080",
              bg="white", font=("Italic", 10, "bold"), command=clicked).place(x=172, y=159)

# Exit Button
btn2 = Button(root, text="Exit", font=("Italic", 10, "bold"), command=root.quit,
              width=8).place(x=176, y=300)

root.mainloop()
