import tkinter as tk
from tkinter import ttk
from layouts.main_layout import MainLayout
from theme import *
from components import ProfileSection
from PIL import Image, ImageTk
from models import Reservation
class HomePage(tk.Frame) :
  
  def __init__(self, parent):
    
    self.parent = parent
    
    super(HomePage, self).__init__(parent, bg=WHITE, name="home_page")
 
    
    self.user = self.parent.app.user
    self.add_profile_section()
    

    self.add_reservation_frame()
    
  

  def add_profile_section(self):
    
    profile = ProfileSection(self, self.user.get_full_name().title(), f"%dth Year" % self.user.year_level, self.user.course)
    profile.pack(pady=20)
    frame = tk.Frame(self, bg="gray", height=2)
    frame.pack(fill=tk.X)
    #frame.pack()
  
  def add_approved_reservation(self, parent):
    approved_reservation = Reservation(student_id = self.user.id).get_reservations_by_status_user_id(status=Reservation.APPROVED)
    frame = tk.Frame(parent, bg=WHITE, height=200)
    container = tk.Frame(frame, bg='white')
    label = tk.Label(container, text="Approved Reservations", font=("arial", 20, 'bold'), bg=WHITE)
    label.pack()
    message = ""
    
    if len(approved_reservation) == 0:
      message = "\t• No Approved Reservations"
      reservation_label = tk.Label(container, text=message, font=("arial", 15), bg=WHITE)
      reservation_label.pack()
      container.pack()
      return frame
    reservation  = approved_reservation[-1]
    message = f"\t• {reservation.facility.name}-{reservation.facility.location}\n\t{reservation.date_reserved} , {reservation.time_from} - {reservation.time_to}"
    reservation_label = tk.Label(container, text=message, font=("arial", 15), bg=WHITE)
    button = tk.Button(container, text="View All", bg=WHITE, fg='blue', font=("arial", 15,'italic', 'underline'), borderwidth=0, cursor="hand2")
    sized_box = tk.Frame(container, height=100, bg=WHITE)
    reservation_label.pack()
    sized_box.pack()
    button.place(anchor="se", relx=.9, rely=.9)
    container.pack()
    button.bind("<Button-1>", lambda e: self.parent.app.nav_to_pending_reservations(Reservation.APPROVED))
    return frame
  def add_pending_requests(self, parent):
    pending_reservations = Reservation(student_id = self.user.id).get_reservations_by_status_user_id(status=Reservation.PENDING)
    if len(pending_reservations) == 0:
      return tk.Frame(parent, bg=WHITE, height=200)
    
    reservation = pending_reservations[-1]

    frame = tk.Frame(parent, bg=WHITE, height=100)
    container = tk.Frame(frame, bg='white')
    label = tk.Label(container, text="Pending Reservations", font=("arial", 20, 'bold'), bg=WHITE)
    reservation_label = tk.Label(container, text=f"\t• {reservation.facility.name}-{reservation.facility.location}\n\t{reservation.date_reserved} , {reservation.time_from} - {reservation.time_to}", font=("arial", 15), bg=WHITE)
    button = tk.Button(container, text="View All", bg=WHITE, fg='blue', font=("arial", 15,'italic', 'underline'), borderwidth=0, cursor="hand2")
    sized_box = tk.Frame(container, height=100, bg=WHITE)
    label.pack()
    reservation_label.pack()
    sized_box.pack()
    button.place(anchor="se", relx=.9, rely=.9)
    container.pack()

    button.bind("<Button-1>", lambda e: self.parent.app.nav_to_pending_reservations(Reservation.PENDING))
    return frame

  def add_reservation_frame(self):
    frame = tk.Frame(self, bg="blue", height=100)
    approved_reservation = self.add_approved_reservation(frame)
    pending_request = self.add_pending_requests(frame)
    approved_reservation.pack(side="left", fill="both", expand=True )
    pending_request.pack(side="right", fill="both", expand=True)
    frame.pack(fill='both', expand=True)

 