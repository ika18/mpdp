# -*- coding:utf-8 -*-

class Frog:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstracle):
        print('{} the Frog encounters {} and {}!'.format(self, obstracle, obstracle.action()))


class Bug:
    def __str__(self):
        return 'a bug'

    def action(self):
        return 'eats it'


class FrogWorld:
    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return '\n\n\t----- Frog World ------'

    def make_character(self):
        return Frog(self.player_name)

    def make_obstracle(self):
        return Bug()


class Wizard:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstracle):
        print('{} the Wizard battles against {} and {}!'.format(self, obstracle, obstracle.action()))


class Ork:
    def __str__(self):
        return 'an evil ork'

    def action():
        return 'kills it'


class WizardWorld:
    def __init__(self, name):
        print(self)
        self.name = name


    def __str__(self):
        return '\n\n\t-------- Wizard World --------'

    def make_character(self):
        return Wizard(self.player_name)


class GameEnv:
    def __init__(self, factory):
        self.hero = factory.make_character()
        self.obstracle = factory.make_obstracle()

    def play(self):
        self.hero.interact_with(self.obstracle)

def validate_age(name):
    try:
        age = input('Welcome {}. How old are you? '.format(name))
        age = int(age)
    except ValueError as err:
        print('Age {} is invalid, please try again...'.format(age))
        return (False, age)
    return (True, age)

def main():
    name = input("Hello. What's your name? ")
    valid_input = False
    while not valid_input:
        valid_input, age = validate_age(name)
    game = FrogWorld if age < 18 else WizardWorld
    env = GameEnv(game(name))
    env.play()

if __name__ == '__main__':
    main()