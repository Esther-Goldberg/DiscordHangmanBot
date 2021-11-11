from discord.ext import commands
from datetime import datetime

import game


class Hangman(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.games = {}

    @commands.command()
    async def sayHello(self, ctx):
        print('received message!')
        await ctx.send('Hello!')

    @commands.command()
    async def hangman(self, ctx):
        if ctx.guild in self.games:
            time = self.games[ctx.guild].created_time
            if (datetime.now() - time).total_seconds() > 5*60:
                self.games[ctx.guild] = game.Game(ctx.guild, ctx.author, ctx.channel, datetime.now())
                await ctx.send(f'Game started\nUse `!guess <letter>` to guess!\nYour word is\n{self.games[ctx.guild].display_board()}')
            else:
                await ctx.send('Game already in progress')
        else:
            self.games[ctx.guild] = game.Game(ctx.guild, ctx.author, ctx.channel, datetime.now())
            await ctx.send(f'Game started\nUse `!guess <letter>` to guess!\nYour word is\n{self.games[ctx.guild].display_board()}')

    @commands.command()
    async def guess(self, ctx, letter):
        if ctx.guild in self.games:
            game = self.games[ctx.guild]
            if game.author == ctx.author:
                code, message = game.guess(letter.lower()[0])

                if code != 2:
                    message += "\n"
                    message += game.display_board()
                    if code == -2:
                        message += f"\nYour word was`{game.word}`"
                        message += "\nTry again!"
                        del self.games[ctx.guild]
                else:
                    del self.games[ctx.guild]
                await ctx.send(message)
            else:
                await ctx.send("You are not the current player!")
        else:
            await ctx.send("No game in progress! Use `!hangman` to start a game")
