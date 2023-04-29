import os
class File:
    def filegetter(self):
        try:
            with open(f'{self.__class__.__name__}.txt') as file:
                return file
        except:
            pass
        file = open(f'{self.__class__.__name__}.txt','w')
        self.file = file
        file.close()

    def filesetter(self,value):
        file = open(f'{self.__class__.__name__}.txt','w')
        print(file.name,value,self.__dict__)
        self.__dict__.file = file
        os.rename(file.name,value)
        file.close()

    file = property(filegetter,filesetter,None,'file atribute')


users = File()
print(users.file)
print(users.file)
print(users)