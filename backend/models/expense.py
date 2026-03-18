class Expense:
    def __init__(self, amount, category, description):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = '2026-03-18 13:36:28'  # Current Date and Time

    def __str__(self):
        return f'Expense({self.amount}, {self.category}, {self.description})'