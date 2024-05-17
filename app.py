from tkinter import *
from models.reservation import Reservation
from pages import HomePage, LoginPage, BookAFacilityPage, BookingForm, BookingList
from pages.admin import HomePage as AdminHomePage,BookingDetails, FacilitiesPage, AddFacilityPage,EditFacilityPage
from models import User
from layouts.main_layout import MainLayout
from theme import *


class JRUConnect():

  def __init__(self):
    
    self.root = Tk()  # create root window
    self.root.title("JRUConnect")  # title of the GUI window
    self.root.geometry(f"{self.root.winfo_screenwidth()}x{self.root.winfo_screenheight()}")  # specify the window size
    
    self.root.update_idletasks()
    self.user = None
    self.root.wm_attributes('-transparentcolor', '#ab23ff')
    self.root.config(bg='red')
    

    self.main_layout = MainLayout(self.root, show_buttons= False,
                                   on_book_button_clicked=self.book_button_clicked,
                                     on_dashboard_button_clicked=self.dashboard_button_clicked,
                                     background=DARK_YELLOW,
                                     app=self
                                     )
    self.main_layout.pack(fill="both", expand=True)
    
    
    
    self.nav_to_login_page()

      

  def run(self):
    self.root.mainloop()

  def book_button_clicked(self):
    self.remove_page()
    self.nav_to_book_a_facility()

  def on_login_clicked(self):
    if(self.user.user_type == User.STUDENT):
      self.nav_to_home_page()
    else:
      self.nav_to_admin_page()


  def dashboard_button_clicked(self):
    self.remove_page()
    self.home = HomePage(self.main_layout)
    self.home.pack(expand=True, fill="both")

  def nav_to_login_page(self):
    self.remove_page()
    for child in self.main_layout.winfo_children():
      if(child._name == 'navbar'):
        child.remove_logout_button()
        
    self.login = LoginPage(self.main_layout, on_login_clicked=self.on_login_clicked)
    self.login.place(relx=.5, rely=.5, anchor='center')
    self.main_layout.configure(bg=DARK_YELLOW)
    self.main_layout.remove_buttons()
    self.main_layout.rizal_image.configure(bg=DARK_YELLOW)
    

  
  def nav_to_home_page(self):
    self.remove_page()
    for child in self.main_layout.winfo_children():
      if(child._name == 'navbar'):
        child.add_logout_button()
    self.home = HomePage(self.main_layout)
    self.home.pack(expand=True, fill="both")
    self.main_layout.configure(bg=WHITE)
    self.main_layout.rizal_image.configure(bg=WHITE)
    
    buttons = self.main_layout.add_buttons()
  
  def nav_to_admin_page(self,status='PENDING'):
    self.remove_page()
    for child in self.main_layout.winfo_children():
      if(child._name == 'navbar'):
        child.add_logout_button()
    self.admin_home = AdminHomePage(self.main_layout, status=status)
    self.admin_home.pack(expand=True, fill="both")
    self.main_layout.configure(bg=WHITE)
    self.main_layout.set_admin(self.user, on_approved_button_clicked=self.admin_on_approved_reservation_clicked,on_pending_button_clicked=self.admin_on_pending_reservation_clicked,on_rejected_button_clicked=self.admin_on_rejected_reservation_clicked, on_facilities_button_clicked=self.admin_on_facilities_clicked)
    self.main_layout.rizal_image.configure(bg=WHITE)

  def admin_on_pending_reservation_clicked(self):
    self.remove_page()
    self.admin_home = AdminHomePage(self.main_layout, status=Reservation.PENDING)
    self.admin_home.pack(expand=True, fill="both")

  
  def admin_on_approved_reservation_clicked(self):
    self.remove_page()
    self.admin_home = AdminHomePage(self.main_layout, status=Reservation.APPROVED)
    self.admin_home.pack(expand=True, fill="both")



  def admin_on_rejected_reservation_clicked(self):
    self.remove_page()
    self.admin_home = AdminHomePage(self.main_layout, status=Reservation.REJECTED)
    self.admin_home.pack(expand=True, fill="both")
  
  def admin_on_facilities_clicked(self):
    self.remove_page()
    self.facilities_page = FacilitiesPage(self.main_layout)
    self.facilities_page.pack(expand=True, fill="both")

  def admin_nav_to_add_facility(self):
    self.remove_page()
    self.add_facility = AddFacilityPage(self.main_layout)
    self.add_facility.pack(expand=True, fill="both")

  
  def nav_to_book_a_facility(self):
    self.book_a_facility_page = BookAFacilityPage(self.main_layout)
    self.book_a_facility_page.pack(expand=True, fill="both")
    self.home.pack_forget()

  def nav_to_edit_facility(self,facility):
    self.remove_page()
    self.edit_facility = EditFacilityPage(self.main_layout, facility)
    self.edit_facility.pack(expand=True, fill="both")

  def remove_page(self):
    for widget in self.main_layout.winfo_children():
      if(widget._name.find('page') != -1):
        widget.destroy()
        if(widget._name == 'book_a_facility_page'):
          if(widget.scrollbar != None):
            widget.scrollbar.destroy()
        

  def nav_to_booking_details(self, facility):
    children = self.main_layout.winfo_children()
    for widget in children:
      if(widget._name == 'book_a_facility_page'):
        widget.destroy()
        break

    self.booking_form = BookingForm(self.main_layout, facility)
    self.booking_form.pack(expand=True, fill="both")

  def nav_to_pending_reservations(self,status):
    self.remove_page()
    self.booking_list = BookingList(self.main_layout, status=status)
    self.booking_list.pack(expand=True, fill="both") 

  def show_booking_details(self, reservation):
    self.remove_page()
    self.booking_details = BookingDetails(self.main_layout, reservation)
    self.booking_details.pack(expand=True, fill="both")
