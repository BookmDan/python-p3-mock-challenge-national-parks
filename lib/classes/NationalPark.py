class NationalPark:
  all = []
  def __init__(self, name):
    self.name = name 
    self._trips = []
    self._visitors = []

    NationalPark.all.append(self)
  @property
  def name(self):
    return self._name

  @name.setter
  def name(self, name):
    if isinstance(name,str) and len(name) >=3 and not hasattr(self, 'name'):
      self._name = name
    else: 
      raise Exception ("name must be a string greater tahn 3 characters!")

  # def trips(self, new_trip = None):
  #   from classes.Trip import Trip
  #   pass
  def trips(self, new_trip = None):
    return list(set(self._trips))


  # def visitors(self, new_visitor = None):
  #   from classes.Visitor import Visitor
  #   pass

  def visitors(self):
    return list(set(self._visitors))

  def total_visits(self):
    return len(self._trips)

  def best_visitor(self):
    if len(self._visitors) == 0:
      return None 
    
    # visitor_frequencies={}
    # for visitor in self._visitors:
    #   if visitor not in visitor_frequencies:
    #     visitor_frequencies[visitor] = 0
    #   else:
    #     visitor_frequencies = 1

    # return max(visitor_frequencies, key = visitor_frequencies.get)
    return max(self._visitors, key=self._visitors.count)
  
  @classmethod
  def most_visited(cls):
    curr_park = None 
    curr_max_visits = 0 

    for national_park in cls.all:
      if len(national_park._trips) > curr_max_visits:
        curr_park = national_park
        curr_max_visits = len(national_park._trips)

    return curr_park

  

# - `NationalPark __init__(self, name)`
#   - NationalPark is initialized with a name, as a string
# - `NationalPark property name`
#   - Returns the national_park's name
#   - Names must be of type `str`
#   - Names length must be greater or equal to 3 characters
#   - Should **not be able** to change after the national_park is instantiated
#   - _hint: hasattr()_