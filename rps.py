#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

import random

moves = ['rock', 'paper', 'scissors']
player_Types = ['rocker', 'random', 'reflect', 'cycle', 'rvsr']
n = random.randint(0, 2)
"""The Player class is the parent class for all of the Players
in this game"""


class Player:

    def __init__(self):
        self.score = 0
        self.move_list = []
        self.cycle_list = self.moves()
        self.Contender_Move = ""

    def move(self):
        return 'rock'

    def moves(self):
        return moves

    def get_move(self):
        return self.move()

    def learn(self, my_move, their_move):
        self.My_last_Move = my_last_move
        self.Contender_Move = their_move

    def remember_last_move(self, Contender_Move):
        self.Contender_Move = Contender_Move
        self.move_list.append(Contender_Move)

    def cycler_list(self):

        # To make cycler list remove the first item
        # and append it to the end of the list

        cycle_move = self.cycle_list.pop(0)
        self.cycle_list.append(cycle_move)

    def get_score(self):
        return self.score

    def set_score(self, score):
        self.score = score


class Human_Player(Player):
    def move(self):
        Human_Player_Move = ""
        while Human_Player_Move not in moves:
            Human_Player_Move = input(
                "Enter your move:\n [Rock, Paper or Scissors]:").lower()
            if Human_Player_Move == "exit":
                print("Game Over")
                exit()
        return Human_Player_Move


class Random_player(Player):
    def move(self):
        Random_player_move = random.choice(self.moves())
        self.move_list.append(Random_player_move)
        return Random_player_move


class Reflect_Player(Player):
    def move(self):
        move_list_length = len(self.move_list)
        if move_list_length < 1:
            return random.choice(self.moves())
        else:
            return self.Contender_Move


class Cycle_Player(Player):
    def move(self):
        current_move = self.cycle_list[n]
        self.cycler_list()
        return current_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.rounds = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()

        print(f"Player 1: {move1}  Player 2: {move2}")

        winner = self.determine_winner(move1, move2)
        self.assign_score(winner)

        self.p1.remember_last_move(move2)
        self.p2.remember_last_move(move1)
        self.print_results(winner)

    def print_final_results(self):
        p1_score = self.p1.get_score()
        p2_score = self.p2.get_score()
        print(f"""
        Final results are:
        You => {p1_score}
        The Contender => {p2_score}
        """)

        if p1_score > p2_score:
            print("You win!\n Congratulations :)")
        elif p2_score > p1_score:
            print("The Contender wins...\n Game Over")
        else:
            print("It is a tie")

    def play_game(self):
        print(" \n Game start! \n")
        for round in range(1, 4):
            print(f"Round {round}:")
            self.play_round()
        self.print_final_results()

    def print_results(self, winner):
        p1_score = self.p1.get_score()
        p2_score = self.p2.get_score()
        if winner == 1:
            print("You win!")
        elif winner == 0:
            print("It is a tie")
        else:
            print("The Contender wins!")
        print(f"The score is: You  {p1_score}, The Contender {p2_score} \n ")

    def determine_winner(self, human_move, computer_move):
        if human_move == computer_move:
            return 0
        elif beats(human_move, computer_move):
            return 1
        return 2

    def assign_score(self, winner):
        if winner == 1:
            p1_score = self.p1.get_score()
            p1_score += 1
            self.p1.set_score(p1_score)
        elif winner == 2:
            p2_score = self.p2.get_score()
            p2_score += 1
            self.p2.set_score(p2_score)


if __name__ == '__main__':

    player_Type = ""
    while player_Type not in player_Types:
        player_Type = input(
            "Which player do you want to play aganist (Rocker, Random, Reflect, Cycle, RVSR)\n *Type 'exit' to end the game anytime: => ").lower()
        if player_Type == "exit":
            print("Game Over")
            exit()

    if player_Type == "rocker":
        print(" \n Your Contender is the Rocker")
        game = Game(Human_Player(), Player())
    elif player_Type == "random":
        print(" \n Your Contender is the Random Player")
        game = Game(Human_Player(), Random_player())
    elif player_Type == "reflect":
        print(" \n Your Contender is the Reflect Player")
        print("  Be careful, it copies your moves !!!")
        game = Game(Human_Player(), Reflect_Player())
    elif player_Type == "cycle":
        print(" \n Your Contender is the Random Player")
        game = Game(Human_Player(), Cycle_Player())
    elif player_Type == "rvsr":
        print(" \n Random Player VS Random Player Game")
        game = Game(Random_player(), Random_player())

    game.play_game()
