import random
from time import sleep
from art import text2art

account = 20
opponent = random.choice(['Surfer Guy', 'Guy walking dog', 'Your cousin', 'Pawn Shop Owner', 'Local Dice Shooter'])


# HELPER FUNCTIONS #
def roll_die():
    """Simple function to roll the die"""
    return random.randint(1, 6)


def roll_dice():
    """Simple function to roll 2 dice"""
    return random.randint(1, 6) + random.randint(1, 6)


def play_again():
    """Prompts you to play again or go main menu"""
    choice = input('Another round?\n')
    if choice.lower() in ['y', 'yes', 'ye']:
        bet = input('How much you bettin?\n')
        game(bet)
    elif choice.lower() in ['menu', 'main menu', 'title', 'options', 'help']:
        main_menu()


def main_rolling(player, point, bet):
    """This function is called after the initial roll for turn to handle rolling logic"""
    global account
    bad_roll = point
    good_roll = 7
    # PLAYER ROLLING#
    if player == player_name:
        choice = input()
        if choice == 'roll':
            player_roll = roll_dice()
            print(f'You rolled a {player_roll}\n')
            sleep(1)
            if player_roll == bad_roll:
                account -= int(bet)
                print('You lose the pot.\n')
                print(f'You have ${account} now.\n')
                play_again()
            elif player_roll == good_roll:
                account += int(bet)
                print('You won the pot!\n')
                print(f'Your balance is now {account}\n')
                play_again()
            else:
                print('Didn\'t hit point or 7, roll again')
                main_rolling(player, point, bet)
    # CPU ROLLING#
    else:
        cpu_roll = roll_dice()
        print(f'{opponent} rolled a {cpu_roll}\n')
        sleep(1)
        if cpu_roll == bad_roll:
            account += int(bet)
            print(f'{opponent} lost. You won the pot.\n')
            print(f'You have ${account} now.\n')
            play_again()
        elif cpu_roll == good_roll:
            account -= int(bet)
            print(f'{opponent} won the pot!\n')
            print(f'You have ${account} now\n')
            play_again()
        else:
            main_rolling(player, point, bet)


def game(bet):
    """Called to start the game with the bet value"""
    player_roll = roll_die()
    cpu_roll = roll_die()
    run = True

    print(f'You put ${bet} on the table.')
    sleep(1.5)
    choice = input('Roll to see who goes first\n')
    if choice.lower() == 'roll':
        while run:
            print('Rolling Dice!\n')
            sleep(1)
            print(f'You rolled a {player_roll}\n')
            sleep(1)
            print(f'{opponent} rolls a {cpu_roll}\n')
            sleep(1)
            # YOU ROLL FIRST #
            if player_roll < cpu_roll:
                print(f'Your roll was lower, You are the shooter. Your spot is {player_roll}\n')
                main_rolling(player_name, player_roll, bet)
                run = False
            elif cpu_roll < player_roll:
                print(f'{opponent} rolled lower, they are the shooter.')
                main_rolling(opponent, cpu_roll, bet)
                run = False
            else:
                player_roll = roll_die()
                cpu_roll = roll_die()
                print('Tied dice\n')
                sleep(1)
                continue

    elif choice.lower() == 'quit':
        print('GAME SHOULD STOP HERE')


def main_menu():
    """Displays the options and accepts input"""
    user_command = input('Main Menu:\n\n'
                         'Commands\n'
                         '---------\n'
                         '"balance" to see your account balance\n'
                         '"start [amount]" to start game with a starting bet\n'
                         '"shop" to view items in the shop\n'
                         '"roll"\n')
    sleep(1.5)
    if user_command.lower() == 'balance':
        print(f'Your balance is ${account}.\n')
        main_menu()
    elif 'start' in user_command.lower():
        bet = user_command.lower().split()[1]
        print(bet)
        game(bet)


# TITLE DISPLAY AND INTRO #
welcome = text2art('-----------------\nWELCOME   TO   STREET   DICE\n -----------------', font="Grafitti")
print(welcome)
sleep(3)
player_name = input('Enter your name to begin\n')
sleep(2)
print(f'\n Hello {player_name}. Glad you\'re awake...\n')
sleep(3)
print('Those guys beat you up pretty badly.. They are NOT who you want to be in debt to.\n')
sleep(3)
print('Theres only one surefire way to pay back a deadly loan shark\n')
sleep(3)
print('...')
sleep(2)
print(text2art('\n\nStreet Dice!', font='varsity'))
sleep(3)

main_menu()
