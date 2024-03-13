import random

def guess():
    words = ['apple', 'blueberry', 'cherry', 'moksh', 'viya']

    chosen_word = random.choice(words)
    # print('Chosen word '+ chosen_word)

    count = 0

    curr_word = []
    for _ in range(len(chosen_word)):
        curr_word += '_'

    while count < 7 and '_' in curr_word:
        guess = input('Guess a letter: ').lower()
        
        if(chosen_word.find(guess) == -1):
            count += 1
            print(str(7-count) + ' attempts remaining')
            print(curr_word)
            continue
        for pos in range(len(chosen_word)):
            if(chosen_word[pos] == guess):
                curr_word[pos] = chosen_word[pos]
        print(curr_word)
    
    if '_' not in curr_word:
        print('Congrats!!! You have won.')
    else:
        print('Better luck next time :()')
        
            
    
    

if __name__ == '__main__':
    guess()