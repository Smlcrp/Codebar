class Member:
    def __init__(self, name, job):
        self.name = name
        self.job = job
    def greet(self):
        print(f"Hi! I am {self.name} and I am a {self.job} at Codebar!")


class Student(Member):
    def __init__(self, name, reason, job = 'Student'):
        super().__init__(name, job)
    def stu_records(self):
        print(f"My name is {self.name}, I am a {self.job} at Codebar and I came here because {self.reason}")



class Teacher(Member):
    def __init__(self, name, bio, skills = 'Python, Javascript', job = 'Teacher'):
        super().__init__(name, job)
    
    def add_skill(self, skill):
        self.skills += skill


sam = Student('Sam', 'For Fun')
eric = Teacher('Eric', 'I Like to code a lot')
sam.greet()
eric.greet()