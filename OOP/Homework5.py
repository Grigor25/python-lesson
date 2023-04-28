
import re
class FilterText:
    text = '055-445-789 E.Mask 124.06.2014 093-587-135 Nemo 1.09.1887 E.Auditore 24.17.2020 096-2288-987 R.Rocknrolla'
    def __init__(self):
        self.names = re.findall("[A-Z]{1}.[A-Z]{1}[a-z]*" ,self.text)
        self.dates = re.findall("[0-9]{1,2}$.[0-9]{2}.[0-9]{4}" ,self.text)
        self.phones = re.findall("[0-9]{3}-[0-9]{3}-[0-9]{3}" ,self.text)
    def __getitem__(self, index):
        return self.text.split(' ')[index]
    def __setitem__(self, key, value):
        li = self.text.split(' ')
        li[key] = str(value)
        self.text = " ".join(str(item) for item in li)

man = FilterText()
man[0] = 54
print(man.text)