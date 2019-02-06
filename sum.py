
mylist = [1, 2, [3, 4]]


def find_total_sum(numbers):
    total = 0

    for index in len(numbers):
        if isinstance (numbers[index], list):
            total += find_total_sum(numbers[index])
        total += numbers[index]
    return total

print(find_total_sum)