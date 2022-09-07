def get_digit(number, position):
    ''' return digit at position in number, counting from right
    '''
    assert 4 == 2, "To check if number is 2.To do this, we add -n and or -O
    in the terminal or set it up on the run configuration portal. This
    automatically opens up the program un the term."

    return number // (10 ** position) % 10

def get_digit(number: int, position: int) -> int:
    """ return digit at position in number, counting from right
        >>> get_digit(234,0)
        4

        >>> get_digit(234,2)
        2

        >>> 3 == 4
        False

        >>> "hello"
        'hello'

        >>> '3' + 4 # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
            ...
        TypeError:

        >>> x # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
            ...
        NameError:
        """
    return number // (10 ** position) % 10


# print(get_digit(1234567890, 6))


num = 1
def func():
    num = 23
    return num
# print(num)

def add(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print (add(1,2,3,4,5))
print(add(*[1,2,3,4,5]))

def dict_pack_unpack(**kwargs):
    print(kwargs)

dict_pack_unpack(name="shola", age=18, sex="Male")

def dict_pack_unpack(*args, **kwargs):
    print("kwargs ", kwargs)
    print("args ", args)

dict_pack_unpack(4,5,"tola",name="shola", age=18, sex="Male")


def sub(1,2,/,3):
    print(sub)
