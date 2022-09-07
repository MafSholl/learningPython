lst = []
for i in range(1, 11):
    lst.append(i)

# list comprehension gives us a one liner
lst_com = [i for i in range(1, 11)]
lst_com_even = [i for i in range(2, 11, 2) if i % 2 == 0]
lst_com_even_and_squared_odds = [i if i % 2 == 0 else i ** 2 for i in range(1, 11)]
lst_input = [int(input("Enter a number: ")) for num in range(1, 6)]
list_nested_for = [(x, y) for x in range(1, 5) for y in range(6, 10)]
upper_names = [name.upper() for name in ["dolapo", "tolani", "florence"]]
len_names = [len(name) for name in ["dolapo", "tolani", "florence"]]
list_of_dicts = [{key: value} for key, value in zip(upper_names, lst_com_even)]
generator_expression = (num for num in range(1, 11))
set_comprehension = {a for a in range(5)}


import sys
print(sys.getsizeof(num for num in range(1, 11*100)))
print(sys.getsizeof(num for num in range(1, 11**10)))

dict_comprehension = {k: v for k, v in zip(range(5), range(5))}

print(lst_com)
print(lst_com_even)
print(lst_com_even_and_squared_odds)
print(lst_input)