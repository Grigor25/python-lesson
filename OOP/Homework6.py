
class Tesla:
    names = ['Model S', 'Roadster', 'Model 3', 'Cybertruck', 'Model Y', 'Model X']
    body_types = ['Sedan', 'Coupe', 'Sedan', 'Truck', 'SUVS', 'SUVS']
    engine_types = ['Electric', 'Electric', 'Electric', 'Electric', 'Electric']
    set_iter = []

    def __iter__(self):
        if not self.set_iter:
            return iter(self.names)
        else:
            print(super())
            return iter(self.__dir__()[self.set_iter])
    def set_by_iter(self,value):
        self.set_iter = value

car = Tesla()
car.set_by_iter('body_types')
for item in car:
    print(item)