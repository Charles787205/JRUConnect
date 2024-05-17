import tkinter as tk
from models import Facility
from components import FacilityDetail
from theme import *
class BookAFacilityPage(tk.Canvas):

  def __init__(self, parent):
    self.parent = parent
    super(BookAFacilityPage, self).__init__(parent, bg=WHITE, name='book_a_facility_page')
    #elf.add_book_a_facility_form()

    self.pack(expand=True, fill="both")

    self.add_facilites()
    self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.yview)
    self.configure(yscrollcommand=self.scrollbar.set)
    self.scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')
    self.bind('<MouseWheel>', lambda event: self.yview_scroll(-int(event.delta/60), 'units'))

  def add_facilites(self):
    facilities = Facility.get_facilites()
    self.facilities_frame = tk.Frame(self, bg=WHITE)
    for i in range(0,len(facilities),2):
      print(facilities[i].name, i )
      for j in range(2):
        facility = facilities[i+j]
        facility_detail = FacilityDetail(self.facilities_frame, facility)
        facility_detail.grid(row=int(i/2), column=j, padx=10, pady=10,sticky="w")
    
    self.create_window(300, 0, window=self.facilities_frame, anchor='nw')
    self.facilities_frame.update_idletasks()
    self.configure(scrollregion=(0, 0, 0, self.facilities_frame.winfo_height()))
    #facility = Facility(name="New Auditorium", location="Centennial Building", capacity=1000, image_url="new_auditorium.png")
    #facility_detail = FacilityDetail(self, facility)
   # #facility_detail.grid(row=0, column=0, padx=10, pady=10)
 
  