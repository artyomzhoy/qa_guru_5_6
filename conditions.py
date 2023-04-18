
# Boolean - 3 состояния

b = bool

t = True
f = False
n = None

# if/elif/else - на примере кода ответа

if True:
    print("истина!")
else:
    print("ложь!")

code = 500

if 100 <= code < 400 or code == 418:
    print("Хороший ответ!")
else:
    print("Плохой ответ!")


try:
    1 / 0
except ZeroDivisionError:
    print()

# Пустые объекты - false

print(bool("abc"))
print(bool(""))
print(bool(123))
print(bool(-123))
print(bool(0))
print(bool([0, ""]))
print(bool([]))
print(bool({"key": "value"}))
print(bool({}))

user_list = []

if user_list:
    print(user_list)

items_count = 0

if items_count:
    print(items_count)
