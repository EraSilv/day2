calculation_to_seconds = 24 * 60 * 60
calculation_to_hours = 24 

# print(calculation_to_seconds)
name_of_unit = "hours"

 #VERSION 1:
# print(f"20 days are {20 * 24 * 60 * 60} seconds")
# print(f"35 days are {35 * 24 * 60 * 60} seconds")
# print(f"50 days are {50 * 24 * 60 * 60} seconds")
# print(f"110 days are {110 * 24 * 60 * 60} seconds") 
 #VERSION2:
# print(f"20 days are {20 * calculation_to_seconds} {name_of_unit}")
# print(f"35 days are {35 * calculation_to_seconds} {name_of_unit}")
# print(f"50 days are {50 * calculation_to_seconds} {name_of_unit}")
# print(f"110 days are {110 * calculation_to_seconds} {name_of_unit}") 
 #VERSION3:
# print(f"30 days are {30 * calculation_to_seconds} {name_of_unit}")
# print(f"90 days are {90 * calculation_to_seconds} {name_of_unit}")
# print(f"180 days are {180 * calculation_to_seconds} {name_of_unit}")
# print(f"365 days are {365 * calculation_to_seconds} {name_of_unit}") 

######-------------------------------------------------------------------------------------------------------------------------
 
# def days_to_units(num_of_days):    #----------- line 52------ exchanged--------
#     print(num_of_days > 0) #for true false
#     if num_of_days > 0:
#     print(f"{num_of_days} days are {num_of_days * calculation_to_hours} {name_of_unit}")
#         return(f"{num_of_days} days are {num_of_days * calculation_to_hours} {name_of_unit}")
#     elif num_of_days == 0:
#         return('u entered a 0, please  enter a valid positive number!')
   

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# days_to_units(31 , 'Awesome!')
# days_to_units(35 , 'Looks Good!')
# days_to_units(13)
# days_to_units(90)
# days_to_units(365)

# user_input = input('Hey user, enter a number of days and i will convert it to hours!:\n')
# if user_input.isdigit():
#     user_input_number = int(user_input)
#     calculated_value = days_to_units(user_input_number)
#     print(calculated_value)
# else:
#     print('Ur input is not a  valid number. Dont ruin my programm!')

# ---------------------------------------------------------------------------------

def validate_and_execute():
    try:
        
        user_input_number = int(num_of_days_element )  
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print('u entered a 0, please  enter a valid positive number!')
        else:
            print('u entered a negative, no concersion for u!')

    except ValueError:
        print('Ur input is not a  valid number. Dont ruin my programm!')


while True:
    user_input = input('Hey user, enter a number of days and i will convert it to hours!:\n')
    for num_of_days_element in user_input.split(","):
        validate_and_execute() 
    if user_input == 'exit': break

    
        







