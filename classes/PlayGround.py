# n = int(input("Enter an integer; "))
# if n % 2 == 0:
#     print("This is an even number")
# else:
#     print("This is an odd number")
#
# score = int(input("Enter your score: "))
# if 70 >= score <= 100:
#     print("Your grade is A.")
# elif 60 >= score < 70:
#     print("Your grade is B.")
# elif 50 >= score < 60:
#     print("Your grade is C.")
# elif 40 >= score < 50:
#     print("Your grade is D.")
# elif 0 >= score < 40:
#     print("Your grade is F.")

# loop = 1
# while loop <= 10:
#     print(loop, end=' ')
#     loop += 1
# print()

# word = "hello"
# for i in word:
#     print(i, end=' ')
# print

# userInput = int(input("Enter an input: "))
# i = 1
# sum_of_factors = 0
# while i <= (userInput // 2):
#     possibleFactorial = userInput % i
#
#     if possibleFactorial == 0:
#         print(i, end=' ')
#         sum_of_factors += i
#     i += 1
# print()
# print('Sum of the factors of this number is: ', sum_of_factors)
# if sum_of_factors < userInput:
#     print("This is a deficient number")
# else:
#     print("This is an abundant number")

# star = "*"
# for i in range(1, 21, 2):
#     print(f"{star * i: ^20}")

# lst = list("abcdefghijk")
# print(lst)
# print(lst[::-1])
# print(lst * 2)
# print(lst + [1,2,3,4,5])
# # lst += [1,2,3,4,5]
# print(lst)
# print('a' in lst)
# print('q' in lst)
# print('q' not in lst)
# list_of_lists = [1,2,[3,4,5],6]
# print (list_of_lists)

# new_lst = ['segun', 'sege', 'oko', 'mama', 'e']

# new_lst.append("kurubente")
# new_lst += ("kurubente") ---- append is just like this
# new_lst.extend("kuruna")
# new_lst.append(["babadudu", "kukute", "ajibogun"])
# new_lst.extend(["babadudu", "kukute", "ajibogun"])
# print(new_lst)
#
# new_lst.insert(1, "Babyface")
# print(new_lst)
# new_lst.insert(-1, "dende")
# print(new_lst)
# new_lst.insert(len(new_lst), "turaya")
# print(new_lst)

# print(new_lst.pop())
# print(new_lst.pop(1))
# print(new_lst.remove("kurubente"))
# print(new_lst)
# print(new_lst.clear())
# print(new_lst.count('oko'))
# print(new_lst.reverse())
# print(new_lst.sort())
# print(new_lst)
# print(new_lst.sort(key=len))
# print(new_lst)

# prof = dict(name='segun', age=12)
# print(prof)
# my_dict = {
#     'name': "Segun",
#     'age': 12,
#     'sex': 'Male',
#     'hobby': ['Python', 'Java'],
#     'Is_wife_beater': False
# }
# print(len(my_dict))
# print('age' in my_dict)
# print(my_dict)
# for key in my_dict:
#     print(key)
# for key in my_dict:
#     print(key, '--->', my_dict[key])
# print(end='\n')
# for key in my_dict.keys():
#     print(key)
# print(end='\n')
# for value in my_dict.values():
#     print(value)
# print(end='\n')
# for key, value in my_dict.items():
#     print(key, '--->',value)
# print(my_dict.items())
