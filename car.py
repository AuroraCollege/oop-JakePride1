class Car:
    def __init__(self,year,model,make):
        self.year = year
        self.model = model
        self.make = make
        
    def display_info(self):
        print(self.year, self.model, self.make)
        
year_1 = input("when did your car come out:")
model_1 = input("what model is your car:")
make_1 = input("what make is your car:")
car1 = Car(year_1,model_1,make_1)
car1.display_info()