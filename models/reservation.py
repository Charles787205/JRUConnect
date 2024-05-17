from . import DatabaseModel
from enum import Enum
import datetime
from .facility import Facility
from .student import Student


class Reservation(DatabaseModel):

  PENDING = 'PENDING'
  APPROVED = 'APPROVED'
  REJECTED = 'REJECTED'
  


  def __init__(self, **kwargs):
    self.id = kwargs.get('id', -1)
    self.facility_id = kwargs.get('facility_id', -1)
    self.student_id = kwargs.get('student_id', -1)
    self.date_reserved = kwargs.get('date_reserved', '')
    self.facility = kwargs.get('facility', None)
    self.time_from = kwargs.get('time_from', '')
    self.time_to =kwargs.get('time_to', '')
    self.notes = kwargs.get('notes', '')
    self.status = kwargs.get('status', Reservation.PENDING)
    self.created_at = kwargs.get('date_created', '')
    self.updated_at = kwargs.get('date_updated', '')
    self.user_id = kwargs.get('user_id', -1)

  def add_reservation(self):
   try:
     
    if(self.mydb == None):
      self.connect_db()
    mycursor = self.mydb.cursor(dictionary=True)
    query = "INSERT INTO reservations (facility_id, user_id, date_reserved, time_from, time_to, notes) VALUES (%s,%s, %s,%s,%s,%s)"

    values = (self.facility_id, self.student_id, self.date_reserved, self.time_from, self.time_to, self.notes)
    mycursor.execute(query, values)
    self.mydb.commit()
    self.mydb.close()
    return True
   except Exception as e:
     print(e)
     return False
   

  def get_reservations_by_status_user_id(self, status=PENDING):
    if(self.mydb == None):
      self.connect_db()
    mycursor = self.mydb.cursor(dictionary=True)
    query = "SELECT * FROM reservations WHERE status = %s AND user_id = %s ORDER BY date_reserved DESC"
    values = (status, self.student_id)
    mycursor.execute(query, values)
    results = mycursor.fetchall()
    reservations = []
    for result in results:
      #result['date_reserved'] = result['date_reserved'].strftime("%B %d, %Y")
      reservations.append(Reservation(**result))
    
    for reservation in reservations:
      facility = Facility().get_facility_by_id(reservation.facility_id)
      reservation.facility = facility
    self.mydb.close()
    return reservations
   
  def get_reservations(self):
    if(self.mydb == None):
      self.connect_db()
    mycursor = self.mydb.cursor(dictionary=True)
    query = "SELECT * FROM reservations"
    
    mycursor.execute(query)
    results = mycursor.fetchall()
    reservations = []
    for result in results:
      #result['date_reserved'] = result['date_reserved'].strftime("%B %d, %Y")
      reservations.append(Reservation(**result))
    
    for reservation in reservations:
      facility = Facility().get_facility_by_id(reservation.facility_id)
      reservation.facility = facility
      
      reservation.student = Student().get_student_by_id(reservation.user_id)
    self.mydb.close()
    return reservations
  

  def get_reservations_by_status(self, status):
    
    if(self.mydb == None):
      self.connect_db()
    mycursor = self.mydb.cursor(dictionary=True)
    query = "SELECT * FROM reservations WHERE status = %s"
    values = (status,)
    mycursor.execute(query, values)
    results = mycursor.fetchall()
    reservations = []
    
    for result in results:
      #result['date_reserved'] = result['date_reserved'].strftime("%B %d, %Y")
      reservations.append(Reservation(**result))
    
    for reservation in reservations:
      facility = Facility().get_facility_by_id(reservation.facility_id)
      reservation.facility = facility
      reservation.student = Student().get_student_by_id(reservation.user_id)
    self.mydb.close()
    return reservations

  def update_status(self, status):
    if(self.mydb == None):
      self.connect_db()
    mycursor = self.mydb.cursor(dictionary=True)
    query = "UPDATE reservations SET status = %s WHERE id = %s"
    values = (status, self.id)
    mycursor.execute(query, values)
    self.mydb.commit()
    self.mydb.close()
    return True