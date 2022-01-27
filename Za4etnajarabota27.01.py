from tkinter import *

def new_window(event):
    win1=Toplevel()
    win1.grab_set()
    win1.geometry("500x300")
    logw=Label(text="loh")
    logw.grid(row=0, column=0)
    win1.mainloop()

root = Tk()
root.title("Iseseisevtöö")
root.geometry("400x250")
root.resizable(width=False, height=False)
label = Label(text="Чтобы увидеть работы нажмите на кнопку BUTTON!", font="12", pady="10")
label.pack()
btn1 = Button(text="BUTTON", background="#000000", foreground="#fff", padx="15", pady="2", font="12")
btn1.pack()

root.mainloop()

btn1.bind("<Button-1>",
          lambda e="Description": new_window(e))
