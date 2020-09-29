dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

print(dict1 == dict2)

from collections import OrderedDict

dict3 = OrderedDict({'a': 1, 'b': 2})
dict4 = OrderedDict({'b': 2, 'a': 1})

print(dict3 == dict4)