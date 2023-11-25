class NationalPark:
  def __init__(self, name):
    if isinstance(name, str):
      self.name = name 
      self._trips = []
      self._visitors = []
    else: 
      raise Exception

  @property
  def name(self):
    return self._name

  @name.setter
  def name(self, name):
    if isinstance(name,str) and not hasattr(self, 'name'):
      self._name = name
    else: 
      raise Exception

  def trips(self, new_trip = None):
    from classes.trip import Trip
    pass

  def visitors(self, new_visitor = None):
    from classes.visitor import Visitor
    pass

  def total_visits(self):
    pass

  def best_visitor(self):
    pass


# - `NationalPark __init__(self, name)`
#   - NationalPark is initialized with a name, as a string
# - `NationalPark property name`
#   - Returns the national_park's name
#   - Names must be of type `str`
#   - Names length must be greater or equal to 3 characters
#   - Should **not be able** to change after the national_park is instantiated
#   - _hint: hasattr()_