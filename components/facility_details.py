import tkinter as tk
from PIL import Image, ImageTk
from theme import *

class FacilityDetail(tk.Frame):

  def __init__(self, parent, facility, is_admin=False):
    self.parent = parent
    super(FacilityDetail, self).__init__(parent, bg=WHITE)
    self.facility = facility
    self.is_admin = self.get_user_status()

    self.add_facility_details()

  def add_facility_details(self):
    
    facility = self.facility
    image = Image.open(f"assets/{facility.image_url}")
    image = image.resize((300, 300))
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(self, image=photo, bg='white', anchor="w")
    label.image = photo
    label.grid(row=0, column=0, padx=10, pady=10, rowspan=3)
    name_label = tk.Label(self, text=facility.name, font=("arial", 20, 'bold'), bg='white')
    name_label.grid(row=0, column=1, padx=10, pady=10)
    if(not self.is_admin):
      reserve_now_button = tk.Button(self, text="Reserve Now", bg='white', fg='blue', font=("arial", 15, 'underline'), borderwidth=0, cursor="hand2")
      reserve_now_button.grid(row=2, column=1)
      reserve_now_button.bind("<Button-1>", lambda e: self.on_click())
    else:
      edit_button = tk.Button(self, text="Edit", bg='white', fg='blue', font=("arial", 15, 'underline'), borderwidth=0, cursor="hand2")
      edit_button.grid(row=2, column=1)
      edit_button.bind("<Button-1>", lambda e: self.on_edit_click())

  def on_click(self):
    app = self.winfo_toplevel().children['main_layout'].app
    app.nav_to_booking_details(self.facility)

  def on_edit_click(self):
    self.winfo_toplevel().children['main_layout'].app.nav_to_edit_facility(self.facility)
    
    

  def get_user_status(self):
    from models import User
    user = self.winfo_toplevel().children['main_layout'].app.user
    return user.user_type == User.ADMIN