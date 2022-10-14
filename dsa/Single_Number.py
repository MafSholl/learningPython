def sorted_rearrange(lst):
    output = [0] * len(lst)
    print(lst)
    print()
    j = 2
    for i in range(0, int(len(lst) / 2)):
        if i == 0:
            output[i], output[i + 1] = lst[len(lst) - (i + 1)], lst[i]
        else:
            output[j], output[j + 1] = lst[len(lst) - (i + 1)], lst[i]
            j += j
    if len(lst) % 2 == 1:
        output[len(lst) - 1] = lst[i + 1]
    return output


# print(solution([1, 2, 3, 4, 5, 6, 7]))
# print(solution([1, 2, 3, 4]))
print(sorted_rearrange([1, 2, 3, 4, 5, 6]))
