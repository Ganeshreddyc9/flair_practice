

d = {1:'key'}

print(dir(d))

['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__',
  '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__',
    '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__',
      '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__',
        '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', 
        '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop',
          'popitem', 'setdefault', 'update', 'values']

print(help(d.get))
# get(key, default=None, /) method of builtins.dict instance
#     Return the value for key if key is in the dictionary, else default.

print(help(d.fromkeys))

# fromkeys(iterable, value=None, /) method of builtins.type instance
#     Create a new dictionary with keys from iterable and values set to value.