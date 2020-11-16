from random import randint, choice, randrange
import random

no_takers = 10

marks = []
for i in range(no_takers):
    x = randrange(60, 90)
    marks.append(x)


first_names = ['John', 'Jane', 'Corey', 'Travis', 'Dave', 'Kurt', 'Neil', 'Sam', 'Steve', 'Tom', 'James', 'Robert',
               'Michael', 'Charles', 'Joe', 'Mary', 'Maggie', 'Nicole', 'Patricia', 'Linda', 'Barbara', 'Elizabeth',
               'Laura', 'Jennifer', 'Maria',"sami","abhinav","Naren","Sam","Sinaan" ]

last_names = ['Smith', 'Doe', 'Jenkins', 'Robinson', 'Davis', 'Stuart', 'Jefferson', 'Jacobs', 'Wright',
              'Patterson', 'Wilks', 'Arnold', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson',
              'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin']


def random_score(marks):
    score = choice(marks)
    return score


def luck():
    return randint(0, 100) / 10


above_85 = []
number = 1
for num in range(no_takers):
    first = random.choice(first_names)
    last = random.choice(last_names)
    mark = random_score(marks)
    total = mark + luck()
    ratio = (luck() / 10) * 100
    string = f'{first} {last} ~~ {total} ~~ {str(ratio)[0:5]}\n'

    if total > 85:
        print(*f"[", number, "] ", string, sep="")
        number += 1
        above_85.append(string)
    else:
        print(string)

print(">************************<")
print(*above_85)
