import requests
import json
import page_objects.base_page
import api.api_body
import globals.info

gender = {"f": 'Дорогая', "m": "Дорогой"}

list = [
    ['Алекса', 44, 1349595, gender['m']],
    ['Алекса', 29, 1349595, gender['m']],
    ['Надя', 84, 1349595, gender['f']]
]
for name, age, balance, gender in list:
    print(f"Здраствуйте {gender} {name}, ваш возвраст {age}, баланс счета {balance}")

a = ['1', '2', '3']
b = []
for result in range(1):
    b.extend(a)

print(b)

aaa = "Alexander Ivanov 95 56".split()
some_disct = {}
some_disct['first_name'] = aaa[0]
print(some_disct)


def receive_factorial(n):
    pr = 1
    for i in range(2, n + 1):
        pr = pr * i
    return pr


def get_some_func(x):
    if x == 4:
        return True
    return False


print(get_some_func(2))

some_list = {
    'user': {'name': 'michail', 'age': 22},
    'user2': {'name': 'yuriy', 'age': 34},
}

z = [some_list[a]['name'] for a in some_list]
print(z)


def yields_func():
    for x in range(10):
        yield x


s = yields_func()
print(next(s))
print(next(s))

xz = [-1, -2, 3, -55]
m = map(abs, xz)
for result in m:
    print(result)


def some_random_func(value):
    def inner_func(x):
        y = value + x
        return print(f"Ваш счет {y}")

    return inner_func


xz = some_random_func(4)
print(xz(99))


def new_decorator(func):
    def inner_func(*args, **kwargs):
        print("func1")
        func(*args, **kwargs)

    return inner_func


def new_decorator2(func):
    def inner_func2(id, *args, **kwargs):
        print("func2")
        func(id, *args, **kwargs, )

    return inner_func2


@new_decorator
@new_decorator2
def my_func(id, name, age, balance, status):
    return print(id, name, 44 + age, balance, status)


print(my_func(name='alex', age=44, balance=56, status='married', id=999))
print(my_func(name='alex88888', age=44, balance=56, status='married', id=999))


def create_pet():
    #    category_id = page_objects.base_page.BasePage.random_with_N_digits(4)
    #    category_name = page_objects.base_page.BasePage.randomWord(10)
    request = requests.post("https://petstore.swagger.io/v2/pet",
                            json=api.api_body.pet_app_body(category_id=globals.info.category_id,
                                                           category_name=globals.info.category_name))
    json_body = request.json()
    assert json_body['category']['id'] == globals.info.category_id
    assert json_body['category']['name'] == globals.info.category_name
    return json_body


print(create_pet())


class Car:
    model = "BWM"
    engine = 1.6


class Person:
    name = "Ivan"
    age = 30


a = getattr(Person, 'balance', 100)
print(Person.__getattribute__(Person, 'name'))
Person.x = 400
setattr(Person, 'x', 800)
print(Person.x)
delattr(Person, 'name')
print(Person.x)

z = Person()
z.age = 90
print(z.age)


class User:

    def __init__(self, name, age):
        self.name = name
        if not isinstance(self.name, str):
            raise Exception("only str type")
        else:
            pass
        self.age = age
        if not isinstance(self.age, int):
            raise Exception("only int type")
        else:
            pass

    def change_user_name(self, name):
        self.name = name
        return print(f" the user name is {self.name}")

    def change_user_age(self, age):
        self.age = age
        return print(f" the user age is {self.age}")


user1 = User("44", 22)
print(user1.name)


# print(user1.change_user_name('Alex'))
# print(user1.change_user_age(44))


class Point:

    def __init__(self, coord_x=0, coord_y=0):
        self.move_to(coord_x, coord_y)

    def move_to(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def go_home(self):
        self.move_to(0, 0)


p1 = Point(3, 4)
p2 = Point(-2, -4)
p3 = Point()
print(p3.x, p3.y)
p3.move_to(4, 5)
print(p3.x, p3.y)
p3.go_home()
print(p3.x, p3.y)


class Test:
    some_dict = {
        'name': 'Alex',
        'age': 54
    }

    def __init__(self):
        self.__dict__ = Test.some_dict


a1 = Test()
print(a1.__dict__)


class SomeDecors:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        if not isinstance(name, (str)):
            raise Exception('Only string')
        if not isinstance(balance, (int, float)):
            raise Exception('Only string')

    @property
    def get_balance(self):
        return print(self.balance)

    @get_balance.setter
    def get_balance(self, value):
        self.balance = value


#    @get_balance.deleter
#   def get_balance(self):
#       del self.balance


user00 = SomeDecors('Alex', 9090)
user00.get_balance = 1000
print(user00.get_balance)


class TriangleCalculation:
    def __init__(self, coord_x):
        self.coord_x = coord_x
        self.value = None

    @property
    def get_value(self):
        return self.coord_x

    @get_value.setter
    def get_value(self, value):
        self.coord_x = value
        self.value = None

    @property
    def area(self):
        self.value = self.coord_x ** 2
        return self.value


user000 = TriangleCalculation(2)
print(user000.area)
user000.get_value = 4
print(user000.area)


class SomeClass2:

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"The object Lion - {self.name}"

    def __str__(self):
        return f"The Lion - {self.name}"

    def equal(self, zero):
        if self.value == zero:
            print('nice')


aaa = SomeClass2("alex", 44)
print(aaa.equal(44))


class Testo:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_swing(self):
        return print(f"{self.name} can swing")

    def __str__(self):
        return (f"{self.name} started")


class Testo2:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_swing(self):
        return print(f"{self.name} can swing")

    def __str__(self):
        return (f"{self.name} started")


au1 = Testo('Alex', 77)
au2 = Testo2("Semen", 88)

result = [au1, au2]
for printing in result:
    print(printing, printing.get_swing())


class Nasledovanie:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def can_swing(self):
        return print(self.name, "can swing")


class Doctor(Nasledovanie):

    def can_heal(self):
        return print(self.name, "can heal")

    def can_sell(self):
        return print((self.name, "can sell medical supplies"))


class Architector(Doctor):

    def __init__(self, name, age, experience):
        super().__init__(name, age)
        self.experience = experience

    def can_build(self):
        super().can_swing()
        return print(self.name, "can build")


user0000 = Architector('Alex', 99, '3 years')
print(user0000.can_build())


class ExpectionsTest:

    def __init__(self, name, age):
        self.name = name
        self.age = age


try:
    print('to the zeros')
    zeros = ExpectionsTest('Alex')
except TypeError:
    zeros = ExpectionsTest('Alex',22)
    print(zeros.name,age)
