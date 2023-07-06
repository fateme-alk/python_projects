import random
animals = {
    0:'chicken',
    1:'dog',
    2:'cat',
    3:'mouse',
    4:'frog',
}

def choose_rand_word(category):
    rand_word = random.choice(category).lower()
    return rand_word, set(rand_word)

rand_word, rand_word_set = choose_rand_word(animals)

lives = 6
correct_char_guesses = set()
while lives > 0:
    guessed_char = str(input())
    if rand_word_set:
        if guessed_char in rand_word_set:
            correct_char_guesses.add(guessed_char)
            rand_word_set.remove(guessed_char)
        else: 
            lives = lives - 1
    else:
        print('you win')
        break
    
    for char in rand_word:
        if char in correct_char_guesses:
            print(char, end='')
        else:
            print('_', end='')
    print('\n' * 2, '*' * 20)
else:
    print('you failed')