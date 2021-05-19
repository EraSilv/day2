

# operators = {
#     'megacom': [
#         '0558',
#         '0551',
#         '0555',
#         '0557',
#         '0996',
#         '0550',
#         '0553'
#     ],
#     'beeline': [
#         '0770',
#         '0777'
#     ],
#     'o!': [
#         '0700',
#         '0999'
#     ],
#     'gorod': [
#         '03222',
#         '03231',
#         '03200',
#         '03230',
#         '03211'
#     ],
# }



# def check_no_phone(num):

#     if len(num) >= 9 and len(num) <=10:
#         print('Correct no.!')
#         code = num[0:4]
#         if code in operators['o!']:
#             print('operator O!')
#         elif code in operators['megacom']:
#             print('Operator megacom')
#         elif code in operators['beeline']:
#             print('Operator beeline')
#         code = num[0:5]
#         if code in operators['gorod']:
#             print('UR operator gorod: ')


#     else:
#         print('ERROr no. ')

# phone = input('Enter ph no:')
# phone2 = input('Enter ed ph no:')
# check_no_phone(phone)
# check_no_phone(phone2)

def translate():
    print('say hello!')

def getfullname(fname,lname):
    return fname + ' '+ lname