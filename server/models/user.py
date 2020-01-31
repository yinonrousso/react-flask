class User(dict):

  def __init__(self, uid = 0, fname = '', lname = '', email = ''):
    dict.__init__(self, uid=uid, fname=fname, lname=lname, email=email)
    self.uid = uid
    self.fname = fname
    self.lname = lname
    self.email = email

  def __eq__(self, other):
    return self.uid == other.uid
