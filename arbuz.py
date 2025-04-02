from tkinter import *
root = Tk()
root.geometry('500x500')
root.title('Hello')
canva = Canvas(width=500, height=500, background='gray')
# canva.create_line(0, 0, 490, 490, width=5, fill='blue')
# canva.create_rectangle(10,10,60,60,fill='green',width= 7,outline='pink')
# canva.create_oval(360,360,140,140,width=10,fill='violet')
for i in range(10):
    if i % 3 == 0:
        color = 'white'
    elif i % 2 == 0:
        color = 'red'
    else:
        color = 'green'
    canva.create_rectangle(150+i*10, 150+i*10,350-i*10,350-i*10,fill=color)
canva.pack()
root.mainloop()
