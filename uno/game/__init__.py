import dataclasses
import random

import unicodedata
from typing import TYPE_CHECKING, Literal, Optional

import discord
from discord.ext import commands
from discord.ui import (
    View, Button, button
)

from uno.emojis import all_emojis

if TYPE_CHECKING:
    from uno import UNO as bot_t
else:
    bot_t = commands.Bot


Colour = Literal["red", "blue", "green", "yellow", "other"]
# zero,one,two,three,four,five,six,seven,eight,nine,+2,reverse,skip
Number = Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# +4 = 0, colour change = 1


@dataclasses.dataclass
class Card:
    colour: Colour
    number: Number

    def to_emoji(self) -> discord.PartialEmoji:
        return all_emojis[self.colour][self.number]


class Player:
    def __init__(self, member: discord.Member):
        self.member = member
        self._hand: list[Card] = []

    @property
    def hand(self) -> list[Card]:
        return sorted(self._hand, key=lambda c: (c.colour, c.number))


class UNOGame(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.players: list[Player] = []
        self.top_deck: Optional[Card] = None
        self.reversed = False
        self._current_player: Literal[0, 1, 2, 3] = 0


class Game(commands.Cog):
    def __init__(self, bot: bot_t) -> None:
        self.bot = bot

    @commands.command()
    async def new(self, ctx: commands.Context) -> None:
        demo = View()
        button = Button(style=discord.ButtonStyle.blurple, label="Show cards")

        async def callback(interaction: discord.Interaction):
            view = View()

            for i in range(24):
                view.add_item(Button(style=discord.ButtonStyle.grey, emoji=random.choice(all_emojis)))
            view.add_item(Button(style=discord.ButtonStyle.grey, emoji="\u27a1\ufe0f"))
            response: discord.InteractionResponse = interaction.response
            await response.send_message(view=view, ephemeral=True, content="Your cards:")

        button.callback = callback
        demo.add_item(button)

        await ctx.send(content="_ _", view=demo)


def setup(bot: bot_t) -> None:
    bot.add_cog(Game(bot))
