add = lambda x, y: x + y
sub = lambda x, y: x - y
print(add.__name__)
print(sub.__name__)

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def operate(e, f, fn):
    return fn(e, f)

val_add = operate(4, 6, add)
val_sub = operate(6, 3, sub)
val_mul = operate(5, 4, mul)
print(val_add)
print(val_sub)
print(val_mul)

# Now we use lambda to define our function on the go
val_div = operate(35, 4, lambda x, y: x/y)
val_add = operate(35, 4, lambda x, y: x + y)
val_sub = operate(35, 4, lambda x, y: x - y)
val_mul = operate(35, 4, lambda x, y: x * y)
print(val_div)


def multiple(q, fn):
    return fn(q)
def double(a):
    return a * a
def triple(a):
    return a * a * a

val_double = multiple(3, lambda q: q * q)
print(val_double)
val_triple = multiple(3, lambda q: q * q * q)
print(val_triple)

names = ["Amaka", "Segun", "comb", "Samson", "foil"]
print([name.istitle() for name in names])

all([name.istitle() for name in names])

# test using a function all
print(all([1,2,23,3,4,5,5,0]))
print(all([1,2,23,3,4,5,5]))
print(all([True, False, True]))
print(all([True, True, True]))

# using keyword ANY in accessing a dictionary
print(any([True, True, True]))

# using keyword ANY in accessing a dictionary

peoples =[
    {"name": "Omosetan" "Omorele", "age": 30, "Year_of_exp": 4, "language": ["python", "java"]},
    {"name": "John" "Doe", "age": 25, "Year_of_exp": 2, "language": ["JavaScript", "C#"]},
    {"name": "Amaka" "Stephen", "age": 19, "Year_of_exp": 5, "language": ["python"]},
    {"name": "Florence" "Segun", "age": 28, "Year_of_exp": 4, "language": ["JavaScript", "Python", "java", "HTML"]},
    {"name": "Ernest" "Adeola", "age": 30, "Year_of_exp": 4, "language": ["JavaScript", "java", "Kotlin"]},
]
print([people["age"] <= 20 and "Python" in people["language"] for people in peoples])
print(any([people["age"] <= 20 and people["language"] == 'Python' for people in peoples]))
print([people["name"] for people in peoples if people["age"] <= 28 and "Python" in peoples])

map_object = map(lambda x: x**2, range(1, 10))
lst1 = list(map(lambda x: x**2, range(1, 10)))
lst2 = list(map(lambda x: x**2, range(1, 10)))
print("1", lst1)
print('2', lst2)

lst11 = list(map_object)
lst12 = list(map_object)
#
def isEven(x):
    if x % 2 == 0:
        return True

filter_obj = list(filter(isEven, range(1, 10)))
print(filter_obj)

from functools import reduce
fruits = [ "Apple", "Pear", "Pineapple", "Orange", "Watermenlon", ]
longest_fruit = reduce(lambda x, y: x if len(x) < len(y) else y, fruits)
print(longest_fruit)
print(max(fruits, key=len))
print(sorted(fruits, key=len))
print(sorted(fruits, key=len, reverse=True))

# The diff btw list.sort n sorted:
# sorted ds nt affect the original list
print(sorted(fruits, key=lambda x: x[-1]))

# The Zip built-in function
students = [1, 2, 3, 4]
subject_score = [34, 65, 77, 90]
print(list(zip(students, subject_score, strict=True)))

student_1 = [34, 65, 79, 90]
student_2 = [44, 77, 40, 80]
student_3 = [89, 50, 45, 60]

print(list(zip(student_1, student_2, student_3)))
max_subject_score = [max(subject) for subject in zip(student_1, student_2, student_3)]
print(max_subject_score)