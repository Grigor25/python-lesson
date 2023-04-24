nam = 'ss'
print()

class Tesla:
    names = ['Model S', 'Roadster', 'Model 3', 'Cybertruck', 'Model Y', 'Model X']
    body_types = ['Sedan', 'Coupe', 'Sedan', 'Truck', 'SUVS', 'SUVS']
    engine_types = ['Electric', 'Electric', 'Electric', 'Electric', 'Electric']
    value = 'names'

    def __iter__(self):
        return iter(self[self.value])
    def set_iter_by(self,value):
        self.value = value

car = Tesla()
# car.set_iter_by('body_types')
for item in car:
    print(item)