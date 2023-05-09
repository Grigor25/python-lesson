class Car:
    headlights_count = 4
    def __init__(self,horsepower, weight, engine_type, wheels_count):
        self.horsepower = horsepower
        self.weight = weight
        self.engine_type = engine_type
        self.wheels_count = wheels_count

    def max_speed(self):
        return self.horsepower / self.weight * 1500

    staticmethod
    def weight_change(self,weigth):
        self.weight = weigth
        print(self.__dict__)
    # classmethod
    # def weight_change(new_weight):
    #     weight = new_weight


bmw = Car(1500,200,8,4)
opel = Car(400,50,20,4)
print(bmw.max_speed(),opel.max_speed())
print(40000*4.6)
print(500*385)