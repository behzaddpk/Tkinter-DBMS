import random

class Dice:
    def roll(self):
       frist_number= random.randint(1, 6)
       second_number = random.randint(1, 6)

       return frist_number, second_number


dice = Dice()
print(dice.roll())