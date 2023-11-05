class Car:
  def __init__(self, model, is_manual):
    self.model = model
    self.is_manual = is_manual
  def tell(self):
    if self.is_manual:
      return "manual"
    else:
      return "auto"
  def just_something_else(self):
    return {self.model, self.is_manual}
      
