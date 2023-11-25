class Visitor:
  def __init__(self,name):
    self.name = name

  @property 
  def name(self):
    return self.name
  
  @name.setter
  def name(self, name):
    if isinstance(name, str) and 1 <= len(name) <= 15: 
      self.name = name
    else: 
      raise Exception

  def trips(self, new_trip = None):
    from classes.trip import Trip 
    pass

  def national_parks(self, new_national_park = None):
    from classes.national_park import NationalPark
    pass


# - `Visitor property name`
#   - Returns the visitor's name
#   - Names must be of type `str`
#   - Names must be between 1 and 15 characters, inclusive
#   - Should **be able** to change after the visitor is instantiated
