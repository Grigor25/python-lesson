class God:
    def __init__(self,name,hands,power):
        self.first_name = name
        self.counth_of_hands = hands
        self.super_power = power

    def __voice_after_clap(self):
        return 'jlt'

    def clap(self):
        if self.counth_of_hands > 2:
            self.__voice_after_clap()

class Zeus(God):
    pass


class Hercules(Zeus):
    def get_public(self):
        for item in Hercules.mro():
            for attribut in item.__dict__:
                if attribut[0] == '_' or attribut[0] == '_':
                    continue
                else:
                    print(attribut)
    def get_protected(self):
        for item in Hercules.mro():
            for attribut in item.__dict__:
                if attribut[0] == '_' and attribut[1] != '_':
                    print(attribut)
                else:
                    continue

    def get_private(self):
        for item in Hercules.mro():
            for attribut in item.__dict__:
                if attribut[0:2] == '__':
                    print(attribut)
                else:
                    continue

hercules = Hercules('Hercules',3,'might')
hercules.get_private()
