

# names = {
#     'Руслан' : 26,
#     'Кадыр' : 23,
#     'Ерлан' : 22
# }
# try:
#     name_file = open('vw.txt', 'w')
#     for key, value in names.items():
#         name_file.writelines(key + ',' +str(value) + '\n')


# except FileNotFoundError:
#     print('u dont have such a module or file!')



# a = input('Input full name: ')
# if "уулу" in a or "кызы" in a:
#     s = a.split()
#     print(f"last name: {s[0]} {s[1]},  first name: {s[2]}")

# else:
#     s = a.split()
#     print(f"first name: {s[-1]}  last name: {s[0]}")

#---------------------------------------------------------------------------------
# s = a.split()
# print(s)


# j = ",".join(a) 
# print(j)

# print('name: '+ repr(s[-1] +'  '+' last name: '+ repr(s[0:2])))




task_file = open('vw.txt', 'r')
task_lists = task_file.readlines()


try:
    for task in task_lists:
        t = task.strip()
        print(t, '=' , eval(t))
except ZeroDivisionError:
    print('if i didnt show smth ... U might input zero smwhere!')
except:
    print('smth was input incorrectly')