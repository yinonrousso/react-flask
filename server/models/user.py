class User(dict):

  def __init__(self, uid = 0, name = '', email = ''):
    dict.__init__(self, uid=uid, name=name, email=email)
    self.uid = uid
    self.name = name
    self.email = email

  def __eq__(self, other):
    return self.uid == other.uid
