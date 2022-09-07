paragraph = "This planet has - or rather had - a problem, which was \
this: most of the people living on it were unhappy for pretty much \
of the time. Many solutions were suggested for this problem, but \
most of these were largely concerned with the movements of small \
green pieces of paper, which is odd because on the whole it wasn't \
the small green pieces of paper that were unhappy."

# print(paragraph)

paragraph1 = """This planet has - or rather had - a problem, which was
                this: most of the people living on it were unhappy for pretty much
                of the time. Many solutions were suggested for this problem, but
                most of these were largely concerned with the movements of small
                green pieces of paper, which is odd because on the whole it wasn't
                the small green pieces of paper that were unhappy."""

# print(paragraph1)

string1 = "abra"
string2 = "cadabra"
concat_string = string1 + string2

print(concat_string)

flavour = "apple pie"
print(flavour[0])
print(flavour[-1])
print(flavour[-2])
print(flavour[-3])

#Slicing

number = 16
sum = 0
num_str = str(number)
print(type(num_str))
print(len(num_str))
for i in num_str:
    sum += int(i)
print(sum)


print(2**(3**2), (2**3)**2, (2**3)**3)
