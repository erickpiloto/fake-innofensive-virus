import tkinter as tk

root= tk.Tk()
root.title('g1.com/bbb - BBB 24h')

canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()

def hello():
    label1 = tk.Label(root, text= 'Seu computador acaba de ser\nHaCkEaDo!!!\n \nInocente! kkk', fg='black', font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 200, window=label1)

button1 = tk.Button(text='Clique para Assistir!', command=hello, bg='gray', fg='white')
canvas1.create_window(150, 150, window=button1)

root.mainloop()