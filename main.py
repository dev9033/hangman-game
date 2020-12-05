from random import randint
from linecache import getline


def linecount(file):
    with open(file) as f:
        for total, j in enumerate(f):
            pass
        total += 1
    return total


def random_word():
    total_words = linecount("list.txt")
    i = randint(1, total_words)
    return getline('list.txt', i)


def hint():
    print('hint yes')


def show_letters(word, letters):
    txt = ''
    for i in word:
        if i not in letters:
            txt += '-'
        else:
            txt += i
    print(txt)


def score(word_len, rem_chances):
    main_chances = word_len*2+3
    return round((rem_chances/main_chances)*100, 2)


def hangman(word):
    print("%s letters word: " % len(word)+"_ "*len(word))
    print(word)
    word_set = set(word)
    usr_set = set()
    chances = len(word)*2 + 3
    while True:
        if word_set == usr_set:
            print('you got it, the word was: %s' % word)
            print('score {}%\n\n'.format(score(len(word), chances)))
            break
        else:
            if chances <= 0:
                print('game over\n\n')
                break
            else:
                usr_inp = input('enter a letter: ')
                if usr_inp in word_set:
                    usr_set.add(usr_inp)
                else:
                    chances -= 1
            show_letters(word, usr_set)
            print('%s chances are left\n' % chances)


while True:
    usr_inp = input('play the game? (y/n): ')
    if usr_inp == 'n':
        break
    elif usr_inp == 'y':
        word = random_word()
        hangman(word.strip())
    else:
        print('invalid choice, try again\n')
