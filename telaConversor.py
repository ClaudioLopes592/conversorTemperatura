import tkinter as tk


def converteTemperatura():
    c = float(txt_celsius.get())
    f = (c * 9 / 5) + c
    tk.Label(app, font = ('verdana', '10', 'bold'), bg = 'blue', foreground = 'white', text = ('A temperatura de  {}ºC  equivale a  {}ºF'.format(c,f))).place(x = 20, y = 180, width = 380, height = 20)

app = tk.Tk()
app.title('Coversor de temperatura')
app.geometry('420x300+500+100')
app.configure(bg = 'blue')

tk.Label(app, text = 'Informe a temperatura em graus celsius', font = ('verdana', '10', 'bold'), foreground = 'white', bg = 'blue', anchor = 'w').place(x = 20, y = 50, width = 300, height = 20)
txt_celsius = tk.Entry(app, font = ('verdana', '10', 'bold'))
txt_celsius.place(x = 330, y = 60, anchor = 'w', width = 40, height = 20)
btn_conversor = tk.Button(app, text = 'CONVERTER', command = converteTemperatura)
btn_conversor.place(x = 160, y = 110, width = 100, height = 30)

app.mainloop()