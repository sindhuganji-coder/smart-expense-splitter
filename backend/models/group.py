class Group:
    def __init__(self, group_name, members=None):
        self.group_name = group_name
        self.members = members if members is not None else []

    def add_member(self, member):
        self.members.append(member)

    def remove_member(self, member):
        self.members.remove(member)

    def get_members(self):
        return self.members

    def __str__(self):
        return f'Group: {self.group_name}, Members: {self.members}'