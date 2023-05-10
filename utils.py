def find_max(numbers):
    max = numbers[0]
    for next in numbers:
        if next > max:
            max = next
    return max