class Member:
    def __init__(self, name, job):
        self.name = name
        self.job = job
    def greet(self):
        print(f"Hi! I am {self.name} and I am a {self.job} at Codebar!")



class Student(Member):
    def __init__(self, name, reason, job = 'Student'):
        super().__init__(name, job)
        self.reason = reason



class Teacher(Member):
    def __init__(self, name, bio, skills = [], job = 'Teacher'):
        super().__init__(name, job)
        self.skills = skills
        self.bio = bio
    
    def add_skill(self, skill):
        self.skills.append(skill)



class Workshop:
    def __init__(self, date, subject):
        self.date = date
        self.subject = subject
        self.teachers = []
        self.students = []

    def add_participant(self, member):
        self.member = member
        if (type(member).__name__) == 'Student':
            self.students.append(member)
        elif (type(member).__name__) == 'Teacher':
            self.teachers.append(member)
        else:
            print("Not Valid Member")

    def print_details(self):
        print(f'Workshop: {self.subject}  Startdate: {self.date}')
        print("Students")
        for index, Student in enumerate(self.students):
            print(f"{index + 1}: {Student.name} \n {Student.reason}")
        print("Teachers")
        for index, Teacher in enumerate(self.teachers):
            print(f"{index + 1}: {Teacher.name} \n {Teacher.skills} \n {Teacher.bio}")



        


sam = Student('Sam', 'For Fun and to be smart')
eric = Teacher('Eric', 'I Like to code a lot, and want to shape the minds of students')

workshop = Workshop('12/03/2014', 'Shutl')
jane = Student('Jane Doe', 'I am trying to learn programming and need some help')
lena = Student('Lena Smith', 'I am really excited about learning to program!')
vicky = Teacher('Vicky Python', 'I want to help people learn coding.')
vicky.add_skill('HTML')
vicky.add_skill('JavaScript')
nicole = Teacher('Nicole McMillan', 'I have been programming for 5 years in Python and want to spread the love')
nicole.add_skill('Python')

workshop.add_participant(jane)
workshop.add_participant(lena)
workshop.add_participant(vicky)
workshop.add_participant(nicole)
workshop.print_details()
