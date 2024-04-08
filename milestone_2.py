import random



word_list =  ['watermelon', 'lychee', 'dates', 'banana', 'blueberries']
word = random.choice(word_list)
guess = str(input('Please guess a letter '))


if len(guess) == 1 and guess.isalpha():
    print ('good guess')
else:
    print ('Oops! that is not a valid input')


