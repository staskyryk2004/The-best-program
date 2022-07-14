from tkinter import *
tk= Tk()
# Створення змінної canvas
canvas= Canvas(tk, width=500,height=500)
canvas.pack()
# Завантаження зображення
fish_obj = PhotoImage(file="Background.png")
id_img = canvas.create_image(50,50,anchor=NW, image=fish_obj)
print(id_img)
# Анімація картинки
import time
for i in range(1,100):
    canvas.move(id_img,2,0)
    tk.update()
    time.sleep(0.02)

def move_fish(event):
    if event.keysym == 'Up':
        canvas.move(id_img,0,-4)
    elif event.keysym == 'Down':
        canvas.move(id_img,0,4)
    elif event.keysym == 'Left':
        canvas.move(id_img,-4,0)
    elif event.keysym == 'Right':
        canvas.move(id_img,4,0)
        
canvas.bind_all("<KeyPress-Up>",move_fish)
canvas.bind_all("<KeyPress-Down>",move_fish)
canvas.bind_all("<KeyPress-Left>",move_fish)
canvas.bind_all("<KeyPress-Right>",move_fish)
