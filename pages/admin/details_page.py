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

class BookingDetails(tk.Frame):
  
  def __init__(self, parent, reservation):
    self.parent = parent
    super(BookingDetails, self).__init__(parent, bg=WHITE, name="booking_details_page")
    self.facility = reservation.facility
    self.reservation = reservation
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
    
    reservation_date_data = tk.Label(self.inner_frame, text=self.reservation.date_reserved.strftime("%B %d, %Y"), font=(MAIN_FONT, 20), bg=WHITE)
    reservation_date_label.grid(row=0, column=3, padx=10, pady=10, sticky="e")
    reservation_date_data.grid(row=0, column=4, padx=10, pady=10, sticky="w")
    

    time_from_label = tk.Label(self.inner_frame, text="Time From", font=(MAIN_FONT, 20), bg=WHITE, anchor='e')
    
    time_from_data = tk.Label(self.inner_frame, text=self.reservation.time_from, font=(MAIN_FONT, 20), bg=WHITE)
    time_from_label.grid(row=1, column=3, padx=10, pady=10, sticky="e")
    time_from_data.grid(row=1, column=4, padx=10, pady=10, sticky="w")
    

    time_to_label = tk.Label(self.inner_frame, text="Time To", font=(MAIN_FONT, 20), bg=WHITE, anchor='e')
    time_to_data = tk.Label(self.inner_frame, text=self.reservation.time_to, font=(MAIN_FONT, 20), bg=WHITE)
    time_to_label.grid(row=2, column=3, padx=10, pady=10, sticky="e")
    time_to_data.grid(row=2, column=4, padx=10, pady=10, sticky="w")
    

    notes_label = tk.Label(self.inner_frame, text="Notes", font=(MAIN_FONT, 20), bg=WHITE, anchor='e')
    notes_entry = tk.Text(self.inner_frame, font=(MAIN_FONT, 20), bg=CREAMY_WHITE, height=5, width=30, wrap="word")
    notes_entry.insert(tk.END, self.reservation.notes)

    notes_label.grid(row=3, column=3, padx=10, pady=10, sticky="e")
    notes_entry.grid(row=3, column=4, padx=10, pady=10, sticky="w", rowspan=4)
    notes_entry.config(state=tk.DISABLED)

    button_frame = tk.Frame(self.inner_frame, bg=WHITE)
    if(self.reservation.status == Reservation.PENDING):
      cancel_button = tk.Button(button_frame, text="Reject", font=(MAIN_FONT, 20), bg=RED, fg=WHITE, borderwidth=0, cursor="hand2", command=lambda: self.on_reject_clicked(self.reservation))
      cancel_button.grid(row=0, column=1, padx=10, pady=10, columnspan=1, sticky="e")
      approved_button = tk.Button(button_frame, text="Accept", font=(MAIN_FONT, 20), bg=BLUE, fg=WHITE, borderwidth=0, cursor="hand2", command=lambda: self.on_approve_clicked(self.reservation))
      approved_button.grid(row=0, column=2, padx=10, pady=10, columnspan=1, sticky="e")
    button_frame.grid(row=7, column=4, padx=10, pady=10, columnspan=2, sticky="e")
    self.inner_frame.pack()

  def on_reject_clicked(self,reservation):
    if messagebox.askyesno("Cancel Reservation", "Are you sure you want to cancel this reservation?"):
      #self.reservation.delete()
      #self.parent.nav_to_pending_reservations("pending")
      reservation.update_status(status='REJECTED')
      messagebox.showinfo("Reservation Cancelled", "Reservation has been rejected.")
      #self.parent.app.nav_to_pending_reservations("pending")
      self.parent.app.nav_to_admin_page()
    else:
      pass

  def on_approve_clicked(self,reservation):
    reservation.update_status(status='APPROVED')
    messagebox.showinfo("Reservation Approved", "Reservation has been approved.")
    #self.parent.nav_to_pending_reservations("pending")
    self.parent.app.nav_to_admin_page()
    pass

  

  

 