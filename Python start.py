Rock, Paper, Scissors game on Python


from random import choice

rps = ('rock', 'paper', 'scissors')
rps_dictionary = {
    'rock': {'strong': 'scissors', 'weak': 'paper'},
    'paper': {'strong': 'rock', 'weak': 'scissors'},
    'scissors': {'strong': 'paper', 'weak': 'rock'}
}

def print_result(user_score, com_score, win, lose, tie):
    print('Result: ', end = '')
    if user_score > com_score:
        print('You win!')
    elif user_score < com_score:
        print('You lose!')
    else:
        print('That is a tie!')
    print('---------------------')

    print(f'Your score: {user_score}')
    print(f'Computer score: {com_score}')
    print('---------------------')

    print(f'Win: {win}')
    print(f'Lose: {lose}')
    print(f'Tie: {tie}')

def play(rounds):
    game_result = {
        'user_score': 0,
        'com_score': 0,
        'win': 0,
        'lose': 0,
        'tie': 0
    }

    while rounds > 0:
        user_input = input ('Enter your choice: (1: Rock, 2: Paper, 3: Scissors): ')
        if user_input in ('1', '2', '3'):
            rounds -= 1
            user_hand = rps [int(user_input) - 1]
            com_hand = choice(rps)

            if rps_dictionary [user_hand]['strong'] == com_hand:
                game_result['user_score'] += 1
                game_result['win'] += 1
                result = 'You win!'

            elif rps_dictionary [user_hand]['weak'] == com_hand:
                game_result['com_score'] += 1
                game_result['win'] += 1
                result = 'You lose!'
            else:
                print('That is a tie!')
            print(f'You -> {user_hand}. Computer -> {com_hand}. {result}')
        elif user_input == '0':
            break
        else:
            print('Invalid input!')
        print()
    print_result(**game_result)


if __name__=="__main__":
    print('Welcome!')
    try:
        rounds = int(input('How many rounds would you like to play?'))
        play(rounds)
    except ValueError:
        print('That number is not valid!')
