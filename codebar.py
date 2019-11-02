class Student:
    def __init__(self, name, greeting, member='student'):
        self.member = member
        self.name = name
        self.greeting = greeting


class Instructor(Student):
    def __init__(self, name, greeting, member='instructor'):
        super().__init__(name, greeting)
        self.member = member
        self.skill = []

    def add_skill(self, skill):
        self.skill.append(skill)

class Workshop:
    def __init__(self, date, program):
        self.date = date
        self.program = program
        self.participant = []

    def add_participant(self, participant):
        return self.participant.append(participant)

    def print_details(self):
        print(f'=> \nWorkshop - {self.date} - {self.program}\n\nStudents')
        number = 1
        for participants in self.participant:
            if participants.member == 'student':
                print(f'{number}. {participants.name} - {participants.greeting}')
                number += 1

        number = 1
        print('\nInstructors')
        for participants in self.participant:
            if participants.member == 'instructor':
                skill = ', '.join(participants.skill)
                print(f'{number}. {participants.name} - {skill}\n   {participants.greeting}')
                number+=1


workshop = Workshop("12/03/2014", "Shutl")
jane = Student("Jane Doe", "I am trying to learn programming and need some help")
lena = Student("Lena Smith", "I am really excited about learning to program!")
vicky = Instructor("Vicky Python", "I want to help people learn coding.")
vicky.add_skill("HTML")
vicky.add_skill("JavaScript")
nicole = Instructor("Nicole McMillan", "I have been programming for 5 years in Ruby and want to spread the love")
nicole.add_skill("Ruby")
workshop.add_participant(jane)
workshop.add_participant(lena)
workshop.add_participant(vicky)
workshop.add_participant(nicole)

workshop.print_details()


# =>
# Workshop - 12/03/2014 - Shutl
#
# Students
# 1. Jane Doe - I am trying to learn programming and need some help
# 2. Lena Smith - I am really excited about learning to program!
#
# Instructors
# 1. Vicky Ruby - HTML, JavaScript
#    I want to help people learn coding.
# 2. Nicole McMillan - Ruby
#    I have been programming for 5 years in Ruby and want to spread the love
#