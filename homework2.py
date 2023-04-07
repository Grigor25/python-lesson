class Car():
    wheels_count = 4
    def __init__(self,horsepower,weight,engine_type,headlights_count):
        self.horsepower = horsepower
        self.engine_type = engine_type
        self.headlights_count = headlights_count
        self.weight = weight
    def max_speed(self):
        return self.horsepower / self.weight * 1500
    # @classmethod
    # def change_horsepower(cls,val):
    #     print(val,'@classmethod')
    #     cls.horsepower = val
    @staticmethod
    def change_horsepower(val):
        Car.horsepower = val
x5 = Car(180,2600,'V6',2)
mustang = Car(220,1800,'V8',2)
print(mustang.max_speed())
print(x5.max_speed())


class Bus(Car):
    def __init__(self,horsepower, weight, engine_type, max_seats, busy_seats=0):
        self.horsepower = horsepower
        self.engine_type = engine_type
        self.weight = weight
        self.max_seats = max_seats
        self.busy_seats = busy_seats
    def increase_busy_seats(self,people):
        self.busy_seats += people
    def free_seats(self):
        return self.max_seats - self.busy_seats