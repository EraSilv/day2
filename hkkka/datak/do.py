# Задание 5:
    # Вам дан LIST и пустая Dictionary:
    # pairs = {}
    # В LIST перечислены элементы, где идёт строгая очерёдность STRING и INTEGER.
    # То есть если перед вами элемент типа данных STRING то следующий точно INTEGER и наоборот.
    # keys_values = ['one', 1, 2, 'two', 3, 'three', 'four', 4, 'five', 5, 6 'six', 7, 'seven', 'eight', 8, 'nine',9, 10, 'ten', 11, '11', 12 ,'13']
    # Проходя по LIST необходимо брать элементы по парно, один элемент может относиться только и только к одной паре.
    # Ваша задача выявить если элемент является типом данных string() то записывать его как ключ в Dictionary -> pairs.

    # Пример:
    # pairs ={'one': 1, 'two': 2, 'three': 3, ...}
################################################################################


# pairs = {}

# a = "ghg"


# keys_values = ['one', 1, 2, 'two', 3, 'three', 'four', 4, 'five', 5, 6 ,'six', 7, 'seven', 'eight', 8, 'nine',9, 10, 'ten', 11, 'eleven', 12 ,'twelve']
# digits = []
# strings = []

# for i in keys_values:
#     if isinstance(i, int):
#         digits.append(i)
# # print(digits)


# for stri in keys_values:
#     if isinstance(stri, str):
#         strings.append(stri)
# # print(strings)


# for key in range(len(digits)):
#     pairs[strings[key]] = digits[key]

# print(pairs)






# Задание 3:
#     Вам дан SET значений:
#     uniques = {3,13,15,27,1,4,8,23,19,12,9,2,17}
#     Создайте функцию которая:
#         Удалит все чётные значения внутри SET, а оставшиеся отсортирует по убыванию.
#     В результате, ваша функция должна вернуть отсортированный SET и неважно, каким будет SET растопленным или замороженным.




lst = {3,13,15,27,1,4,8,23,19,12,9,2,17}
lst = list(lst)
def p_even(input_lst):
    output = [x for x in input_lst if x % 2 == 0]
    return output

even = p_even(lst)
# print(even)
for i in lst:
    if i in even:
        lst.remove(i)
a = sorted(lst,  reverse=True)
# print(set(a))
print(a)


