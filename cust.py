
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./cust")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1024x768")
window.configure(bg = "#000000")


canvas = Canvas(
    window,
    bg = "#000000",
    height = 768,
    width = 1024,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    512.0,
    384.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    281.0,
    300.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    760.0,
    333.0,
    image=image_image_3
)
def Reset():
    button_image_1.configure(file=relative_to_assets("button.png"))
    button_image_2.configure(file=relative_to_assets("button.png"))
    button_image_3.configure(file=relative_to_assets("button.png"))
    button_image_4.configure(file=relative_to_assets("button.png"))
    button_image_5.configure(file=relative_to_assets("button.png"))
    button_image_6.configure(file=relative_to_assets("button.png"))
    button_image_7.configure(file=relative_to_assets("button.png"))
    button_image_8.configure(file=relative_to_assets("button.png"))
    button_image_9.configure(file=relative_to_assets("button.png"))

def Select(n):
    if n == 1:
        Reset()
        button_image_1.configure(file=relative_to_assets("Selected.png"))
    if n == 2:
        Reset()
        button_image_2.configure(file=relative_to_assets("Selected.png"))
    if n == 3:
        Reset()
        button_image_3.configure(file=relative_to_assets("Selected.png"))
    if n == 4:
        Reset()
        button_image_4.configure(file=relative_to_assets("Selected.png"))
    if n == 5:
        Reset()
        button_image_5.configure(file=relative_to_assets("Selected.png"))
    if n == 6:
        Reset()
        button_image_6.configure(file=relative_to_assets("Selected.png"))
    if n == 7:
        Reset()
        button_image_7.configure(file=relative_to_assets("Selected.png"))
    if n == 8:
        Reset()
        button_image_8.configure(file=relative_to_assets("Selected.png"))
    if n == 9:
        Reset()
        button_image_9.configure(file=relative_to_assets("Selected.png"))

            
        
    
    
button_image_1 = PhotoImage(
    file=relative_to_assets("button.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Select(1),
    relief="flat"
)
button_1.place(
    x=571.0,
    y=141.0,
    width=116.0,
    height=107.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Select(2),
    relief="flat"
)
button_2.place(
    x=571.0,
    y=267.0,
    width=116.0,
    height=107.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Select(3),
    relief="flat"
)
button_3.place(
    x=571.0,
    y=393.0,
    width=116.0,
    height=107.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Select(4),
    relief="flat"
)
button_4.place(
    x=703.0,
    y=141.0,
    width=116.0,
    height=107.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Select(5),
    relief="flat"
)
button_5.place(
    x=703.0,
    y=267.0,
    width=116.0,
    height=107.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Select(6) ,
    relief="flat"
)
button_6.place(
    x=703.0,
    y=393.0,
    width=116.0,
    height=107.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Select(7),
    relief="flat"
)
button_7.place(
    x=835.0,
    y=141.0,
    width=116.0,
    height=107.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Select(8),
    relief="flat"
)
button_8.place(
    x=835.0,
    y=267.0,
    width=116.0,
    height=107.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Select(9),
    relief="flat"
)
button_9.place(
    x=835.0,
    y=393.0,
    width=116.0,
    height=107.0
)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_10 clicked"),
    relief="flat"
)
button_10.place(
    x=86.0,
    y=571.0,
    width=391.0,
    height=106.0
)
window.resizable(False, False)
window.mainloop()
