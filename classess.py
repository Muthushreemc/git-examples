class CarOfDecade:
  def __init__(self, year, make, model, price):
    self.year = year
    self.make = make
    self.model = model
    self.price = price

  def display_info(self):
      print(f"Car Make: {self.make}, Model: {self.model}, Year: {self.year}, Price: {self.price}")

  def start_engine(self):
        print(f"The engine of the {self.year} {self.make} {self.model} is now running..")

car1 = CarOfDecade(2015,"Toyota","Camry",20000)
car1.display_info()
car1.start_engine()

car2 = CarOfDecade("Honda", "Civic", 2018, 25000)
car2.display_info()
car2.start_engine()
  
