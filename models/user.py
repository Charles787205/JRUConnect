from . import DatabaseModel
import re
class User(DatabaseModel):
  STUDENT = 'STUDENT'
  ADMIN = 'ADMIN'
  
  def __init__(self, **kwargs):
    self.first_name = kwargs.get('first_name', '').lower()
    self.middle_name = kwargs.get('middle_name', '').lower()
    self.last_name = kwargs.get('last_name', '').lower()
    self.email = kwargs.get('email', '')
    self.password = kwargs.get('password', '')
    self.confirm_password  = kwargs.get('confirm_password', '')

    self.id = kwargs.get("id", -1)
    self.user_type = kwargs.get('user_type', self.ADMIN)

  def add_user(self) -> bool:
    if(self.mydb == None):
      self.connect_db()
    mycursor = self.mydb.cursor()
    query = "INSERT INTO users (first_name, middle_name, last_name, email, password, user_type) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (self.first_name, self.middle_name, self.last_name, self.email, self.hash_string(self.password), self.user_type)
    
    mycursor.execute(query, values)
    self.mydb.commit()
    self.id = mycursor.lastrowid
    
    self.mydb.close()
    return self.id
    

  def check_register_info(self) -> bool:
    
    is_nothing_blank = self.first_name != "" and self.middle_name != "" and self.last_name != "" and self.email != "" and self.password != "" and self.confirm_password != "" 

    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    is_email_valid = re.fullmatch(regex, self.email)
    is_password_match = self.confirm_password == self.password
    if not is_nothing_blank:
      return False, "Incomplete Information"
    elif not is_email_valid:
      return False, "Invalid Email Address"
    elif not is_password_match:
      return False, 'Password do not match'
    else:
      return True, 'Success'

    
  def get_user(self):
    if(self.mydb == None):
      self.connect_db()
    mycursor = self.mydb.cursor(dictionary=True)
    query =  "SELECT * FROM users WHERE email = %s AND password = %s"
    values = (self.email, self.hash_string(self.password))
    mycursor.execute(query, values)
    #self.mydb.close()
    result = mycursor.fetchone()
    print(result)
    return result
    
  def get_full_name(self):
    return f"{self.first_name} {self.middle_name} {self.last_name}"
  
  def get_user_by_id(self):
    if(self.mydb == None):
      self.connect_db()
    mycursor = self.mydb.cursor(dictionary=True)
    query = "SELECT * FROM users WHERE id = %s"
    values = (self.id,)
    mycursor.execute(query, values)
    result = mycursor.fetchone()
    self.mydb.close()
    if(result):
      self.first_name = result['first_name']
      self.middle_name = result['middle_name']
      self.last_name = result['last_name']
      self.email = result['email']
      self.user_type = result['user_type']
      return True
    else :
      return False