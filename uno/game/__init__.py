import unicodedata
from typing import TYPE_CHECKING, Literal

import discord
from discord.ext import commands
from discord.ui import (
    View, Button
)

if TYPE_CHECKING:
    from uno import UNO as bot_t
else:
    bot_t = commands.Bot


class Card:
    def __init__(self, number: int, colour: Literal["\U0001f7e5", "\U0001f7e8", "\U0001f7e9", "\U0001f7e6"]):
        self.number = number
        self.colour = colour

    def __str__(self):
        if self.number < 10:
            return f'{self.colour}{self.number}\ufe0f\u20e3'


class UNOView(View):
    def __init__(self):
        super().__init__(timeout=None)


int_names = [
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
    "🔃", "🚫", "+2", "+4", "🏳️‍"
]


class Game(commands.Cog):
    def __init__(self, bot: bot_t) -> None:
        self.bot = bot

    @commands.command()
    async def new(self, ctx: commands.Context) -> None:
        view = View(None)
        # view.add_item(Button(style=discord.ButtonStyle.red, emoji="\U0001f6ab"))
        x = 0
        for c in ["\U0001f7e5", "\U0001f7e8", "\U0001f7e9", "\U0001f7e6"]:
            if x == 25:
                break
            for i in int_names:
                x += 1
                if x == 25:
                    break

                view.add_item(Button(emoji=c if i.isdigit() else None, label=i, style=discord.ButtonStyle.grey))
        view.add_item(Button(style=discord.ButtonStyle.grey, emoji="\u27a1\ufe0f"))
        await ctx.send(content="_ _", view=view)


def setup(bot: bot_t) -> None:
    bot.add_cog(Game(bot))
