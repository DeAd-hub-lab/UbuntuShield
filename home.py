from tkinter import *
root = Tk()
root.title("UbuntuShield")
root.geometry('1200x700')
root.iconbitmap('icon.ico')
root.configure(bg='#2F2D2D')

text_input = Text(root,height=5,width=30)
text_input.pack()

root.mainloop()
