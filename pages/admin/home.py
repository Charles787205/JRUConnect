import tkinter as tk
from theme import *
from models import Reservation
from PIL import Image, ImageTk
class HomePage(tk.Frame):

  def __init__(self, parent, status=Reservation.PENDING, **kwargs):
    super(HomePage, self).__init__(parent, bg=WHITE, name='home_page')
    self.parent = parent
    self.reservations = Reservation().get_reservations_by_status(status)
    self.images = []
    self.status = status
    self.add_home_page()
  def add_home_page(self):
    print(self.reservations)

    title = "Pending Requests" if self.status == Reservation.PENDING else "Approved Reservations" if self.status == Reservation.APPROVED  else  "Rejected Reservations"

    self.title = tk.Label(self, text=title, font=("Arial", 20, 'bold'), bg=WHITE)
    self.title.pack(pady=20)
    canvas = tk.Canvas(self, bg="white")
    
    self.scrollbar = tk.Scrollbar(self, orient="vertical", command=canvas.yview)
    self.scrollable_frame = tk.Frame(canvas, bg="white")
    self.scrollbar.pack(side="right", fill="y")
    
    for i, reservation in enumerate(self.reservations):
      frame = tk.Frame(self.scrollable_frame, bg=WHITE)
      fac_image = Image.open('assets/'+ reservation.facility.image_url)
      fac_image = fac_image.resize((200, 200))
      fac_image = ImageTk.PhotoImage(fac_image)
      self.images.append(fac_image)
      fac_photo = tk.Label(frame, image=fac_image, anchor="w", bg=WHITE)
      fac_photo.grid(row=0, column=0, sticky="w", rowspan=4)
      label = tk.Label(frame, text=f"{reservation.facility.name} - {reservation.facility.location}", font=("Arial", 15, 'bold'), bg=WHITE)
      label.grid(row=0, column=1, sticky="w")

      student_name_label = tk.Label(frame, text=f"Student: {reservation.student.get_full_name().title()}", font=("Arial", 15), bg=WHITE)
      student_name_label.grid(row=1, column=1, sticky="w")

      date_label = tk.Label(frame, text=f"{reservation.date_reserved} {reservation.time_from} - {reservation.time_to}", font=("Arial", 15), bg=WHITE)
      date_label.grid(row=2, column=1, sticky="w")

      button_frame = tk.Frame(frame, bg=WHITE)
      see_details_button = tk.Button(button_frame, text="See Details", font=("Arial", 15), bg=GRAY, fg=BLUE, borderwidth=0, cursor="hand2", command=lambda reservation=reservation: self.on_see_details_clicked(reservation))
      see_details_button.grid(row=0, column=0, sticky="e")

      #if(self.status == Reservation.PENDING):
        #reject_button = tk.Button(button_frame, text="Reject", font=("Arial", 15), bg=RED, fg=WHITE, borderwidth=0, cursor="hand2")
        #reject_button.grid(row=0, column=1, sticky="e", pady=10, padx=10)

        #approve_button = tk.Button(button_frame, text="Approve", font=("Arial", 15), bg=GREEN, fg=WHITE, borderwidth=0, cursor="hand2")
        #approve_button.grid(row=0, column=2, sticky="e", pady=10, padx=10)
      button_frame.grid(row=3, column=1, sticky="e", columnspan=3)
      frame.grid(row=i, column=0, pady=10, padx=10, sticky="w")


    self.scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    self.scrollable_frame.update_idletasks()
    canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
    self.update_idletasks
    print(self.winfo_width())
    canvas.configure(yscrollcommand=self.scrollbar.set, scrollregion=canvas.bbox("all"), width=900, height=800)
    self.bind_all('<MouseWheel>', lambda e: canvas.yview_scroll(int(-1*(e.delta/120)), "units"))
    canvas.pack()
   
  def on_see_details_clicked(self, reservation):
    self.parent.app.show_booking_details(reservation)
