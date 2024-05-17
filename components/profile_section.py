import tkinter as tk
from theme import *
from PIL import Image, ImageTk

class ProfileSection(tk.Frame):

  def __init__(self,parent, name="", year_level="", program=""):
    super(ProfileSection, self).__init__(parent)
    self.parent = parent
    self.name = name
    self.year_level = year_level
    self.program = program
    self.create_section()
    
  def create_section(self):
    container = tk.Frame(self,bg=WHITE)

    #add image
    image = Image.open("assets/profile_image.png")
    image = image.resize((200,200))
    self.profile_photo = ImageTk.PhotoImage(image)
    self.profile_image = tk.Label(container, image=self.profile_photo, bg=WHITE)
    self.profile_image.pack(side=tk.LEFT)

    profile_info_container = tk.Frame(container,bg=WHITE)
    
    basic_info_label = tk.Label(profile_info_container, text="Basic Info", font= (MAIN_FONT, 14, 'bold'), bg=WHITE,anchor="w")
    name_label = tk.Label(profile_info_container, text="Name %s" % self.name, font=(MAIN_FONT, 15), bg=WHITE,anchor="w")
    year_level_label = tk.Label(profile_info_container, text="Year Level %s" % self.year_level, font=(MAIN_FONT, 15), bg=WHITE,anchor="w")
    program_label = tk.Label(profile_info_container, text="Program %s" % self.program, font=(MAIN_FONT, 15), bg=WHITE,anchor="w")

    basic_info_label.grid(row=1, column=1,sticky="w")
    name_label.grid(row=2, column=1,sticky="w")
    year_level_label.grid(row=3, column=1,sticky="w")
    program_label.grid(row=4, column=1,sticky="w")
    profile_info_container.pack(side=tk.LEFT, padx=10)
    container.pack()