# class Teacher:
#     name = ' '
#     age = ' '
#     lesson = ' '
#     def to_teach(self, word):
#         print(self.lesson, word)


# name = input('input name of the teacher: ').title()
# teacher = Teacher()
# teacher.name = name
# if teacher.name == 'Aziza':
#     teacher.age = 31
#     teacher.lesson = 'english'
#     teacher.to_teach('lesson!')
# elif teacher.name == 'Anvar':
#     teacher.age = 34
#     teacher.lesson = 'math'
#     teacher.to_teach('lesson!')
# elif teacher.name == 'Damira':
#     teacher.age = 40
#     teacher.lesson = 'biology'
#     teacher.to_teach('lesson!')
# elif teacher.name == 'Busanam':
#     teacher.age = 31
#     teacher.lesson = 'physicks'
#     teacher.to_teach('lesson!')

# else:
#     print('U have only 4 teachers: \n 1.Aziza \n 2. Anvar \n 3. Damira \n 4. Busanam')







# class Plane:

#     def __init__(self, name , year,sy):
#         self.name = name
#         self.year = year
#         self.sy = sy 
#     def get_name(self):
#         print('name:', self.name)
#     def get_year(self):
#         print('year:', self.year)
#     def get_sy(self):
#         print('sy:', self.sy)
    
    
#     def to_fly(self):
#         self.can_fly = True
#         print('I believe i  can fly...')
 
#     def cant_fly(self):
#         self.can_fly = False
#         print('i believe i cant fly.....')



# myplane = Plane(
#     name = 'Boeing 747',
#     year = 1997,
#     sy = 'USA',
    
    
#     )

# myplane.get_name()
# myplane.get_year()
# myplane.get_sy()


# work = input('to know if its working: ')

# if work == 'yes':
#     myplane.to_fly()

    
# elif work == 'no':
#     myplane.cant_fly()










# whatelse = ''

# class Hacker:
#     def __init__(self, name , level , skills, age, gender):
#         self.name = name
#         self.age = age
#         self.level = level
#         self.skills = skills
#         self.gender = gender

#     def get_name(self):
#         print('name:', self.name)
#     def get_age(self):
#         print('age:', self.age)
#     def get_level(self):
#         print('level:', self.level)
#     def get_skills(self):
#         print('skills:', self.skills)
#     def get_gender(self):
#         print('gender:', self.gender)

    
#     def to_work(self):
#         # self.to_work = True
#         print('Can hack bank accounts!')
#         if whatelse == 'else':
#             print('ERROR! HACK attacking!!!')


# erlan = Hacker(
#     name = 'Erlan',
#     age = 2003,
#     level = 'Unknown',
#     skills = 'Unknown',
#     gender = 'male'
    
# )

# erlan.get_name()
# erlan.get_age()
# erlan.get_level()
# erlan.get_skills()
# erlan.get_gender()







# work = input('Show abilities ? : ')
# if work == 'yes':
#     erlan.to_work()

# whatelse = input('Continue? : ')
# if whatelse == 'else':
#     erlan.to_work()

    



