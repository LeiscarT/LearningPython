import collections
import pprint

fileInput = input("ingrese el nombre del archivo: ")
with open (fileInput, 'r') as info:
    count = collections.Counter(info.read().upper)
    value = pprint.pformat(count)
    print(value)