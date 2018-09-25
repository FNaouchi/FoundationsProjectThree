# CLASSES AND METHODS
class Person():
    def __init__(self, name, bio, age):
        self.name = name
        self.bio = bio
        self.age = age


class Club():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.president = None
        self.members = []

    def assign_president(self, person):
        self.president = person


    def recruit_member(self, person):
        self.members.append(person)


    def print_member_list(self):
        for member in self.members:
            if member == self.president:
                print("- %s (%d years old, President) - %s\n" %(member.name, member.age, member.bio))
            else:
                print("- %s (%d years old) - %s\n" %(member.name, member.age, member.bio))

