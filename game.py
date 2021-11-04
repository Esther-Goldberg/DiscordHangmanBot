import discord
import random


class Game():

    words_list = [
        "yesterday",
        "minecraft",
        "discord",
        "computer",
        "telephone"
    ]

    def __init__(self, guild, author, channel, time):
        self.guild = guild
        self.author = author
        self.channel = channel
        self.created_time = time

        self.letters_guessed = []
        self.word = random.choice(Game.words_list)
        self.display_word = ["_" for x in range(len(self.word))]
        self.guesses_remaining = 7

    def guess(self, letter):
        letter = letter.lower()
        if letter in self.letters_guessed:
            return (1, "Already guessed this letter, try again!")
        elif letter in self.word:
            for index, character in enumerate(self.word):
                if character == letter:
                    self.display_word[index] = letter

            if '_' not in self.display_word:
                return (2, f"Congratulations! You win!\nThe word was `{self.word}`")

            return (0, "Correct guess!")
        else:
            self.letters_guessed.append(letter)
            self.guesses_remaining -= 1
            if self.guesses_remaining == 0:
                return (-2, "Sorry, you lose!")
            return (-1, "Wrong guess!")

    def display_board(self):
        board = []

        if self.guesses_remaining <= 6:
            board.append("`         0         `")
            if self.guesses_remaining == 5:
                board.append("`         |         `")
                board.append("`                   `")
                board.append("`                   `")
            elif self.guesses_remaining == 4:
                board.append("`         |         `")
                board.append("`         |         `")
                board.append("`                   `")
            elif self.guesses_remaining == 3:
                board.append("`        /|         `")
                board.append("`         |         `")
                board.append("`                   `")
            elif self.guesses_remaining == 2:
                board.append("`        /|\\        `")
                board.append("`         |         `")
                board.append("`                   `")
            elif self.guesses_remaining == 1:
                board.append("`        /|\\        `")
                board.append("`         |         `")
                board.append("`        /          `")
            elif self.guesses_remaining == 0:
                board.append("`        /|\\        `")
                board.append("`         |         `")
                board.append("`        / \\        `")
            else:
                board.append("`                   `")
                board.append("`                   `")
                board.append("`                   `")

            board.append("")

        word_so_far = "`" + " ".join(self.display_word).center(19, " ") + "`"

        board.append(word_so_far)

        return "\n".join(board)
