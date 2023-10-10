import tkinter as tk
from tkinter import Canvas

def draw_graph():
    x_values = range(-10, 11)
    y_values = [x**2 + 6*x + 12 for x in x_values]

    canvas.delete("all")

    # размеры
    graph_width = 200
    graph_height = 200
    x_scale = graph_width / (len(x_values) - 1)
    y_scale = graph_height / (max(y_values) - min(y_values))

    # Отрисовываем оси координат
    canvas.create_line(20, graph_height + 20, graph_width + 20, graph_height + 20)
    canvas.create_line(20, 20, 20, graph_height + 20)

    #  график
    for i in range(len(x_values) - 1):
        x1 = x_values[i] * x_scale + 20
        y1 = graph_height - (y_values[i] - min(y_values)) * y_scale + 20
        x2 = x_values[i+1] * x_scale + 20
        y2 = graph_height - (y_values[i+1] - min(y_values)) * y_scale + 20
        canvas.create_line(x1, y1, x2, y2)

def draw_flower():
    canvas.delete("all")

    #  стебель
    canvas.create_polygon(230, 550,
                          230, 350,
                          280, 350,
                          280, 550,
                          fill="green")

    # лепестки
    canvas.create_oval(     190, 290,     290, 390,       fill="yellow"   )
    canvas.create_oval(     150, 250,     250, 350,       fill="red"      )
    canvas.create_oval(     250, 250,     350, 350,       fill="red"      )
    canvas.create_oval(     150, 350,     250, 450,       fill="red"      )
    canvas.create_oval(     250, 350,     350, 450,       fill="red"      )

# окно
window = tk.Tk()
window.title("График функции и цветок")
window.geometry("800x800")

#  холст
canvas = Canvas(window, width=900, height=900)
canvas.place(x=25, y=25)

# кнопки
graph_button = tk.Button(window, text="Построить график", command=draw_graph)
graph_button.place(x=150, y=20)

flower_button = tk.Button(window, text="Нарисовать цветок", command=draw_flower)
flower_button.place(x=300, y=20)

window.mainloop()