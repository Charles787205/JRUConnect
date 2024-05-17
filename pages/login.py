import tkinter as tk
from models import Student
from theme import *
from .register import RegisterPage
from models import User
class LoginPage(tk.Frame):
  
  def __init__(self, parent, on_login_clicked=None):
    self.parent = parent
    super(LoginPage, self).__init__(parent, bg=WHITE, name='login_page')
    self.login_form = self.add_login_form()
    self.on_login_clicked = on_login_clicked
   


  def add_login_form(self):
    login_form = self

    def on_login_clicked():
      email = email_entry.get()
      password = password_entry.get()
      user = User(email=email, password=password)
      user_info = user.get_user()
      if user_info == None:
        error_message = tk.Label(login_form, text="Invalid email or password", font=(MAIN_FONT, 15), bg=WHITE, fg='red', name='error_message')
        error_message.pack(before=button, pady=10)
      else: 
        if user_info['user_type'] == User.STUDENT:
          self.user = Student(**user_info)
          self.user.add_data_from_dict(self.user.get_course_and_year_level())
        else: 
          self.user = User(**user_info)
        self.parent.app.user = self.user 
        self.on_login_clicked()
    
    label = tk.Label(login_form, text="Login", font=(MAIN_FONT, 20, 'bold'), bg=WHITE, fg=BLUE)
    label.pack(pady=20)
    email_label = tk.Label(login_form, text="Email", font=(MAIN_FONT, 15), bg=WHITE, fg=BLUE)
    email_label.pack()
    email_entry = tk.Entry(login_form, font=(MAIN_FONT, 15), fg=BLUE)
    email_entry.pack(pady=10)
    password_label = tk.Label(login_form, text="Password", font=(MAIN_FONT, 15), bg=WHITE, fg=BLUE)
    password_label.pack()
    password_entry = tk.Entry(login_form, font=(MAIN_FONT, 15), show="*", fg=BLUE )
    password_entry.pack(pady=10)
    button = tk.Button(login_form, text="Login", bg=BLUE, fg=DARK_YELLOW, font=(MAIN_FONT, 15), borderwidth=0, cursor="hand2",padx=20, pady=3, command=on_login_clicked)
    button.pack(pady=20)

    register_frame = tk.Frame(login_form , bg=WHITE)
    prompt_label = tk.Label(register_frame, text="Don't have an account yet? ", font=(MAIN_FONT, 15), bg=WHITE, fg=BLUE)
    register_label = tk.Label(register_frame, text="Register", font=(MAIN_FONT, 15), bg=WHITE, fg='blue')
    prompt_label.pack(side='left')
    register_label.pack(side='right')
    register_frame.pack(padx=20, pady=20)
    register_label.bind('<Button-1>', self.on_register_clicked)
    
    

    return login_form
  
  
    
    
  def on_register_clicked(self, event):
    self.place_forget()
    register_page = RegisterPage(self.parent)
    register_page.place(relx=.5, rely=.5, anchor='center')
