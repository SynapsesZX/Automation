gender = ['Дорогой', 'Дорогая']
people_list = [['Семен', 45, gender[0]], ['Степан', 55, gender[1]]]
for name, age, gender, in people_list:
    print(f"{gender} {name} твой возраст {age}")


def some_function(x):
    for result in range(1, 10):
        print(x, result, x * result)


print(some_function(2))

a = [45, 6, 7, 8, 9]
b = 'alex'.join([str(i) for i in a])
print(b)


def some_desocrator(func):
    def inner_func(*args, **kwargs):
        func(*args, **kwargs)
        print('Hello')
        print("the cicle ended")

    return inner_func


@some_desocrator
def new_func(name):
    print(name)


print(new_func('Alex'))


class SomeTest:

    def __init__(self, name, balance):
        self.name = name
        if not isinstance(balance, (int, float)):
            raise Exception("only integer or float values")
        self.balance = balance

    @property
    def my_balance(self):
        return self.balance

    @my_balance.setter
    def my_balance(self, value):
        self.balance = value

    def __str__(self):
        return f"your name is {self.name}"


a = SomeTest('alex', 444)

print(str(a))


class Person:

    def can_walk(self):
        return print('can walk')

    #    def can_heal(self):
    #       return print(self.name,'can heal from person')

    def __init__(self, name):
        print('наследование')
        self.name = name


class Sanitar(Person):

    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def can_heal(self):
        return print(self.name, 'sanitar can heal you')


class Doctor(Sanitar, Person):

    def __init__(self, name,age,profession,):
        super().__init__(name,age)
        self.profession = profession



#    def can_heal(self):
#        super().can_heal()
#       return print(self.name,"doc can heal you")


class Architector(Doctor):

    def can_heal(self):
        super().can_heal()
        return print(self.name, " i can heal architector")

    def can_buid(self):
        return print('i can heal you')


a = Doctor(name='Alex',age=22,profession='IT')


class SomeTest:
    def __init__(self,name):
        self.name = name

    def can_walk(self):
         return print(self.name, "can walk")

    def can_eat(self):
         return print(self.name,'can eat')

class SomeTest2:
    def __init__(self, name):
        self.name = name

    def can_walk(self):
        return print(self.name, "can walk")

    def can_eat(self):
        return print(self.name, 'can eat')



a1 = SomeTest('Alex')
a2 = SomeTest2('Semen')

result = [a1,a2]
for learn in result:
    print(learn.can_walk())




class Books:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.books = []

    def can_read(self):
        return print(self.name,'может читать')

    def add_book(self,book):
        return print(self.books + book)




class Author(Books):
    def __init__(self,name,age):
        super(Author, self).__init__(name,age)



author = Books('Yuriy',28)
author.add_book(['Ukraine'])
author.add_book(['Mazepa'])
print(author.books)


