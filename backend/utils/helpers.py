def calculate_percentage(total, part):
    if total == 0:
        return 0
    return (part / total) * 100

def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

def split_expense(amount, number_of_people):
    if number_of_people <= 0:
        raise ValueError('Number of people must be greater than zero')
    return amount / number_of_people
