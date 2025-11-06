import random

word=['python', 'java', 'kotlin', 'javascript','ruby']

#randomly choose a word from the list
chose_word=random.choice(word)
word_disply=['-' for _ in chose_word]
attempts=8 #number of allowed attempts

print("Welcome to Hangman")


while attempts > 0 and '-' in word_disply:
    print("\n" + ''.join(word_disply))
    guess=input("guess a letter:\n").lower()
    if guess in chose_word:
        for index, letter in enumerate(chose_word):
            if letter==guess:
                word_disply[index]=guess #reveal letter
    else:
        print("that letter doesn't appear in the word, idiot!!!!.")
        attempts-=1

#gess conclusion
if '-' not in word_disply:
    print('you guess the word!')
    print('-'.join(word_disply))
    print("you survived!")
else:
    print("you run out of attempts. the word was:" + chose_word)
    print("you lost")
    
