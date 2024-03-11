from tkinter import *
from tkinter import messagebox
import subprocess
import os
root = Tk()
root.title("UbuntuShield")
root.geometry('1200x700')
root.configure(bg='#D9D9D9')

def home():
    home_btn = Frame(main_frame)
    
    
    var = IntVar()
    checkbox = Checkbutton(home_btn, text="Enable Ubuntu Shield", variable=var, font=('Bold', 16))
    checkbox.pack()

    lb = Label(home_btn, text="Ubuntu Shield, crafted by the talented coders Naaz and Kunal, is a robust \n security tool designed to fortify your Ubuntu system against a multitude of threats.\n With its array of powerful features, \n Ubuntu Shield empowers users to safeguard their systems with ease \nand confidence. Key Features: Port Blocker: Take control of your\n network security by selectively blocking ports, \npreventing unauthorized access and thwarting potential cyber threats.\n With Ubuntu Shield's port blocking feature,\n you can fortify your system's defenses against malicious intrusions.\n Website Blocker: Regulate internet usage and protect against harmful or\n distracting content with Ubuntu Shield's website blocking capability.\n Easily create custom blocklists or whitelists to manage access to specific websites, \nensuring a secure and productive browsing experience.\n USB Blocker: Safeguard sensitive data and prevent unauthorized data transfers with Ubuntu Shield's\n USB blocking functionality. Whether in a corporate environment or \nat home, you can control access to USB devices,\n mitigating the risk of data breaches and malware infections.\n SELinux Integration: Benefit from enhanced access controls and\n mandatory access policies with Ubuntu Shield's seamless \nintegration of SELinux (Security-Enhanced Linux).\n Enjoy fine-grained control over process and user access permissions, bolstering the security of your Ubuntu system \nagainst potential threats. Update Option: Stay ahead of security vulnerabilities\n and software bugs with Ubuntu Shield's update feature.\n Effortlessly keep your Ubuntu system up-to date.", font=('bold',16))
    lb.pack()
    home_btn.pack(pady=20)

    def showInfo():
        if var.get() == 1:
            messagebox.showinfo("Information", "Ubuntu Shield is enabled!")
        else:
            messagebox.showinfo("Information", "Ubuntu Shield Disabled!.")

    Button(home_btn, text="Ok", command=showInfo).pack()




def b1():
    b1_btn = Frame(main_frame)
    var1 = IntVar()
    checkbox1 = Checkbutton(b1_btn, text="Enable Port Block", variable=var1, font=('Bold', 16))
    checkbox1.pack()
    lb = Label(b1_btn, text='Port Blocking is a security feature \nthat allows users to control access to specific network ports on their systems or devices.\n By selectively blocking ports,\n users can prevent unauthorized network traffic\n from entering or leaving their network,\n enhancing overall security posture. \nThis feature is vital for organizations looking to protect against external threats,\n such as hacking attempts or malware infections\n, by restricting access to vulnerable ports commonly targeted by attackers.\n With port blocking, users can effectively manage network traffic and mitigate\n potential security risks', font=('Bold',16))
    lb.pack()

    b1_btn.pack(pady=20,padx=20)

    def showInfo1():
        if var1.get() == 1:
            script_dir = os.path.dirname(os.path.realpath(__file__))
            relative_script_path = 'scripts/port.sh'
            absolute_script_path = os.path.join(script_dir, relative_script_path)
            subprocess.run(['bash', absolute_script_path])
            messagebox.showinfo("Information", "Port Block is enabled!")
        else:
            messagebox.showinfo("Information", "Port Block Disabled!")

    Button(b1_btn, text="Ok", command=showInfo1).pack()

    

def b2():
    b2_btn = Frame(main_frame)
    var2 = IntVar()
    checkbox2 = Checkbutton(b2_btn, text="Enable Website Blocker", variable=var2, font=('Bold', 16))
    checkbox2.pack()
    lb = Label(b2_btn, text='The Website Blocking option empowers users to control access to specific websites,\n enhancing security and productivity.\n By configuring custom blocklists or whitelists, users can restrict or \npermit access to websites based on their organization\'s policies.', font=('Bold',16))
    lb.pack()
    b2_btn.pack(pady=20)

    def showInfo1():
        if var2.get() == 1:
            script_dir = os.path.dirname(os.path.realpath(__file__))
            relative_script_path = 'scripts/block.sh'
            absolute_script_path = os.path.join(script_dir, relative_script_path)
            subprocess.run(['bash', absolute_script_path])
            messagebox.showinfo("Information", "Website Blocker is enabled!")
        else:
            messagebox.showinfo("Information", "Website Blocker Disabled!")

    Button(b2_btn, text="Ok", command=showInfo1).pack()

def b3():
    b3_btn = Frame(main_frame)
    var3 = IntVar()
    checkbox2 = Checkbutton(b3_btn, text="SE Linux Website Blocker", variable=var3, font=('Bold', 16))
    checkbox2.pack()
    lb = Label(b3_btn, text='SELinux (Security-Enhanced Linux) is a security feature integrated\n into Linux operating systems, \noffering enhanced access control mechanisms\n to enforce mandatory access controls (MAC).\n It provides fine-grained policies that regulate the access permissions of processes and users,\n based on security policies defined by administrators.\n SELinux helps prevent unauthorized access, privilege escalation, and the spread of malicious software,\n thereby bolstering the overall security posture of Linux systems.', font=('Bold',16))
    lb.pack()
    b3_btn.pack(pady=20)
    def showInfo1():
        if var3.get() == 1:
            script_dir = os.path.dirname(os.path.realpath(__file__))
            relative_script_path = 'scripts/se.sh'
            absolute_script_path = os.path.join(script_dir, relative_script_path)
            subprocess.run(['bash', absolute_script_path])
            messagebox.showinfo("Information", "SE Linux  is enabled!")
        else:
            messagebox.showinfo("Information", "SE Linux disabled!")

    Button(b3_btn, text="Ok", command=showInfo1).pack()

def b4():
    b4_btn = Frame(main_frame)
   
    var4 = IntVar()
    checkbox2 = Checkbutton(b4_btn, text="Enable USB Block", variable=var4, font=('Bold', 16))
    checkbox2.pack()
    lb = Label(b4_btn, text='The USB Blocking feature provides users\n with the ability to control and manage the usage of USB devices on their systems\n. This feature is especially crucial in environments where security and \ndata integrity are paramount, such as corporate networks, government organizations,\n educational institutions, and healthcare facilities.', font=('Bold',16))
    lb.pack()
    b4_btn.pack(pady=20)
    def showInfo1():
        if var4.get() == 1:
            script_dir = os.path.dirname(os.path.realpath(__file__))
            relative_script_path = 'scripts/USB_disable.sh'
            absolute_script_path = os.path.join(script_dir, relative_script_path)
            subprocess.run(['bash', absolute_script_path])
            messagebox.showinfo("Information", "USB Block is enabled!")
        else:
            script_dir = os.path.dirname(os.path.realpath(__file__))
            relative_script_path = 'scripts/USB_enable.sh'
            absolute_script_path = os.path.join(script_dir, relative_script_path)
            subprocess.run(['bash', absolute_script_path])
            messagebox.showinfo("Information", "USB Block disabled!")

    Button(b4_btn, text="Ok", command=showInfo1).pack()

def b5():
    b5_btn = Frame(main_frame)
    var5 = IntVar()
    checkbox2 = Checkbutton(b5_btn, text="Enable Updates", variable=var5, font=('Bold', 16))
    checkbox2.pack()
    lb = Label(b5_btn, text='The updating Linux feature allows users to keep their\n Linux operating system up-to-date with the latest security patches,\n bug fixes, and software enhancements. Through this feature,\n users can easily download and install updates\n for their system\'s software packages, including the kernel,\n libraries, applications, and system utilities.\n Regular updates help ensure system stability,\n performance optimization, and protection against emerging security vulnerabilities,\n thereby maintaining the security and reliability of the Linux environment.', font=('Bold',16))
    lb.pack()
    b5_btn.pack(pady=20)
    def showInfo1():
        if var5.get() == 1:
            script_dir = os.path.dirname(os.path.realpath(__file__))
            relative_script_path = 'scripts/update.sh'
            absolute_script_path = os.path.join(script_dir, relative_script_path)
            subprocess.run(['bash', absolute_script_path])
            messagebox.showinfo("Information", "Update in Progress!")
        else:
            messagebox.showinfo("Information", "Updates Disabled!")

    Button(b5_btn, text="Ok", command=showInfo1).pack()

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

home_btn = Button(options_frame, text='Home',bg='#2F2D2D',fg='#D9D9D9',bd=0, font=('bold',20),command=lambda: indicates(home_indicate, home))
home_btn.place(x=10,y=50)


main_frame = Frame(root, highlightbackground='#2F2D2D', highlightthickness=2)
main_frame.pack(side=LEFT)
main_frame.pack_propagate(False)
main_frame.configure(height=1200, width=800)

home_indicate = Label(options_frame, text='',bg='#2F2D2D')
home_indicate.place(x=3,y=50,width=5,height=40)


b1_btn = Button(options_frame, text='Port Blocker',bg='#2F2D2D',fg='#D9D9D9',bd=0, font=('bold',20),command=lambda: indicates(b1_indicate, b1))
b1_btn.place(x=10,y=100)

b1_indicate = Label(options_frame, text='',bg='#2F2D2D')
b1_indicate.place(x=3,y=100,width=5,height=40)


b2_btn = Button(options_frame, text='Website Blocker',bg='#2F2D2D',fg='#D9D9D9',bd=0, font=('bold',20),command=lambda: indicates(b2_indicate,b2))
b2_btn.place(x=10,y=150)

b2_indicate = Label(options_frame, text='',bg='#2F2D2D')
b2_indicate.place(x=3,y=150,width=5,height=40)


b3_btn = Button(options_frame, text='SELinux',bg='#2F2D2D',fg='#D9D9D9',bd=0, font=('bold',20),command=lambda: indicates(b3_indicate,b3))
b3_btn.place(x=10,y=200)

b3_indicate = Label(options_frame, text='',bg='#2F2D2D')
b3_indicate.place(x=3,y=200,width=5,height=40)


b4_btn = Button(options_frame, text='USB Blocker',bg='#2F2D2D',fg='#D9D9D9',bd=0,font=('bold',20),command=lambda: indicates(b4_indicate,b4))
b4_btn.place(x=10,y=250)

b4_indicate = Label(options_frame, text='',bg='#2F2D2D')
b4_indicate.place(x=3,y=250,width=5,height=40)


b5_btn = Button(options_frame, text='Updates',bg='#2F2D2D',fg='#D9D9D9',bd=0, font=('bold',20),command=lambda: indicates(b5_indicate,b5))
b5_btn.place(x=10,y=300)

b5_indicate = Label(options_frame, text='',bg='#2F2D2D')
b5_indicate.place(x=3,y=300,width=5,height=40)
root.mainloop()
