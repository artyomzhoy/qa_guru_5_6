from collections import defaultdict

# словарь, который содержит какое-то значение по умолчанию для ключей/значений

d = defaultdict(int)

d["abc"] = 123
d["def"] += 1  # значение по умолчанию для int = 0
print(d)

d = defaultdict(list)

d["users"].append("Maria")

print(d)

from collections import namedtuple  # неизменяемый тип данных

user = namedtuple("user", ["name", "age"])

user1 = user(name="Maria", age=18)
user2 = user(name="Artyom", age=28)

print(user1)
print(user2)


from collections import OrderedDict  # сортировка

mydict = OrderedDict()
mydict['z'] = 'первый'
mydict['a'] = 'последний'

print(mydict)

mydict.move_to_end('z')
print(mydict)


