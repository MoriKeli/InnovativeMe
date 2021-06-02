from random import randint
score = 0
for i in range(5):
    num = randint(1, 10)
    guess = int(input('Enter a number: '))
    if guess == num:
        score += 10
    else:
        score -= 1
print('Total score: ', score)