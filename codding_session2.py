# ----1----

print('----1----')
import math


def cylinder_area(height, radius):
    def circle_area(radius):
        s_circle = radius ** 2 * math.pi
        return s_circle

    circle_area(3)

    def circumference(radius):
        s_length = 2 * radius * math.pi
        return s_length

    circumference(3)

    def rectangle_area(length, width):
        s_rectangle = length * width
        return s_rectangle

    rectangle_area(4, 8)
    s_cylinder = circumference(radius) * (height + radius)
    print(s_cylinder)


cylinder_area(3, 2)


# ----2----
print('----2----')

def count_args(*args):
    print(len(args))


count_args(1, 3, 5)


# ----3----

print('----3----')


def check_sum(*numbers):
    total = 0
    for n in numbers:
        total += n
    if total < 50:
        print('not enough')
    else:
        print('verification passed')


check_sum(16, 28, 10)


# ----4----
print('----4----')

def info_kwargs(**kwargs):
    for key, value in sorted(kwargs.items(), key=lambda x: x[0].lower()):
        print(f"{key} = {value}")


info_kwargs(first_name="John", last_name="Doe", AGE=33)


# ----5----
print('----5----')
def create_actor(**kwargs):
    actor_data = {}
    for key, value in kwargs.items():
        actor_data[key] = value
    return actor_data


actor = create_actor(name="Tom Hanks", age=65, nationality="American")
print(actor)


# ----6----
print('----6----')
def multiply(value):
    if not hasattr(multiply, "stored_value"):
        multiply.stored_value = value
    result = value * multiply.stored_value
    multiply.stored_value = value
    return result

print(multiply(5))
print(multiply(2))
print(multiply(4))