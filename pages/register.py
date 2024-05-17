import tkinter as tk
from theme import *
from . import login
from models import User
from models import Student

class RegisterPage(tk.Frame):
  
  def __init__(self, parent):
    self.parent = parent
    super(RegisterPage, self).__init__(parent, bg=WHITE, name='register_page')
    self.add_register_form()
   


  def add_register_form(self):
    
    
    title_frame = tk.Frame(self, bg=WHITE, height=50)
    title_label = tk.Label(title_frame, text="Register", font=(MAIN_FONT, 20, 'bold'), bg=WHITE, fg=BLUE)
    back_button = tk.Button(title_frame, text="Back", bg=WHITE, fg=BLUE, font=(MAIN_FONT, 15), borderwidth=0, cursor="hand2", command=self.on_back_clicked)
    title_label.place(relx=.5, rely=.5, anchor='center')
    back_button.place(anchor='w', relx=0.03, rely=.5)
    title_frame.pack(side='top', fill='x', pady=20, padx=20)
    
    input_frame = tk.Frame(self, bg=WHITE)

    options = ['ADMIN', 'STUDENT']



    self.user_type =  tk.StringVar()
    self.user_type.set('STUDENT')
    user_type_dropdown = tk.OptionMenu(input_frame, self.user_type, *options, command=lambda x: on_usertype_select())
    user_type_dropdown.config(font=(MAIN_FONT, 15), bg=WHITE, fg=BLUE, borderwidth=2, width=20)
    user_type_dropdown.grid(row=0, column=0, padx=10, pady=10, columnspan=3)

    first_name_label = tk.Label(input_frame, text="First Name", font=(MAIN_FONT, 15), bg=WHITE, fg=BLUE)
    first_name_entry = tk.Entry(input_frame, font=(MAIN_FONT, 15), fg=BLUE, borderwidth=2)
    first_name_label.grid(row=1, column=0, padx=10, pady=10)
    first_name_entry.grid(row=2, column=0, padx=10)

    
    middle_name_label = tk.Label(input_frame, text="Middle Name", font=(MAIN_FONT, 15), bg=WHITE, fg=BLUE)
    middle_name_entry = tk.Entry(input_frame, font=(MAIN_FONT, 15), fg=BLUE, borderwidth=2)
    middle_name_label.grid(row=1, column=1, padx=10, pady=10)
    middle_name_entry.grid(row=2, column=1, padx=10)

    last_name_label = tk.Label(input_frame, text="Last Name", font=(MAIN_FONT, 15), bg=WHITE, fg=BLUE)
    last_name_entry = tk.Entry(input_frame, font=(MAIN_FONT, 15), fg=BLUE, borderwidth=2)
    last_name_label.grid(row=1, column=2, padx=10, pady=10)
    last_name_entry.grid(row=2, column=2, padx=10)

    email_label = tk.Label(input_frame, text="Email", font=(MAIN_FONT, 15), bg=WHITE, fg=BLUE)
    email_entry = tk.Entry(input_frame, font=(MAIN_FONT, 15), fg=BLUE, width=40, borderwidth=2)
    email_label.grid(row=3, column=0, padx=10, pady=10, columnspan=2)
    email_entry.grid(row=4, column=0, padx=10, columnspan=2)

    course_label = tk.Label(input_frame, text="Course", font=(MAIN_FONT, 15), bg=WHITE, fg=BLUE)
    course_entry = tk.Entry(input_frame, font=(MAIN_FONT, 15), fg=BLUE, borderwidth=2)
    
    course_label.grid(row=3, column=2, padx=10, pady=10,columnspan=1)
    course_entry.grid(row=4, column=2, padx=10,columnspan=1)


    password_label = tk.Label(input_frame, text="Password", font=(MAIN_FONT, 15), bg=WHITE, fg=BLUE)
    password_label.grid(row=5, column=0, padx=10, pady=10)
    password_entry = tk.Entry(input_frame, font=(MAIN_FONT, 15), show="*", fg=BLUE , width=20, borderwidth=2)
    password_entry.grid(row=6, column=0, padx=10)

    confirm_password_label = tk.Label(input_frame, text="Confirm Password", font=(MAIN_FONT, 15), bg=WHITE, fg=BLUE)
    confirm_password_label.grid(row=5, column=1, padx=10, pady=10)
    confirm_password_entry = tk.Entry(input_frame, font=(MAIN_FONT, 15), show="*", fg=BLUE, width=20, borderwidth=2  )
    confirm_password_entry.grid(row=6, column=1, padx=10)
    
    year_entry_command = self.register(lambda s: s.isdigit() or s == "")
    year_level_label = tk.Label(input_frame, text="Year Level", font=(MAIN_FONT, 15), bg=WHITE, fg=BLUE)
    year_level_entry = tk.Entry(input_frame, font=(MAIN_FONT, 15), fg=BLUE, borderwidth=2, validate='all', validatecommand=(year_entry_command, '%P'))
    year_level_label.grid(row=5, column=2, padx=10, pady=10)
    year_level_entry.grid(row=6, column=2, padx=10)

    def on_register_clicked():
      first_name = first_name_entry.get()
      middle_name = middle_name_entry.get()
      last_name = last_name_entry.get()
      email = email_entry.get()
      course = course_entry.get()
      password = password_entry.get()
      confirm_password = confirm_password_entry.get()
      year_level = year_level_entry.get()
      user_type = self.user_type.get()
      
      print(first_name, middle_name, last_name, email, course, password, confirm_password, year_level)
      if(user_type == 'STUDENT'):
        user = Student(first_name=first_name, middle_name=middle_name, last_name=last_name, email=email, course=course, password=password, confirm_password=confirm_password, year_level=year_level, user_type=user_type)
      else:
        user = User(first_name=first_name, middle_name=middle_name, last_name=last_name, email=email,  password=password, confirm_password=confirm_password, user_type=user_type)
        
      register_info = user.check_register_info()
      if(register_info[0]):
        user.id = user.add_user()
        
        self.on_user_registered(user)
      else:
        print(register_info[1])
        for com in self.pack_slaves():
          if com._name == 'error_message':
            com.destroy()
        error_message = tk.Label(self, text=register_info[1], font=(MAIN_FONT, 15), bg=WHITE, fg='red', name='error_message')
        error_message.pack(before=button)
        
    def on_usertype_select():
      if(self.user_type.get() == 'STUDENT'):
        year_level_label.grid(row=5, column=2, padx=10, pady=10)
        year_level_entry.grid(row=6, column=2, padx=10)
        course_label.grid(row=3, column=2, padx=10, pady=10,columnspan=1)
        course_entry.grid(row=4, column=2, padx=10,columnspan=1)
      else:
        year_level_label.grid_forget()
        year_level_entry.grid_forget()
        course_label.grid_forget()
        course_entry.grid_forget()

    input_frame.pack(pady=20)
    button = tk.Button(self, text="Register", bg=BLUE, fg=DARK_YELLOW, font=(MAIN_FONT, 15), borderwidth=0, cursor="hand2",padx=20, pady=3, command=on_register_clicked)
    
    button.pack(pady=20)

    
    
    return self
  
  
  
    
  def on_back_clicked(self):
    login_page = login.LoginPage(self.parent)
    login_page.place(relx=.5, rely=.5, anchor='center')
    self.place_forget()

  def on_user_registered(self,user):
    self.parent.app.user = user
    self.parent.app.on_login_clicked()
    self.destroy()