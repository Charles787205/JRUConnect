from . import user
class Student(user.User):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.year_level = int(kwargs.get('year_level', -1))
    self.course = kwargs.get('course', '')
    user_type = user.User.STUDENT

  def add_data_from_dict(self, data):
    
    self.year_level = data.get('year_level', -1)
    self.course = data.get('course', '')

  def check_register_info(self) -> bool:
    info = super().check_register_info()
    if(not info[0]):
      return info
    elif not self.year_level != "" and self.course != "":
      return False, "Incomplete Information"
    
    return super().check_register_info()[0] and self.year_level != "" and self.course != "", "Success"
  
  def add_user(self):
    if(self.mydb == None):
      self.connect_db()
    mycursor = self.mydb.cursor()
    query = "INSERT INTO students (id, course, year_level) VALUES (%s,%s, %s)"
    if(self.check_register_info()):
      self.id = super().add_user()
      print(self.id)
      values = (self.id, self.course, self.year_level)

      mycursor.execute(query, values)
      self.mydb.commit()
      self.id = mycursor.lastrowid
      self.mydb.close()
      return self.id
    self.mydb.close()
  
  def get_course_and_year_level(self):
    if(self.mydb == None):
      self.connect_db()
    mycursor = self.mydb.cursor(dictionary=True)
    query = "SELECT course, year_level FROM students WHERE id = %s"
    values = (self.id,)
    mycursor.execute(query, values)
    result = mycursor.fetchone()
    self.mydb.close()
  
    return result
 
  
  def get_student_by_id(self, student_id):
    if(self.mydb == None):
      self.connect_db()
    
    student = Student(id=student_id)
    student.get_user_by_id()
    mycursor = self.mydb.cursor(dictionary=True)
    query = "SELECT * FROM students WHERE id = %s"
    values = (student_id,)
    mycursor.execute(query, values)
    result = mycursor.fetchone()
    student.year_level = result['year_level']
    student.course = result['course']
    self.mydb.close()
    return student