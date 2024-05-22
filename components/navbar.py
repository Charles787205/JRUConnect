import tkinter as tk
import theme as theme
import os
from PIL import Image, ImageTk
def resource_path(relative):
    return os.path.join(
        os.environ.get(
            "_MEIPASS2",
            os.path.abspath(".")
        ),
        relative
    )
class Navbar(tk.Frame):
  LOGO_SIZE = 110
  
  def __init__(self, parent):
    tk.Frame.__init__(self, parent,bg=theme.BLUE, name="navbar")
    self.parent = parent
    self.background_color = theme.BLUE
    self.title = "JRUConnect"
    self.configure(height=140)
    self.add_widgets()
    
    print("navbar")
  def add_widgets(self):
    self.add_image()
    self.add_header()
    self.add_logout_button()

  def add_header(self):
    header = tk.Label(self, text=self.title, font=(theme.MAIN_FONT, 50), bg=self.background_color, fg=theme.WHITE)
    header.pack(side="left", padx=10, pady=10)

  def add_image(self):
    image = Image.open(resource_path("assets/logo.png"))  
    image = image.resize((self.LOGO_SIZE, self.LOGO_SIZE))
    global photo
    
    photo = ImageTk.PhotoImage(image)
    
    logo = tk.Label(self, image=photo, bg=self.background_color)
    logo.pack(side="left", padx=10, pady=10)

   
  def add_logout_button(self):
    logout_button = tk.Button(self, text="Logout", font=(theme.MAIN_FONT, 20), bg=theme.BLUE, fg=theme.WHITE, command=self.logout, name="logout_button")
    logout_button.pack(side="right", padx=10, pady=10)

  def logout(self):
    self.winfo_toplevel().children['main_layout'].app.user = None
    self.winfo_toplevel().children['main_layout'].app.nav_to_login_page()
    self.parent.app.nav_to_login_page()

  def remove_logout_button(self):
    for child in self.winfo_children():
      if child.winfo_name() == "logout_button":
        child.destroy()
    
 