from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import os
import subprocess
def handle_log():
    email = email_input.get()
    pswd = pswd_input.get()
    print(email,pswd)
    if (email == '12323003' and pswd == 'Naaz@123'):
        current_directory = os.path.dirname(os.path.realpath(__file__))
        relative_path_to_script = "scripts/Main.sh"
        absolute_path_to_script = os.path.join(current_directory, relative_path_to_script)
        subprocess.run(["bash", absolute_path_to_script])
        messagebox.showinfo('Yes', 'You Logged in succesfully')
    elif (email == '12324783' and pswd == 'kunal@123'): 
        current_directory = os.path.dirname(os.path.realpath(__file__))
        relative_path_to_script = "scripts/Main.sh"
        absolute_path_to_script = os.path.join(current_directory, relative_path_to_script)
        subprocess.run(["bash", absolute_path_to_script])
        messagebox.showinfo('Yes', 'You Logged in succesfully')
    else:
        messagebox.showerror('Error', 'Login Failed')

root = Tk()
root.title("UbuntuShield")
root.geometry('1200x700')

root.configure(bg='#2F2D2D')



text_label = Label(root,text='UbuntuShield',fg='#D9D9D9',bg='#2F2D2D')
text_label.pack()
text_label.config(font=('poppins', 50),highlightbackground='#D9D9D9',highlightthickness=5)


email_label = Label(root,text='Enter ID',fg='#D9D9D9',bg='#2F2D2D',font=('poppins',24))
email_label.pack(pady=(30,10))


email_input=Entry(root,width=50)
email_input.pack(ipady=3,pady=(10,5))

pswd_label = Label(root,text='Enter Password',fg='#D9D9D9',bg='#2F2D2D')
pswd_label.pack(pady=(20,5))
pswd_label.config(font=('poppins', 24))

pswd_input=Entry(root,width=50)
pswd_input.pack(ipady=3,pady=(10,5))


login_btn = Button(root,text='Login Here',bg='#D9D9D9',fg='#2F2D2D',width=10,height=1,command=handle_log)
login_btn.pack(pady=(20,5))
login_btn.config(font=('poppins',10))

root.mainloop()


