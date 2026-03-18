class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __str__(self):
        return f'User({self.username}, {self.email})'

# Example usage:
# user = User('johndoe', 'johndoe@example.com')
# print(user)