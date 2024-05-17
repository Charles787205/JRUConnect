import tkinter as tk;
from models import Reservation;
from theme import *;
import datetime
from PIL import Image, ImageTk
class BookingList(tk.Canvas):

  def __init__(self, parent, status=Reservation.PENDING, **kwargs):
    super(BookingList, self).__init__(parent, bg=WHITE,name="book_list_page", **kwargs)
    self.status = status
    self.parent = parent
    self.reservations = Reservation(student_id = self.parent.app.user.id).get_reservations_by_status_user_id(status=self.status)
    self.pack()
    self.add_reservations(status)
    self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.yview)
    self.configure(yscrollcommand=self.scrollbar.set)
    self.scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')
    self.bind_all('<MouseWheel>', lambda event: self.yview_scroll(-int(event.delta/60), 'units'))
    

  def add_reservations(self, status):
    self.frame = tk.Frame(self,bg=WHITE)
    title = "Pending Reservations" if status == Reservation.PENDING else "Approved Reservations"
    label = tk.Label(self.frame, text=title, font=("arial", 20, 'bold'), bg=WHITE)
    label.grid(row=0, column=0, padx=10, pady=10, sticky='w')
    print(self.reservations)
    for i in range(len(self.reservations)):
      reservation = self.reservations[i]
      reservation_frame = tk.Frame(self.frame, bg=WHITE)

      image = Image.open(f"assets/{reservation.facility.image_url}")
      image = image.resize((200, 200))
      photo = ImageTk.PhotoImage(image)
      image_label = tk.Label(reservation_frame, image=photo, bg=WHITE)
      image_label.image = photo
      image_label.grid(row=0, column=0, padx=10, rowspan=3, pady=10, sticky='w')

      label = tk.Label(reservation_frame, text=f"{reservation.facility.name} - {reservation.facility.location}", font=("arial", 20, 'bold'), bg=WHITE, anchor='w')
      label.grid(row=0, column=1, padx=10, pady=10, sticky='w')
      date_reserved = reservation.date_reserved.strftime("%B %d, %Y")
      message = f"{date_reserved}\n{reservation.time_from} - {reservation.time_to}"
      reservation_label = tk.Label(reservation_frame, text=message, font=("arial", 15), bg=WHITE)
      reservation_label.grid(row=1, column=1, padx=10, pady=10, sticky='w')
      reservation_frame.grid(row=i+1, column=0, padx=10, pady=10, sticky='w')
    self.create_window(300, 0, window=self.frame, anchor='nw')
    self.frame.update_idletasks()
    self.configure(scrollregion=(0, 0, 0, self.frame.winfo_height()))

