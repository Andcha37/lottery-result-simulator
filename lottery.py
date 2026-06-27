from random import randint


def generate_numbers(n):
    numbers = []
    while len(numbers) < n:
        number = randint(1, 45)
        if number not in numbers:
            numbers.append(number)
    return numbers


def draw_winning_numbers():
    main_numbers = sorted(generate_numbers(6))

    while True:
        bonus_number = randint(1, 45)
        if bonus_number not in main_numbers:
            break

    return main_numbers + [bonus_number]


def count_matching_numbers(numbers, winning_numbers):
    count = 0
    for number in numbers:
        if number in winning_numbers:
            count += 1
    return count


def check(numbers, winning_numbers):
    main_count = count_matching_numbers(numbers, winning_numbers[:6])
    bonus_count = count_matching_numbers(numbers, winning_numbers[6:])

    if main_count == 6:
        return "1000000000"
    elif main_count == 5 and bonus_count == 1:
        return "50000000"
    elif main_count == 5 and bonus_count == 0:
        return "1000000"
    elif main_count == 4:
        return "50000"
    elif main_count == 3:
        return "5000"
    else:
        return "0"


if __name__ == "__main__":
    winning_numbers = draw_winning_numbers()
    my_numbers = sorted(generate_numbers(6))
    print("내 번호:", my_numbers)
    print("당첨 번호:", winning_numbers)
    print("당첨금:", check(my_numbers, winning_numbers))
