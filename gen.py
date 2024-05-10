from sys import getsizeof
from faker import Faker
faker = Faker()

#numbers = [x for x in range(1,10_000_000_000_000+1)]
numbers2 = (x for x in range(1,10_000_000_000_000+1))
#print(numbers)
#print(getsizeof(numbers))
print(getsizeof(numbers2))
print(type(numbers2))

dictionary = {
    1:2,
    2:2
}
set = {1,2,3,4,5,5,6,7,2,4,1}
print(set)

touple = (1,2,3,4,5,6,1,2,3,4)
print(touple)
print(type(touple))
def generator():
    for x in range(1000_000):
        yield faker.name()

names = generator()
print(type(names))
print(names)
for name in names:
    print(name)
print(getsizeof(names))