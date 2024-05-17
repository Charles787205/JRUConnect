import tkinter as tk
from theme import *
from components import Navbar
import theme as theme
from PIL import Image, ImageTk
from tkinter import ttk
class MainLayout(tk.Frame) :

  
  
  def __init__(self, parent,background=theme.WHITE, on_book_button_clicked=None, on_dashboard_button_clicked=None, show_buttons=True, show_admin_buttons=True, app=None, **kwargs):
    super(MainLayout, self).__init__(parent, name="main_layout")
    self.set_layout()
    self.background = background
    self.parent = parent
    self.configure(bg=background,border=0)  # Set the background color
    self.rizal_width = 400
    self.rizal_height = 400
    self.add_rizal()
    self.parent.bind("<Configure>", self.on_resize)
    self.on_book_button_clicked = on_book_button_clicked
    self.on_dashboard_button_clicked = on_dashboard_button_clicked
    self.show_buttons = show_buttons
    
    if(self.show_buttons):
      self.add_buttons()

    self.app = app
  
  def set_title(self, title):
    self.parent.title(title)
  
  def set_geometry(self, geometry):
    self.parent.geometry(geometry)
  
  def add_page(self, page):
    page.pack()

  def set_layout(self):
    self.navbar = Navbar(self)
    self.navbar.pack(side="top", fill="x")
  
  def add_rizal(self):
    
    image = Image.open("assets/rizal.png")
    image = image.resize((self.rizal_width, self.rizal_height))
    self.rizal_photo = ImageTk.PhotoImage(image)
    x = self.winfo_toplevel().winfo_width()
    y = self.winfo_toplevel().winfo_height()

    self.rizal_image = tk.Label(self, image=self.rizal_photo, bg=self.background)
    self.rizal_image.place(x= x-self.rizal_width, y=y-self.rizal_height)
    
    
  def on_resize(self,event):
    if(event.widget != self.winfo_toplevel()):
      return
    width =self.rizal_width
    height = self.rizal_height
    x = self.winfo_toplevel().winfo_width()
    y = self.winfo_toplevel().winfo_height()
    
    self.rizal_image.place_configure(x=x-width, y= y-height)

  def add_buttons(self):
    frame = tk.Frame(self, height=10, bg="blue", name="nav_buttons_frame")

    dashboard_button = tk.Button(frame, bg=DARK_YELLOW_ACTIVE,height=1, text="My Dashboard", fg=theme.WHITE, font=("arial", 20), pady=0, borderwidth=0, activebackground=DARK_YELLOW_ACTIVE, command=self.on_dashboard_button_clicked)

    booking_button = tk.Button(frame, bg=DARK_YELLOW,height=1, text="Book A Facility", fg=theme.WHITE, font=("arial", 20), pady=0 ,borderwidth=0, activebackground=DARK_YELLOW_ACTIVE, command=self.on_book_button_clicked)

    dashboard_button.pack(expand=True, fill="x",side=tk.LEFT)
    booking_button.pack(expand=True, fill="x",side=tk.LEFT)
    frame.pack(side="top",fill=tk.X, after=self.navbar, pady=0)
    return frame
    
  def add_admin_buttons(self):
    frame = tk.Frame(self, height=10, bg="blue", name="nav_buttons_frame")

    pending_button = tk.Button(frame, bg=DARK_YELLOW_ACTIVE,height=1, text="Pending Reservations", fg=theme.WHITE, font=("arial", 20), pady=0, borderwidth=0, activebackground=DARK_YELLOW_ACTIVE, command=self.on_pending_button_clicked)
    rejected_button= tk.Button(frame, bg=DARK_YELLOW,height=1, text="Rejected Reservations", fg=theme.WHITE, font=("arial", 20), pady=0 ,borderwidth=0, activebackground=DARK_YELLOW_ACTIVE, command=self.on_rejected_button_clicked)
    approved_button = tk.Button(frame, bg=DARK_YELLOW,height=1, text="Approved Reservations", fg=theme.WHITE, font=("arial", 20), pady=0 ,borderwidth=0, activebackground=DARK_YELLOW_ACTIVE, command=self.on_approved_button_clicked)

    pending_button.pack(expand=True, fill="x",side=tk.LEFT)
    rejected_button.pack(expand=True, fill="x",side=tk.LEFT)
    approved_button.pack(expand=True, fill="x",side=tk.LEFT)
    facilities_button = tk.Button(frame, bg=DARK_YELLOW,height=1, text="Facilities", fg=theme.WHITE, font=("arial", 20), pady=0 ,borderwidth=0, activebackground=DARK_YELLOW_ACTIVE, command=self.on_facilities_button_clicked)
    facilities_button.pack(expand=True, fill="x",side=tk.LEFT)
    frame.pack(side="top",fill=tk.X, after=self.navbar, pady=0)
    return frame

  def set_admin(self, user, on_pending_button_clicked=None, on_rejected_button_clicked=None, on_approved_button_clicked=None, on_facilities_button_clicked=None):
    self.user =user
    self.on_pending_button_clicked = on_pending_button_clicked
    self.on_rejected_button_clicked = on_rejected_button_clicked
    self.on_approved_button_clicked = on_approved_button_clicked
    self.on_facilities_button_clicked = on_facilities_button_clicked
    self.add_admin_buttons()

  def remove_buttons(self):
    for widget in self.winfo_children():
      if(widget._name == "nav_buttons_frame"):
        widget.destroy()