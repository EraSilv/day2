fruits1 = { 'apple', 'cherry', 'banana', 'lemon', 'watermelon', 'coconut', 'salt' }
fruits2 = { 'melon', 'potato', 'tomato', 'banana', 'carrot', 'lemon' }
print(fruits1.intersection(fruits2))


#---------------------------------------------------------------------------------
fruits1 = { 'apple', 'cherry', 'banana', 'lemon', 'watermelon', 'coconut', 'salt' }
fruits2 = { 'melon', 'potato', 'tomato', 'banana', 'carrot', 'lemon' }
print(fruits1.update(fruits2))

#--------------------------------------------------------------------------------

predmets ={
	'биография',
	'математика',
	'химия',
	'биология',
	'физика',
	'астрономия',
	'123Физ',
	'Гастрономия',
	'Книги',
	'Литература'
}

predmets.remove('Книги')
predmets.remove('123Физ')
predmets.remove('Гастрономия')
predmets.remove('биография')
print(predmets)