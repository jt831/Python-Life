# Beautiful is better than ugly

from collections import OrderedDict

ort = OrderedDict()

ort['jen'] = 'python'
ort['mike'] = 'Java'

orts = {'jen': 'python', 'make': 'java'}
for man, language in orts.items():
    print(man.title() + " " + language.title())
