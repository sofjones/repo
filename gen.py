import random

list1 = [0,1,2,3]
number_of_errors = random.choice(list1)

if number_of_errors == 0:
    print('no errors present')
    exit
    
errors = []
for i in range(number_of_errors):
    list2 = ['Spelling', 'Subject-verb', 'Punctuation', 'Capitalization', 'Formation of Plurals', 'Word Usage']
    rand_error = random.choice(list2)
    errors.append(rand_error)

print(errors)