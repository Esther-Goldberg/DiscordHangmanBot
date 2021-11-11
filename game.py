import random


class Game():

    WORDS_LIST = [
        "yesterday",
        "minecraft",
        "discord",
        "computer",
        "telephone"
    ]

    STARTER_BOARD = [
        '┍━━┑   ',
        '│      ',
        '│      ',
        '│      ',
        '│      ',
        '┶━━━━━━']

    HANGMAN_PARTS = {
        # wrong_guesses : [row, column, new_value]
        1: [1, 4, '0'],
        2: [2, 4, '|'],
        3: [3, 4, '|'],
        4: [2, 3, '/'],
        5: [2, 5, '\\'],
        6: [4, 3, '/'],
        7: [4, 4, '\\']
    }


    def __init__(self, guild, author, channel, time):
        self.guild = guild
        self.author = author
        self.channel = channel
        self.created_time = time

        self.letters_guessed = []
        self.word = random.choice(Game.WORDS_LIST)
        self.display_word = ["_" for x in range(len(self.word))]
        self.wrong_guesses = 0
        self.board = Game.STARTER_BOARD[:]


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
            self.wrong_guesses += 1
            self.update_board()
            if self.wrong_guesses == 7:
                return (-2, "Sorry, you lose!")
            return (-1, "Wrong guess!")

    def update_board(self):
        row, column, string = Game.HANGMAN_PARTS[self.wrong_guesses]
        self.board[row] = self.board[row][:column] + string + self.board[row][column + 1:]

    def display_board(self):
        word_so_far = "`" + " ".join(self.display_word).center(19, " ") + "`"
        return ("\'" + "\n".join(self.board) + "\'" + "\n" + word_so_far)
