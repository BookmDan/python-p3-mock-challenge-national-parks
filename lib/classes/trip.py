class Trip:
  all = []
  def __init__(self, visitor, national_park, start_date, end_date):
    self.visitor= visitor
    self.national_park = national_park
    self.start_date = start_date  
    self.end_date = end_date

    self.visitor._trips.append(self)
    self.visitor._national_parks.append(self.national_park)

    self.national_park._trips.append(self)
    self.national_park._visitors.append(self.visitor)

    Trip.all.append(self)
  
  @property
  def visitor(self):
    return self._visitor
  
  @visitor.setter
  def visitor(self, visitor):
    from classes.Visitor from Visitor

    if isinstance(visitor, Visitor):
      self._visitor = visitor
    else: 
      raise Exception("visitor must be instance of class Visitor")
  
  @property
  def national_park(self):
    return self._national_park

  @national_park.setter
  def national_park(self, national_park):
    from classes.NationalPark import national_park

    if isinstance(national_park, NationalPark):
      self._national_park = national_park
    else:
      raise Exception("National park must be an instance of class NationalPark")

  @property
  def start_date():
    return self._start_date
  
  @start_date.setter
  def start_date(self, start_date):
    if type(start_date ) == str and len(start_date) >= 7:
      self._start_date = start_date
    else:
      raise Exception("Start date must be a string greater than 6 characters!")
    
  @property
  def end_date(self):
    return self._end_date
  
  @end_date.setter
  def end_date(self, end_date):
    if type(end_date) == str and len(end_date) >= 7:
      self._end_date = end_date
    else :
      raise Exception("End date must be a string of greater than 6 characters")
    
  