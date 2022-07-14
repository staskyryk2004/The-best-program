


def button_press():
    print("Кнопка натиснута")


from tkinter import *
tk = Tk()
b1 = Button(tk, text="Натисни мене", command=button_press)
b1.pack()


