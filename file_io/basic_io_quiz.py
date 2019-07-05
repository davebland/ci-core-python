def game_menu():
    print("1. Play")
    print("2. Add Qs")
    print("3. Quit")
    option_selected = int(input("Select an option: "))
    if option_selected == 1:
        play_quiz()
    elif option_selected == 2:
        add_qs()
    elif option_selected == 3:
        print("Bye...")
    else:
        print("Not a valid option, please try again")
        game_menu()

def add_qs():
    print('')
    question = input("Enter a qs: ")
    answer = input("And the answer: ")
    
    f = open('quiz_questions.txt', 'a')
    f.write(question + '\n')
    f.write(answer + '\n')
    f.close()
    
    print("Thanks, that's been stored")
    game_menu()
    
def play_quiz():
    print('')
    questions = []
    answers = []
    
    with open('quiz_questions.txt', 'r') as file:
        lines = file.read().splitlines()
    
    for i, text in enumerate(lines):
        if i%2 == 0:
            questions.append(text)
        else:
            answers.append(text)
            
    num_of_qs = len(questions)
    score = 0
    
    for question, answer in zip(questions, answers):
        guess = input(question + ': ')
        if guess == answer:
            score += 1
            print("CORRECT\n")
        else:
            print("INCORRECT\n")
    
    print('Score is {0} out of {1}\n'.format(score, num_of_qs))
        
    game_menu()

# Start game
game_menu()