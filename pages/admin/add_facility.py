from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from theme import *
from models import Facility
import shutil
class AddFacilityPage(Frame):
  def __init__(self, parent):
    self.parent = parent
    super(AddFacilityPage, self).__init__(parent, bg=WHITE, name='add_facility_page')
    self.add_facility_form()
    self.pack(expand=True, fill="both")

  def add_facility_form(self):
    self.facility_form = Frame(self, bg=WHITE)
    self.facility_form.pack(pady=50)
    
    self.name_label = Label(self.facility_form, text="Facility Name", font=(MAIN_FONT, 20), bg=WHITE)
    self.name_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    self.name_entry = Entry(self.facility_form, font=(MAIN_FONT, 20))
    self.name_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

    self.location_label = Label(self.facility_form, text="Facility Location", font=(MAIN_FONT, 20), bg=WHITE)
    self.location_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    self.location_entry = Entry(self.facility_form, font=(MAIN_FONT, 20))
    self.location_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    self.capacity_label = Label(self.facility_form, text="Seating Capacity", font=(MAIN_FONT, 20), bg=WHITE)
    self.capacity_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    self.capacity_entry = Entry(self.facility_form, font=(MAIN_FONT, 20))
    self.capacity_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    self.image_label = Label(self.facility_form, text="Facility Image", font=(MAIN_FONT, 20), bg=WHITE)
    self.image_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
    self.image_entry = Entry(self.facility_form, font=(MAIN_FONT, 20))
    self.image_entry.insert(0, "Choose Image")
    self.image_entry.bind("<Button-1>", self.on_image_entry_click)
    self.image_entry.configure(textvariable=self.image_entry, state="readonly")
    self.image_entry.grid(row=3, column=1, padx=10, pady=10, sticky="w")
    
    
    
    self.add_facility_button = Button(self.facility_form, text="Add Facility", font=(MAIN_FONT, 20), bg=WHITE, fg=BLUE, cursor="hand2")
    self.add_facility_button.grid(row=4, column=1, padx=10, pady=10, sticky="w")
    self.add_facility_button.bind("<Button-1>", lambda e: self.on_add_facility_clicked())
  def on_image_entry_click(self, event):
    file_path = filedialog.askopenfile()
    
    is_valid_image = self.validate_image(file_path.name)
    if not is_valid_image:
      messagebox.showerror("Invalid Image", "Please select a valid image file")
    else:
    
      self.image_entry.configure(fg="black", state="normal")
      self.image_entry.delete(0, END)
      self.image_entry.insert(0, file_path.name)
      self.image_entry.configure(textvariable=self.image_entry, state="readonly")
      

  def validate_image(self, file_path):
    print(file_path)
    try:
      from PIL import Image

      image = Image.open(file_path)
      image.close()
      return True
    except Exception as e:
      print(e)
      return False
    
  def on_add_facility_clicked(self):
    name = self.name_entry.get()
    location = self.location_entry.get()
    capacity = self.capacity_entry.get()
    image_url = self.image_entry.get()
    
    if not name or not location or not capacity or not image_url:
      messagebox.showerror("Missing Fields", "Please fill in all fields")
      return
    
    source_file = open(image_url, 'rb')
    destination_file = open(f"assets/{image_url.split('/')[-1]}" , 'wb')
    shutil.copyfileobj(source_file, destination_file)
    image_url = image_url.split('/')[-1]
    facility = Facility(name=name, location=location, seating_capacity=capacity, image_url=image_url)
    facility.save()
    messagebox.showinfo("Facility Added", "Facility has been added successfully")
    
    self.parent.app.admin_on_facilities_clicked()
    self.destroy()