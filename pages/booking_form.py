from models import Facility, Reservation
import tkinter as tk
from PIL import Image, ImageTk
from theme import *
from tkcalendar import Calendar
from tkcalendar import DateEntry
from tktimepicker import SpinTimePickerModern, SpinTimePickerOld, constants, AnalogPicker, AnalogThemes
from tkinter import messagebox
import datetime
import time

class BookingForm(tk.Frame):
  
  def __init__(self, parent, facility):
    self.parent = parent
    super(BookingForm, self).__init__(parent, bg=WHITE, name="booking_form_page")
    self.facility = facility
    self.add_reservation_details()
    
  def add_reservation_details(self):
    facility = self.facility
    self.inner_frame = tk.Frame(self, bg=WHITE)

    facility_image = Image.open(f"assets/{facility.image_url}")
    facility_image = facility_image.resize((500, 500))
    facility_photo = ImageTk.PhotoImage(facility_image)
    facility_label = tk.Label(self.inner_frame, image=facility_photo, bg=WHITE)
    facility_label.image = facility_photo
    facility_label.grid(row=0, column=0, padx=10, pady=10, rowspan=7, columnspan=2, sticky="w")
    
    facility_name_label = tk.Label(self.inner_frame, text="Facility", font=(MAIN_FONT, 20, 'bold'), bg=WHITE, anchor='e')
    facility_name_label1 = tk.Label(self.inner_frame, text=facility.name.title(), font=(MAIN_FONT, 20), bg=WHITE)
    facility_name_label.grid(row=7, column=0, padx=10, pady=10, sticky="w")
    facility_name_label1.grid(row=7, column=1, padx=10, pady=10, sticky="w")

    location_label = tk.Label(self.inner_frame, text="Location", font=(MAIN_FONT, 20, 'bold'), bg=WHITE, anchor='e')
    location_label1 = tk.Label(self.inner_frame, text=facility.location.title(), font=(MAIN_FONT, 20), bg=WHITE)
    location_label.grid(row=8, column=0, padx=10, pady=10, sticky="w")
    location_label1.grid(row=8, column=1, padx=10, pady=10, sticky="w")

    seating_capacity_label = tk.Label(self.inner_frame, text="Seating Capacity", font=(MAIN_FONT, 20, 'bold'), bg=WHITE, anchor='e')
    seating_capacity_label1 = tk.Label(self.inner_frame, text=facility.seating_capacity, font=(MAIN_FONT, 20), bg=WHITE)
    seating_capacity_label.grid(row=9, column=0, padx=10, pady=10, sticky="w")
    seating_capacity_label1.grid(row=9, column=1, padx=10, pady=10, sticky="w")

    reservation_date_label = tk.Label(self.inner_frame, text="Reservation Date", font=(MAIN_FONT, 20), bg=WHITE, anchor='e')
    
    reservation_date_entry = DateEntry(self.inner_frame, font=(MAIN_FONT, 20), bg=CREAMY_WHITE)
    reservation_date_label.grid(row=0, column=3, padx=10, pady=10, sticky="e")
    reservation_date_entry.grid(row=0, column=4, padx=10, pady=10, sticky="w")
    

    time_from_label = tk.Label(self.inner_frame, text="Time From", font=(MAIN_FONT, 20), bg=WHITE, anchor='e')
    
    time_from_entry = tk.Entry(self.inner_frame, font=(MAIN_FONT, 20), bg=CREAMY_WHITE)
    time_from_label.grid(row=1, column=3, padx=10, pady=10, sticky="e")
    time_from_entry.grid(row=1, column=4, padx=10, pady=10, sticky="w")
    time_from_entry.bind("<Button-1>", lambda e: self.on_reserve_time_clicked(time_from_entry))

    time_to_label = tk.Label(self.inner_frame, text="Time To", font=(MAIN_FONT, 20), bg=WHITE, anchor='e')
    time_to_entry = tk.Entry(self.inner_frame, font=(MAIN_FONT, 20), bg=CREAMY_WHITE)
    time_to_label.grid(row=2, column=3, padx=10, pady=10, sticky="e")
    time_to_entry.grid(row=2, column=4, padx=10, pady=10, sticky="w")
    time_to_entry.bind("<Button-1>", lambda e: self.on_reserve_time_clicked(time_to_entry))

    notes_label = tk.Label(self.inner_frame, text="Notes", font=(MAIN_FONT, 20), bg=WHITE, anchor='e')
    notes_entry = tk.Text(self.inner_frame, font=(MAIN_FONT, 20), bg=CREAMY_WHITE, height=5, width=30)
    notes_label.grid(row=3, column=3, padx=10, pady=10, sticky="e")
    notes_entry.grid(row=3, column=4, padx=10, pady=10, sticky="w", rowspan=4)

    button = tk.Button(self.inner_frame, text="Reserve", font=(MAIN_FONT, 20), bg=BLUE, fg=WHITE, borderwidth=0, cursor="hand2", command=lambda: self.add_reservation(reservation_date=reservation_date_entry.get(), time_from=time_from_entry.get(), time_to= time_to_entry.get(), notes= notes_entry.get("1.0", "end-1c")))
    button.grid(row=7, column=4, padx=10, pady=10, columnspan=2, sticky="e")
    self.inner_frame.pack()



  

 
  def on_reserve_time_clicked(self, time_entry):
    toplevel = tk.Toplevel(self, bg=WHITE)
    toplevel.title("Reservation Details")
    toplevel.anchor("center")
    #time_picker = SpinTimePickerModern(toplevel)
    #time_picker.addAll(constants.HOURS24)
    #time_picker.configureAll(bg=WHITE, height=1, fg=BLUE, font=(MAIN_FONT, 16), hoverbg=DARK_YELLOW,
                           # hovercolor=WHITE, clickedbg=DARK_YELLOW, clickedcolor=WHITE)
    #time_picker.configure_separator(bg=CREAMY_WHITE, fg=BLACK)
    time_picker = AnalogPicker(toplevel)
    if(time_entry.get() != ""):
      time_string = time_entry.get().split(" ")
      time = time_string[0].split(":")
      hours = time[0]
      minutes = time[1]
      time_picker.setSpinHours(hours)
      time_picker.setSpinMinutes(minutes)
      time_picker.setHours(hours)
      time_picker.setMinutes(minutes)
    else: 
      time_picker.setMinutes(0)
    time_picker.pack(expand=True, fill="both")
    theme = AnalogThemes(time_picker)
    
    theme.setNavyBlue()
    
    #theme.setDracula()
    def print_time():
      time_entry.delete(0, tk.END)
      time = time_picker.time()
      hours = f"0{time[0]}" if len(str(time[0])) == 1 else str(time[0])
      minutes = f"0{time[1]}" if len(str(time[1])) == 1 else str(time[1])
      time_entry.insert(0, datetime.datetime.strptime(f"{hours}:{minutes} {time[2]}", "%I:%M %p").time())
      
      
      print(datetime.datetime.strptime(f"{hours}:{minutes} {time[2]}", "%I:%M %p").time())
      toplevel.destroy()

    button = tk.Button(toplevel, text="Okay", command=print_time, bg=BLUE, fg=WHITE, font=(MAIN_FONT, 15, 'bold'))
    button.pack(ipadx=20, ipady=2, pady=10)
  
  def add_rizal(self, parent):  
    parent.update_idle_tasks()
    image = Image.open("assets/rizal.png")
    image = image.resize((self.rizal_width, self.rizal_height))
    self.rizal_photo = ImageTk.PhotoImage(image)
    x = self.winfo_toplevel().winfo_width()
    y = self.winfo_toplevel().winfo_height()

    self.rizal_image = tk.Label(self, image=self.rizal_photo, bg=self.background)
    self.rizal_image.place(x= x-self.rizal_width, y=y-self.rizal_height)
  
  def add_reservation(self, **kwargs):
    is_something_empty = False
    for key in kwargs.keys():
      if kwargs.get(key) == "":
        label = tk.Label(self.inner_frame, text="Please fill all the information", font=(MAIN_FONT, 15), fg=RED, name="error_message")
        label.grid(row=8, column=4,padx=10, pady=10, columnspan=2, sticky="e")
        is_something_empty = True
    if is_something_empty:
      return
    date = datetime.datetime.strptime(kwargs.get('reservation_date'), "%m/%d/%y").date()
    reservation = Reservation(facility_id = self.facility.id,
                              student_id = self.parent.app.user.id,
                              date_reserved = date,
                              time_from = kwargs.get('time_from'),
                              time_to = kwargs.get('time_to'),
                              notes = kwargs.get('notes')
                              )
    if reservation.add_reservation():
      messagebox.showinfo("Success", "Reservation Successful")
      self.parent.app.nav_to_home_page()
    print(self.facility.id,self.parent.app.user.id, kwargs.get('reservation_date'),kwargs.get('time_from'),kwargs.get('time_to'),kwargs.get('notes'), sep=",")
    
  