
def digital_root(n):
    input_sum = 0
    if n > 9:
        for i in str(n):
            input_sum += int(i)
        return digital_root(input_sum)
    return n
    #     return sum(int(i) for i in str(n))

# print([user_info['username'] for user_info in user_infos if user_info["tweets"] != []])

print(digital_root(9))
print(digital_root(16))
print(digital_root(942))
print(digital_root(132189))
print(digital_root(493193))
