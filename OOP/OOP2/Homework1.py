class Car:
    def __init__(self,brand, model, color, year, started=False):
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year
        self.started = started
    def start(self):
        print('br br br')
        self.started = True
        print(self.__dict__)

    def stop(self):
        print('stop')
        self.started = False

    def model_year(self):
        return 2023 - self.year

    def color_change(self,color):
        self.color = color

bmv = Car('Bmw','X5','Red','2010')
hyundai = Car('Hyundayi','Elantra','Black','2014')
bmv.color_change('Grey')

print(bmv.start())