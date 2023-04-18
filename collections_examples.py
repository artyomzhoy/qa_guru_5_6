
from collections import defaultdict

d = defaultdict(int)

d["abc"] = 123
d["def"] += 1
print(d)

d = defaultdict(list)

d["users"].append("Maria")

print(d)

from collections import namedtuple

user = namedtuple("user", ["name", "age"])

user1 = user(name="Maria", age=18)

print(user1)

from collections import OrderedDict
