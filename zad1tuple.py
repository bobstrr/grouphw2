def count_equal_numbers(sequence):
    numbers = sequence.split()

    counter = {}

    for number in numbers:
        number = round(float(number), 1)
        counter[number] = counter.get(number, 0) + 1

    for number, count in counter.items():
        print(f"{number} - {count} times")

sequence = input("Enter a sequence of numbers separated by spaces: ")
count_equal_numbers(sequence)