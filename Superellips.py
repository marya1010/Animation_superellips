import tkinter as tk
import math


# функция рисования точки
def drawer(canvas, x, y, a, b):
    x += a
    y += b

    x1 = (x - 1)
    y1 = (y - 1)
    x2 = (x + 1)
    y2 = (y + 1)

    point = canvas.create_oval(x1, y1, x2, y2, fill="red", outline="red")
    points_list.append(point)


# функция сигнум
def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


# функция рисования всего эллипса
def draw_ellips(canvas, n):

    a, b = WIN_W // 2, WIN_H // 2 #центр экрана
    pow = 2 / n
    number_points = 1000 #количество точек
    x_coord = [] # список х координат точек
    y_coord = [] # список у координат точек
    t = 0
    for i in range(number_points + 1):
        x = (abs((math.cos(t))) ** pow) * a * sign(math.cos(t))
        y = (abs((math.sin(t))) ** pow) * b * sign(math.sin(t))
        x_coord.append(x)
        y_coord.append(y)
        t += (math.pi * 2) / number_points

    #рисуем все полученные точки
    for i in range(len(x_coord)):
        drawer(canvas, x_coord[i], y_coord[i], a, b)

#слайдер
def slider(number):
    # Удаляем предыдущие точки, если они есть
    if len(points_list) != 0:
        for point in points_list:
            canvas.delete(point)
    # Отрисовываем эллипс
    draw_ellips(canvas, float(number))


WIN_W = 400
WIN_H = 400
root = tk.Tk()
canvas = tk.Canvas(root, width=WIN_W, heigh=WIN_H)
points_list = []
root.title('Superellips')

canvas.configure(bg='white')
canvas.pack(fill=tk.BOTH, expand=1)

# Слайдер
scale = tk.Scale(root, from_=0.01, to=3.75, digits=3, resolution=0.01, command=slider, orient=tk.HORIZONTAL)
scale.pack(side=tk.LEFT, padx=5)

root.mainloop()