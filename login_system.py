import tkinter
from tkinter import messagebox
from PIL import ImageTk


class login_system:
    def __init__(self, root):
        self.root = root
        self.root.title('Login System')
        self.root.geometry("1350x700+0+0")

        # ======All Images=======
        self.bg_icon = ImageTk.PhotoImage(file="images/background.jpg")
        self.user_icon = tkinter.PhotoImage(file="images/user_icon.png")
        self.password_icon = tkinter.PhotoImage(file="images/password_icon.png")
        self.logo_icon = tkinter.PhotoImage(file="images/logo.png")

        # =======variable====
        self.uname = tkinter.StringVar()
        self.pass_ = tkinter.StringVar()

        def login():
            if self.uname.get() == "" or self.pass_.get() == "":
                messagebox.showerror("Error", 'All fields are required!')
            elif self.uname.get() == "Unnati" and self.pass_.get() == "unnatiwork":
                messagebox.showinfo("Login Successful", f"Welcome {self.uname.get()}")
            else:
                messagebox.showinfo("Error", "Invalid username or password")

        bg_lbl = tkinter.Label(self.root, image=self.bg_icon).pack()
        title = tkinter.Label(self.root, text="Login System", font=("Times New Roman", 40, "bold"), bd=10,
                              relief=tkinter.GROOVE)
        title.place(x=0, y=0, relwidth=1)

        Login_Frame = tkinter.Frame(self.root, bg="white")
        Login_Frame.place(x=400, y=150)

        logolbl = tkinter.Label(Login_Frame, image=self.logo_icon, bd=0).grid(row=0, columnspan=2, pady=20)

        lbluser = tkinter.Label(Login_Frame, text="Username", image=self.user_icon, compound=tkinter.LEFT,
                                font=("Times New Roman", 10, "bold"), bg="white").grid(row=1, column=0, padx=20,
                                                                                       pady=10)
        lblpass = tkinter.Label(Login_Frame, text="Password", image=self.password_icon, compound=tkinter.LEFT,
                                font=("Times New Roman", 10, "bold"), bg="white").grid(row=2, column=0, padx=20,
                                                                                       pady=10)

        txtuser = tkinter.Entry(Login_Frame, textvariable=self.uname, bd=5, relief=tkinter.GROOVE, font=("", 15)).grid(
            row=1, column=1, padx=20)
        txtpass = tkinter.Entry(Login_Frame, textvariable=self.pass_, bd=5, relief=tkinter.GROOVE, font=("", 15)).grid(
            row=2, column=1, padx=20)

        btn_log = tkinter.Button(Login_Frame, text="Login", width=15, font=("times new roman", 14, "bold"),
                                 command=login, bg="Black",
                                 fg="grey").grid(row=3, column=1, pady=10)


root = tkinter.Tk()
obj = login_system(root)
root.mainloop()
