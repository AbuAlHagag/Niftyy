
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./quest")


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

def reset():
    button_image_2.configure(file=relative_to_assets("button.png"))
    button_image_3.configure(file=relative_to_assets("button.png"))
    button_image_4.configure(file=relative_to_assets("button.png"))
    button_image_5.configure(file=relative_to_assets("button.png"))
    
def select(n):
    if n==5:
        reset()
        button_image_5.configure(file=relative_to_assets("selected.png"))
    if n==2:
        reset()
        button_image_2.configure(file=relative_to_assets("selected.png"))
    if n==3:
        reset()
        button_image_3.configure(file=relative_to_assets("selected.png"))
    if n==4:
        reset()
        button_image_4.configure(file=relative_to_assets("selected.png"))

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=86.0,
    y=571.0,
    width=391.0,
    height=106.0
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    760.0,
    333.0,
    image=image_image_3
)

canvas.create_text(
    662.0,
    87.0,
    anchor="nw",
    text="Game Time",
    fill="#FFFFFF",
    font=("GRANDGALAXY", 27 * -1)
)

canvas.create_text(
    676.0,
    152.0,
    anchor="nw",
    text="Question",
    fill="#FFFFFF",
    font=("GRANDGALAXY", 24 * -1)
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: select(2),
    relief="flat"
)
button_2.place(
    x=575.0,
    y=322.0,
    width=370.0,
    height=77.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: select(3),
    relief="flat"
)
button_3.place(
    x=575.0,
    y=414.0,
    width=370.0,
    height=77.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: select(4),
    relief="flat"
)
button_4.place(
    x=575.0,
    y=506.0,
    width=370.0,
    height=77.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: select(5),
    relief="flat"
)
button_5.place(
    x=575.0,
    y=230.0,
    width=370.0,
    height=77.0
)
window.resizable(False, False)
window.mainloop()
