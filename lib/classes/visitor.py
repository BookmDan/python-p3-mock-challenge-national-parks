class Visitor:
  def __init__(self,name):
    self.name = name
  
    self._trips = []
    self._national_parks = []
  

  @property 
  def name(self):
    return self._name
  
  @name.setter
  def name(self, name):
    if isinstance(name, str) and 1 <= len(name) <= 15: 
      self._name = name
    else: 
      raise Exception ("Name should be a string between 1 and 15 characters, inclusive!")

  def trips(self, new_trip = None):
    from classes.Trip import Trip 
    pass

  def national_parks(self, new_national_park = None):
    from classes.NationalPark import NationalPark
    pass

  def trips(self):
    return self._trips

  def national_parks(self):
    return list(set(self._national_parks))
  
  def total_visits_at_park(self, park):
    return len([trip for trip in self._trips if trip.national_park == park])
  


# - `Visitor property name`
#   - Returns the visitor's name
#   - Names must be of type `str`
#   - Names must be between 1 and 15 characters, inclusive
#   - Should **be able** to change after the visitor is instantiated
