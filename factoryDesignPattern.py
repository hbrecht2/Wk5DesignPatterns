import abc

class User(metaclass=abc.ABCMeta):
    def __init__(self, username, displayName):
        self.username = username
        self.displayName = displayName

    @abc.abstractmethod
    def getUserType(self):
        pass
    
    def __str__(self):
        return "{}: {}".format(self.__class__. __name__, self.displayName)
    
    
class Guest(User):
    def getUserType(self):
        return "guest"
    
class Blogger(User):
    def getUserType(self):
        return "blogger"
    
class UserFactory(object):
   @classmethod
   def create(cls, name, *args):
      name = name.lower().strip()

      if name == 'guest':
         return Guest(*args)
      elif name == 'blogger':
         return Blogger(*args)
        
def main():
    print(UserFactory.create('blogger', 'user1', 'Luke'))
    print(UserFactory.create('Guest', 'user2', 'Han'))
    
main()
      