import random

import unicodedata
from typing import TYPE_CHECKING, Literal

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
            response: discord.InteractionResponse = interaction.response  # type: ignore
            await response.send_message(view=view, ephemeral=True, content="Your cards:")

        button.callback = callback
        demo.add_item(button)

        await ctx.send(content="_ _", view=demo)


def setup(bot: bot_t) -> None:
    bot.add_cog(Game(bot))
