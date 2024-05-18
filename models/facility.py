from . import DatabaseModel
class Facility(DatabaseModel):
  def __init__(self, **kwargs):
    self.name = kwargs.get('name', '')
    self.image_url = kwargs.get('image_url', '')
    self.location = kwargs.get('location', '')
    self.seating_capacity = kwargs.get('seating_capacity', 0)
    self.id = kwargs.get('id', -1)

  def get_facilites():
    self = Facility()
    if(self.mydb == None):
      self.connect_db()
    mycursor = self.mydb.cursor(dictionary=True)
    query = "SELECT * FROM facilities"
    mycursor.execute(query)
    results = mycursor.fetchall()
    self.mydb.close()
    facilities = []
    print(results)
    for result in results:
      facilities.append(Facility(**result))
    return facilities
  

  def get_facility_by_id(self, id):
    if(self.mydb == None):
      self.connect_db()
    mycursor = self.mydb.cursor(dictionary=True)
    query = "SELECT * FROM facilities WHERE id = %s"
    values = (id,)
    mycursor.execute(query, values)
    result = mycursor.fetchone()
    self.mydb.close()
    return Facility(**result)
  
  def save(self):
    if(self.mydb == None):
      self.connect_db()
    mycursor = self.mydb.cursor(dictionary=True)
    query = "INSERT INTO facilities (name, location, seating_capacity, image_url) VALUES (%s, %s, %s, %s)"
    values = (self.name, self.location, self.seating_capacity, self.image_url)
    mycursor.execute(query, values)
    self.mydb.commit()
    self.mydb.close()

  def edit(self):
    print(self.id)
    if(self.mydb==None):
      self.connect_db()
    mycursor = self.mydb.cursor(dictionary=True)
    query = "UPDATE facilities SET name = %s, location = %s, seating_capacity = %s, image_url = %s WHERE id = %s"
    values = (self.name, self.location, self.seating_capacity, self.image_url, self.id)
    mycursor.execute(query, values)
    self.mydb.commit()
    self.mydb.close()

  
    