# 1

# class Car:
#     def __init__(self,brand, model, color, year, started=False):
#         self.brand = brand
#         self.model = model
#         self.color = color
#         self.year = year
#         self.started = started
#     def start(self):
#         self.started = True
#         print('br br br start')
#     def stop(self):
#         self.started = False
#         print('stop')
# car = Car('Bmw','x5','black','2014')
# car.start()
# car.stop()

# 2
class Car:
    def __init__(self,brand, model, color, year, started=False):
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year
        self.started = started
    def start(self):
        print('br br br start')
    def stop(self):
        print('stop')
    def brand_model(self):
        print(self.brand,' ',self.model)
    def car_age(self):
        print(2023 - self.year)
    def change_color(self,new_color):
        print(self.color)
        self.color = new_color
        print(self.color)
x5 = Car('BMW','x5','Black',2014)
c300 = Car('Mercedes','c300','white',2018)



#  construktor@ ashxatum e erm menq stextsum enq object clasic __init__ methodov isk destructor@ erb menq jnjum enq object@
#   kanchvum e __del__  method@
# class Car(object):
#
#     def __init__(self):
#
#         self.str1 = ‘str’
#
#         print('stextsvum e')
#
#     def __del__(self):
#
#         print('Jnjvum e')
