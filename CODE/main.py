from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("UbuntuShield")
root.geometry('1200x700')
root.iconbitmap('icon.ico')
root.configure(bg='#D9D9D9')
def home():
    home_btn = Frame(main_frame)
    lb = Label(home_btn, text="Ubuntu Shield, crafted by the talented coders Naaz and Kunal,\n is a robust security tool designed to fortify \nyour Ubuntu system against a multitude of threats.\n With its array of powerful features, Ubuntu Shield empowers users to safeguard \ntheir systems with ease and confidence.",font=('Bold',16))
    lb.pack()
    home_btn.pack(pady=20)

def b1():
    b1_btn = Frame(main_frame)
    lb = Label(b1_btn, text='\n\n\n\nMenu Page\n\nPage: 2', font=('Bold',30))
    lb.pack()
    b1_btn.pack(pady=20)

def b2():
    b2_btn = Frame(main_frame)
    lb = Label(b2_btn, text='Menu Page\n\nPage: 3', font=('Bold',30))
    lb.pack()
    b2_btn.pack(pady=20)

def b3():
    b3_btn = Frame(main_frame)
    lb = Label(b3_btn, text='Menu Page\n\nPage: 4', font=('Bold',30))
    lb.pack()
    b3_btn.pack(pady=20)

def b4():
    b4_btn = Frame(main_frame)
    lb = Label(b4_btn, text='Menu Page\n\nPage: 5', font=('Bold',30))
    lb.pack()
    b4_btn.pack(pady=20)

def b5():
    b5_btn = Frame(main_frame)
    lb = Label(b5_btn, text='Menu Page\n\nPage: 6', font=('Bold',30))
    lb.pack()
    b5_btn.pack(pady=20)

def hide():
    home_indicate.config(bg='#2F2D2D')
    b1_indicate.config(bg='#2F2D2D')
    b2_indicate.config(bg='#2F2D2D')
    b3_indicate.config(bg='#2F2D2D')
    b4_indicate.config(bg='#2F2D2D')
    b5_indicate.config(bg='#2F2D2D')

def dlt():
    for frame in main_frame.winfo_children():
        frame.destroy()

def indicates(lb, page):
    hide()
    lb.config(bg='#D9D9D9')
    dlt()
    page()





options_frame = Frame(root,bg='#2D2F2F')
options_frame.pack(side=LEFT)
options_frame.pack_propagate(False)
options_frame.config(width=300,height=1200)

home_btn = Button(options_frame, text='Home',bg='#D9D9D9',fg='#2F2D2D',bd=0, font=('bold',20),command=lambda: indicates(home_indicate, home))
home_btn.place(x=10,y=50)


main_frame = Frame(root, highlightbackground='#2F2D2D', highlightthickness=2)
main_frame.pack(side=LEFT)
main_frame.pack_propagate(False)
main_frame.configure(height=1200, width=800)

home_indicate = Label(options_frame, text='',bg='#2F2D2D')
home_indicate.place(x=3,y=50,width=5,height=40)


b1_btn = Button(options_frame, text='Port Blocker',bg='#D9D9D9',fg='#2F2D2D',bd=0, font=('bold',20),command=lambda: indicates(b1_indicate, b1))
b1_btn.place(x=10,y=100)

b1_indicate = Label(options_frame, text='',bg='#2F2D2D')
b1_indicate.place(x=3,y=100,width=5,height=40)


b2_btn = Button(options_frame, text='Website Blocker',bg='#D9D9D9',fg='#2F2D2D',bd=0, font=('bold',20),command=lambda: indicates(b2_indicate,b2))
b2_btn.place(x=10,y=150)

b2_indicate = Label(options_frame, text='',bg='#2F2D2D')
b2_indicate.place(x=3,y=150,width=5,height=40)


b3_btn = Button(options_frame, text='SELinux',bg='#D9D9D9',fg='#2F2D2D',bd=0, font=('bold',20),command=lambda: indicates(b3_indicate,b3))
b3_btn.place(x=10,y=200)

b3_indicate = Label(options_frame, text='',bg='#2F2D2D')
b3_indicate.place(x=3,y=200,width=5,height=40)


b4_btn = Button(options_frame, text='USB Blocker',bg='#D9D9D9',fg='#2F2D2D',bd=0,font=('bold',20),command=lambda: indicates(b4_indicate,b4))
b4_btn.place(x=10,y=250)

b4_indicate = Label(options_frame, text='',bg='#2F2D2D')
b4_indicate.place(x=3,y=250,width=5,height=40)


b5_btn = Button(options_frame, text='Updates',bg='#D9D9D9',fg='#2F2D2D',bd=0, font=('bold',20),command=lambda: indicates(b5_indicate,b5))
b5_btn.place(x=10,y=300)

b5_indicate = Label(options_frame, text='',bg='#2F2D2D')
b5_indicate.place(x=3,y=300,width=5,height=40)
root.mainloop()